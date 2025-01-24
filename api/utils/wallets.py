from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import event
from db.models.user import User
from db.models.wallet import Wallet
from db.models.bid import Bid


def get_wallets(db: Session):
    return db.query(Wallet).all()

def add_funds(db: Session, user_id: UUID, funds: int):
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
    wallet.balance += funds
    db.add(wallet)
    db.commit()
    return f"Successfully added {funds} to the wallet. New balance: {wallet.balance}"

@event.listens_for(User, "after_insert")
def create_wallet(mapper, connection, target):
    """Create a wallet automatically when a user is created."""
    session = Session(bind=connection)
    wallet = Wallet(user_id=target.id)
    session.add(wallet)
    session.commit()

@event.listens_for(Bid, "before_insert")
def check_and_deduct_balance(mapper, connection, target):
    # Fetch the user's wallet
    session = Session(bind=connection)
    wallet = session.query(Wallet).filter_by(user_id=target.user_id).first()

    if not wallet:
        raise ValueError("User does not have a wallet.")

    if wallet.balance < target.amount:
        raise ValueError("Insufficient wallet balance to place this bid.")

    # Deduct the balance
    wallet.balance -= target.amount
    session.add(wallet)
    session.commit()