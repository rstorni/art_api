from fastapi import FastAPI
from app.db import schema, engine
from app.routes import router

# Create FastAPI app
app = FastAPI()

# Include routes
app.include_router(router)

# Function to initialize the database
def init_db():
    print("Initializing the database...")
    schema.Base.metadata.create_all(bind=engine)
    print("Database initialized!")

# Main function
if __name__ == "__main__":
    import uvicorn

    # Initialize the database
    init_db()

    # Start the FastAPI server
    print("Starting FastAPI...")
    uvicorn.run(app, host="0.0.0.0", port=8000)