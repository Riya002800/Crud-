from fastapi import FastAPI, Depends  # FastAPI class and dependency injection
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud
from crud import create_user, get_users


# Create the tables in the database if they don't exist
Base.metadata.create_all(bind=engine)
from fastapi import HTTPException

app = FastAPI()

# Dependency to get a database session for each request
# This will automatically create and close the DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET endpoint to retrieve all users
# 'db: Session = Depends(get_db)' means: call get_db(), inject result as 'db'
@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# POST endpoint to add a new user
@app.post("/users")
def add_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name, email)

# PUT: Update an existing user's name or email
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str = None, email: str = None, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id, name, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found") # type: ignore
    return user

# DELETE: Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    result = crud.delete_user(db, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found") # type: ignore
    return {"message": "User deleted successfully"}
