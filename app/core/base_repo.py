from flask_sqlalchemy import SQLAlchemy


class BaseRepository:

    def __init__(self, db: SQLAlchemy) -> None:
        self.__db = db
