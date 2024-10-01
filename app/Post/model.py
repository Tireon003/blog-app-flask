from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from app.core import Base
from app.utils import datetime_utcnow

if TYPE_CHECKING:
    from app.User import User


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(60), nullable=False)
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    created_at: Mapped[datetime] = mapped_column(default=datetime_utcnow)
    views: Mapped[int] = mapped_column(default=0)

    author: Mapped["User"] = relationship(
        back_populates="posts",
        lazy="joined",
    )
