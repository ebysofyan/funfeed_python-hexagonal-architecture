from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "user__users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str | None] = mapped_column(String(100))
