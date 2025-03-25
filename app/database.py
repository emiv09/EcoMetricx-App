from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/productdb"
# SQLALCHEMY_DATABASE_URL = os.environ.get('RDS_URL')
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@fastapi-aws-database.ctkg44s4qpi1.eu-north-1.rds.amazonaws.com:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()