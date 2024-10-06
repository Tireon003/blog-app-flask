from typing import TYPE_CHECKING

from .model import Role

if TYPE_CHECKING:
    from .repository import RoleRepository


class RoleService:

    def __init__(self, repo: "RoleRepository"):
        self.repo = repo

    def create_role(self, role_name: str) -> None:
        self.repo.insert(name=role_name)

    def get_roles(self) -> list[Role]:
        roles = self.repo.select()
        return roles

    def delete_role(self, role_id: int) -> None:
        self.repo.delete(role_id=role_id)
