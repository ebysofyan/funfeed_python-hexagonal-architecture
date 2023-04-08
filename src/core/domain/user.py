from sqlalchemy import String, BigInteger
from .base import Base
from sqlalchemy.orm import mapped_column, MappedColumn


class User(Base):
    __tablename__ = "user__users"

    id: MappedColumn = mapped_column(BigInteger, primary_key=True)
    username: MappedColumn = mapped_column(String(50), nullable=False)
    password: MappedColumn = mapped_column(String)
    name: MappedColumn = mapped_column(String(100))
