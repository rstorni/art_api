from fastapi import APIRouter


router = APIRouter()


@router.get('/auctions')
def read_auctions():
    pass

@router.get('/auctions/{auction_id}')
def read_auction():
    pass

@router.post('/create_auction')
def create_auction():
    pass