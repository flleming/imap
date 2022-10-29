import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import DB_URI, DATABASE_NAME

SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")
engine = create_engine("mysql+pymysql://{dbUri}/{dbName}".format(dbUri=DB_URI, dbName=DATABASE_NAME))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def getDb():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
