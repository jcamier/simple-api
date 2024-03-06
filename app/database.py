import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Name of your SQLite database file
DB_NAME = os.getenv('DB_NAME', 'historical_weather_data.db')

# Construct the absolute path for the SQLite URL
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, DB_NAME)}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
