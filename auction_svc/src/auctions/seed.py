"""
Database management tools - mostly for development.
"""

import logging
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from auctions import models  # pylint: disable=unused-import
from auctions.database import Base, get_db_conn_string


def init_db():
    conn_str = get_db_conn_string(is_async=False)
    logging.info("Initializing database...")
    engine = create_engine(conn_str, echo=True)
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)

    with Session(engine) as session:

        item_1 = models.Item(
            id=uuid.uuid4(),
            make="Toyota",
            model="Corolla",
            year=2019,
            color="blue",
            mileage=10000,
            image_url="https://via.placeholder.com/150",
        )

        item_2 = models.Item(
            id=uuid.uuid4(),
            make="Ford",
            model="Fusion",
            year=2018,
            color="red",
            mileage=20000,
            image_url="https://via.placeholder.com/150",
        )

        session.add_all([item_1, item_2])
        session.commit()
