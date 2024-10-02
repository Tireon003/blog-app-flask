from flask import Flask

from config import settings


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.db_url


@app.get("/about")
def index():
    return '<h1 style="color: green">Index</h1>'


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
