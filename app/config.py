from uuid import uuid4
from socket import gethostbyname, gethostname


# Конфигурация
DEBUG = True
DATABASE = "database.db"
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = uuid4().bytes
HOST = gethostbyname(gethostname())
PORT = '5000'
