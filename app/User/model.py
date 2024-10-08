from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

from app.core import Base
from app.Post import Post
from app.Role import Role


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey('roles.id', ondelete="SET NULL"))

    posts: Mapped[list["Post"]] = relationship(
        back_populates="author",
        lazy="dynamic",
    )

    role: Mapped["Role"] = relationship(
        back_populates="users",
        lazy="joined",
    )
