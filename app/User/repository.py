from datetime import datetime
from sqlalchemy import delete

from .model import User
from app.core import BaseRepository


class UserRepository(BaseRepository):

    def insert(
            self,
            username: str,
            hashed_password: str,
            email: str,
            date_of_birth: datetime | None = None,
            role_id: int = 1
    ) -> None:
        user = User(
            username=username,
            hashed_password=hashed_password,
            date_of_birth=date_of_birth,
            email=email,
            role_id=role_id,
        )
        self.db.session.add(user)
        self.db.session.commit()

    def select(self, user_id: int) -> User | None:
        user = self.db.session.get(User, user_id)
        return user

    def update(self, user_id: int, **kwargs) -> None:
        user = self.db.session.get(User, user_id)
        for k, v in kwargs.items():
            if hasattr(user, k):
                setattr(user, k, v)
        self.db.session.add(user)
        self.db.session.commit()

    def delete(self, user_id: int) -> None:
        stmt = (
            delete(User)
            .filter_by(id=user_id)
        )
        self.db.session.execute(stmt)
