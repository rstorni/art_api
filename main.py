from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from api.routes import artworks, auctions, bids, lots, users, wallets
from db.db_setup import engine
from db.models import artwork, auction, bid, lot, user, wallet

user.Base.metadata.create_all(bind=engine)
artwork.Base.metadata.create_all(bind=engine)
auction.Base.metadata.create_all(bind=engine)
bid.Base.metadata.create_all(bind=engine)
lot.Base.metadata.create_all(bind=engine)
wallet.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create FastAPI app
app = FastAPI(
        title='Art API',
        description='Api for managing art auction data'
)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)



# Include routes
app.include_router(users.router)
app.include_router(artworks.router)
app.include_router(auctions.router)
app.include_router(bids.router)
app.include_router(lots.router)
app.include_router(wallets.router)
