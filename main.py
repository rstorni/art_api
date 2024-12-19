from fastapi import FastAPI
from api.routes import auctions
from db import model, engine
from api.routes import users, auctions

# Create FastAPI app
app = FastAPI(
        title='Art API',
        description='Api for managing art auction data'
)

# Include routes
app.include_router(users.router)
app.include_router(auctions.router)

# Function to initialize the database
def init_db():
    print("Initializing the database...")
    model.Base.metadata.create_all(bind=engine)
    print("Database initialized!")

# Main function
if __name__ == "__main__":
    import uvicorn

    # Initialize the database
    init_db()

    # Start the FastAPI server
    print("Starting FastAPI...")
    uvicorn.run(app, host="0.0.0.0", port=8000)