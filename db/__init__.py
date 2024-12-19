from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#connect to database
engine = create_engine('postgresql://localhost:5432/art_db', echo=True)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()