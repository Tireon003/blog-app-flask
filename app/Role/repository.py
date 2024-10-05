from sqlalchemy import select, delete

from app.core import BaseRepository
from .model import Role

class RoleRepository(BaseRepository):

    def insert(self, name: str) -> None:
        role = Role(name=name)
        self.db.session.add(role)
        self.db.session.commit()

    def select(self) -> list[Role] | None:
        stmt = select(Role)
        roles = self.db.session.scalars(stmt).all()
        return roles

    def delete(self, role_id: int) -> None:
        stmt = (
            delete(Role)
            .filter_by(id=role_id)
        )
        self.db.session.execute(stmt)
        self.db.session.commit()
