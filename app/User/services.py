from typing import TYPE_CHECKING
from datetime import datetime
from injector import inject

from .model import User

if TYPE_CHECKING:
    from .repository import UserRepository


class UserService:

    def __init__(self, repo: "UserRepository") -> None:
        self.repo = repo

    def create_user(
            self,
            username: str,
            hashed_password: str,
            email: str,
            date_of_birth: datetime | None = None,
            role_id: int = 1
    ) -> None:
        self.repo.insert(
            username=username,
            hashed_password=hashed_password,
            email=email,
            date_of_birth=date_of_birth,
            role_id=role_id
        )

    def get_by_id(self, user_id: int) -> User | None:
        user = self.repo.select(user_id=user_id)
        return user

    def set_new_params(self, user_id: int, **kwargs) -> None:
        self.repo.update(user_id=user_id, **kwargs)

    def remove_user(self, user_id: int) -> None:
        self.repo.delete(user_id=user_id)
