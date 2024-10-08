from sqlalchemy import select, delete
from flask_sqlalchemy import SQLAlchemy

from .model import Role


class RoleRepository:

    def __init__(self, db: SQLAlchemy) -> None:
        self.__db = db

    def insert(self, name: str) -> None:
        role = Role(name=name)
        self.__db.session.add(role)
        self.__db.session.commit()

    def select(self) -> list[Role] | None:
        stmt = select(Role)
        roles = self.__db.session.scalars(stmt).all()
        return roles

    def delete(self, role_id: int) -> None:
        stmt = (
            delete(Role)
            .filter_by(id=role_id)
        )
        self.__db.session.execute(stmt)
        self.__db.session.commit()
