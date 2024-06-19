from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from auctions.database import Base


class Auction(Base):
    __tablename__ = "auctions"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    reserve_price: Mapped[int] = mapped_column(Integer(), default=0)
    winner: Mapped[str] = mapped_column(String(255), nullable=True)
    seller: Mapped[str] = mapped_column(String(255), nullable=False)
    sold_price: Mapped[int] = mapped_column(Integer(), nullable=True)
    current_high_bid: Mapped[int] = mapped_column(Integer(), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),  # pylint: disable=not-callable
        onupdate=func.now(),  # pylint: disable=not-callable
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),  # pylint: disable=not-callable
        onupdate=func.now,
    )
    ends_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False)

    item: Mapped["Item"] = relationship("Item", back_populates="auction")


class Item(Base):
    __tablename__ = "items"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    make: Mapped[str] = mapped_column(String(255), nullable=False)
    model: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column(Integer(), nullable=False)
    color: Mapped[str] = mapped_column(String(255), nullable=False)
    mileage: Mapped[int] = mapped_column(Integer(), nullable=False)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False)

    auction_id: Mapped[UUID] = mapped_column(ForeignKey("auctions.id"), nullable=True)
    auction: Mapped[Auction] = relationship(
        "Auction", back_populates="item", cascade="all, delete-orphan", single_parent=True
    )
