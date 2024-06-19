"""
Database management tools - mostly for development.
"""

import logging

from sqlalchemy import create_engine

from auctions import models  # pylint: disable=unused-import
from auctions.database import Base, get_db_conn_string


def init_db():
    conn_str = get_db_conn_string(is_async=False)
    logging.info("Initializing database...")
    engine = create_engine(conn_str, echo=True)
    with engine.begin() as conn:
        Base.metadata.drop_all(conn)
        Base.metadata.create_all(conn)
