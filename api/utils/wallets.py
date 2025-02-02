from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import event
from db.models.user import User
from db.models.wallet import Wallet
from db.models.bid import Bid
from db.models.lot import Lot


def get_wallets(db: Session):
    return db.query(Wallet).all()

def add_funds(db: Session, user_id: UUID, funds: int):
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
    wallet.balance += funds
    db.add(wallet)
    db.commit()
    return f"Successfully added {funds} to the wallet. New balance: {wallet.balance}"

def subtract_funds(db: Session, user_id: UUID, funds: int):
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()

    wallet.balance -= funds
    db.add(wallet)
    db.commit()
    return f"Successfully removed {funds} from the wallet. New balance: {wallet.balance}"


# EVENTS -----------------------------------------------------------

@event.listens_for(User, "after_insert")
def create_wallet(mapper, connection, target):
    session = Session(bind=connection)
    wallet = Wallet(user_id=target.id)
    session.add(wallet)
    session.commit()

@event.listens_for(Bid, "after_insert")
def deduct_balance(mapper, connection, target):
    db = Session(bind=connection)
    subtract_funds(db, target.user_id, target.amount)

@event.listens_for(Bid, "before_insert")
def validate_bid(mapper, connection, target):
    db = Session(bind=connection)
    current_lot = db.query(Lot).filter(Lot.lot_id == target.lot_id).first()
    current_bid = db.query(Bid).filter(Bid.bid_id == current_lot.current_bid).first()
    wallet = db.query(Wallet).filter(Wallet.user_id == target.user_id).first()

    if not wallet:
        raise ValueError("No wallet found")
    if wallet.balance < target.amount:
        raise ValueError(f"Insuficent ballence. Balance: {wallet.balance} Amount Bid: {target.amount}")
    if target.amount <= current_bid.amount: 
        raise ValueError(f"The amount bid {target.amount} must be larger than the current bid amount {current_bid.amount}")