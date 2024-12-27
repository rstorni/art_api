from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql+psycopg2://localhost:5432/art_db'
Base = declarative_base()

engine = create_engine(
   DATABASE_URL, 
   connect_args={}, 
   future=True, 
   echo=True
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    future=True, 
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()