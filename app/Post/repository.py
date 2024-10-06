from sqlalchemy import select

from app.core import BaseRepository
from .model import Post


class PostRepository(BaseRepository):

    def insert(self, title: str, content: str, author_id: int) -> None:
        post = Post(title=title, content=content, author_id=author_id)
        self.__db.session.add(post)

    def update(self,post_id: int,  title: str | None = None, content: str | None = None) -> None:
        post = self.__db.session.get(Post, post_id)
        if title:
            post.title = title
        if content:
            post.content = content
        self.__db.session.add(post)
        self.__db.session.commit()

    def increment_views(self, post_id: int) -> None:
        post = self.__db.session.get(Post, post_id)
        post.views += 1
        self.__db.session.add(post)
        self.__db.session.commit()

    def delete(self, post_id: int) -> None:
        post = self.__db.session.get(Post, post_id)
        self.__db.session.delete(post)
        self.__db.session.commit()

    def select_all(self) -> list[Post]:
        stmt = select(Post)
        return self.__db.session.scalars(stmt).all()

    def select_post_by_id(self, post_id: int) -> Post | None:
        return self.__db.session.get(Post, post_id)

    def get_by_author_id(self, author_id: int) -> list[Post]:
        return self.__db.session.scalars(select())
