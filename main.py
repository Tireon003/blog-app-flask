from flask import Flask
from app.config import settings
from app.User import bp as user_bp
from app.core.database import db


def create_app():

    app = Flask(__name__)

    # Настройка конфигурации
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.db_url
    app.config["SECRET_KEY"] = settings.SECRET_KEY

    # Инициализация базы данных
    db.init_app(app)

    # Регистрация блюпринтов
    app.register_blueprint(user_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
