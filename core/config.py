from passlib.context import CryptContext
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ACCESS_TOKEN_EXPIRES = 24 * int(config("ACCESS_TOKEN_EXPIRES"))
ALGORITHM = config("ALGORITHM")
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
DB_URI = config("DB_URI")
DATABASE_NAME = config("DATABASE_NAME")
IMAP_SERVER = config("IMAP_SERVER")
IMAP_EMAIL = config("IMAP_EMAIL")
IMAP_PASSWORD = config("IMAP_PASSWORD")
