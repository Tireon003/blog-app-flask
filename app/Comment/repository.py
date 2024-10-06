from sqlalchemy import select, delete

from app.core import BaseRepository
from .model import Comment


class CommentRepository(BaseRepository):

    def select_from_post(self, post_id: int) -> list[Comment]:
        stmt = (
            select(Comment)
            .filter_by(post_id=post_id)
            .order_by(Comment.created_at.desc())
        )
        result = self.__db.session.execute(stmt).scalars()
        comments = [comment for comment in result.all()]
        return comments

    def update(self, comment_id: int, content: str) -> None:
        comment = self.__db.get(Comment, comment_id)
        if comment:
            comment.content = content
            self.__db.session.add(comment)
            self.__db.session.commit()

    def insert_to_post(self, post_id: int, owner_id: int, content: str) -> None:
        comment = Comment(
            owder_id=owner_id,
            post_id=post_id,
            content=content,
        )
        self.__db.session.add(comment)
        self.__db.session.commit()

    def delete(self, comment_id: int) -> None:
        stmt = (
            delete(Comment)
            .filter_by(id=comment_id)
        )
        self.__db.session.execute(stmt)
        self.__db.session.commit()
