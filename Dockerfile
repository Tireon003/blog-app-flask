FROM python:3.12

WORKDIR /server

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app/main.py"]
#CMD alembic upgrade head && python3 app/main.py