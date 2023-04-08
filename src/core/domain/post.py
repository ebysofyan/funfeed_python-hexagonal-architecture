
from sqlalchemy import (BigInteger, ForeignKey, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Post(Base):
    __tablename__ = "post__posts"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("user__users.id", ondelete="CASCADE")
    )

    user = relationship("User")


class PostImage(Base):
    __tablename__ = "post__post_images"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    url: Mapped[str] = mapped_column(String(50), nullable=False)
    post_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("post__posts.id", ondelete="CASCADE")
    )

    post: Mapped["Post"] = relationship()


class PostViewer(Base):
    __tablename__ = "post__post_viewers"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("user__users.id", ondelete="CASCADE")
    )
    post_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("post__posts.id", ondelete="CASCADE")
    )

    user = relationship("User")
    post: Mapped["Post"] = relationship()


class PostLike(Base):
    __tablename__ = "post__post_likes"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("user__users.id", ondelete="CASCADE")
    )
    post_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("post__posts.id", ondelete="CASCADE")
    )

    user = relationship("User")
    post: Mapped["Post"] = relationship()


class PostComment(Base):
    __tablename__ = "post__post_comments"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("user__users.id", ondelete="CASCADE")
    )
    post_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("post__posts.id", ondelete="CASCADE")
    )

    user = relationship("User")
    post: Mapped["Post"] = relationship()
