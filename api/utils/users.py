from sqlalchemy.orm import Session

from db.models.user import User as db_UserClass
from validation_schemas.users import UserCreate


def get_user(db: Session, user_id: str):
    return db.query(db_UserClass).filter(db_UserClass.id == user_id).first()

def get_users(db: Session):
    return db.query(db_UserClass).all()

def create_user(db: Session, user: UserCreate):
    
    db_user = db_UserClass(
        username = user.username, 
        password = user.password, 
        first_name = user.first_name, 
        last_name = user.last_name, 
        email = user.email, 
        is_active =  user.is_active
        )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    