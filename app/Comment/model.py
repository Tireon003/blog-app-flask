from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String
from typing import TYPE_CHECKING
from datetime import datetime

from app.core import Base
from app.utils import datetime_utcnow

if TYPE_CHECKING:
    from app.User import User
    from app.Post import Post


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete="CASCADE"),
        nullable=False,
    )
    post_id: Mapped[int] = mapped_column(
        ForeignKey('posts.id', ondelete="CASCADE"),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime_utcnow, nullable=False)
