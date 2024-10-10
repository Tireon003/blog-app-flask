from typing import TYPE_CHECKING

from .model import Post

if TYPE_CHECKING:
    from .repository import PostRepository


class PostService:

    def __init__(self, repo: "PostRepository"):
        self.repo = repo

    def create_post(self, title: str, content: str, author_id: int) -> None:
        self.repo.insert(
            title=title,
            content=content,
            author_id=author_id,
        )

    def edit_post(self, post_id: int,  title: str | None = None, content: str | None = None) -> None:
        self.repo.update(
            post_id=post_id,
            title=title,
            content=content,
        )

    def get_posts(self) -> list[Post] | None:
        posts = self.repo.select_all()
        return posts

    def get_post(self, post_id: int) -> Post | None:
        post = self.repo.select_post_by_id(post_id=post_id)
        self.repo.increment_views(post)
        return post

    def get_author_posts(self, author_id: int) -> list[Post] | None:
        posts = self.repo.select_by_author_id(author_id)
        return posts

    def delete_post(self, post_id: int) -> None:
        self.repo.delete(post_id=post_id)
