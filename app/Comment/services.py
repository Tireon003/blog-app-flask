from typing import TYPE_CHECKING

from .model import Comment

if TYPE_CHECKING:
    from .repository import CommentRepository


class CommentService:

    def __init__(self, repo: "CommentRepository"):
        self.repo = repo

    def add_comment(self, post_id: int, owner_id: int, content: str) -> None:
        self.repo.insert_to_post(
            post_id=post_id,
            owner_id=owner_id,
            content=content,
        )

    def get_comments(self, post_id: int) -> list[Comment]:
        comments = self.repo.select_from_post(post_id=post_id)
        return comments

    def delete_comment(self, comment_id: int) -> None:
        self.repo.delete(comment_id=comment_id)

    def edit_comment(self, comment_id: int, content: str) -> None:
        self.repo.update(
            comment_id=comment_id,
            content=content,
        )
