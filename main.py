from fastapi import FastAPI

from api.routes import users, auctions
from db.db_setup import engine
from db.models import user

user.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
        title='Art API',
        description='Api for managing art auction data'
)

# Include routes
app.include_router(users.router)
app.include_router(auctions.router)
