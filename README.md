# Blog API on Flask
It is back-end API application for blog using Flask. I implemented base CRUD operations, data validation, interaction with Postgres by SQLAlchemy, migrations.

---
# Stack
- Python
- Flask
- Flask-Pydantic
- Flask-SQLAlchemy
- REST
- PostgreSQL
- Docker
- Alembic

---
# How to run
1. Install Docker on your system
2. Open terminal
3. Enter:
```commandline
git clone https://github.com/Tireon003/blog-app-flask.git
```
4. Create .env file in project folder with variables: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, SECRET_KEY
5. Enter command:
```shell
docker-compose up -d --build
```
Well, now project us running.

To stop project, enter:
```shell
docker-compose stop
```

# TODO
- Improve exception processing
- Add authentication