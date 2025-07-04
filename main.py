# from fastapi import FastAPI, Depends  # FastAPI class and dependency injection
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine, Base
# import crud

# # Create the tables in the database if they don't exist
# from database import SessionLocal, engine, Base

# app = FastAPI()

# # Dependency to get a database session for each request
# # This will automatically create and close the DB connection
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # GET endpoint to retrieve all users
# # 'db: Session = Depends(get_db)' means: call get_db(), inject result as 'db'
# @app.get("/users")
# def read_users(db: Session = Depends(get_db)):
#     return crud.get_users(db)

# # POST endpoint to add a new user
# @app.post("/users")
# def add_user(name: str, email: str, db: Session = Depends(get_db)):
#         return crud.create_user(db, name, email)

# @app.put("/users/{user_id}")
# def update_user(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
#     user = crud.get_user_by_id(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found") # type: ignore
#     return crud.update_user(db, user_id, name, email)

# # DELETE - Delete user by ID
# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = crud.get_user_by_id(db, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found") # type: ignore
#     return crud.delete_user(db, user_id)

# main.py (FastAPI)

from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import shutil
import os

import models
import database
import utils

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload-users/")
async def upload_users(file: UploadFile = File(...), db: Session = Depends(get_db)):
    My_file = f"temp_{load_workbook}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(load_workbook, buffer)

    try:
        users = utils.parse_excel(temp_file)
        if not users:
            raise HTTPException(status_code=400, detail="No valid user records found.")

        created = 0
        for user_data in users:
            
            existing = db.query(models.User).filter_by(email=user_data.email).first()
            if existing:
                continue
            user = models.User(
                name=user_data.name,
                email=user_data.email,
                phone=user_data.phone
            )
            db.add(user)
            created += 1

        db.commit()
        return {"message": f"Uploaded successfully. {created} users created."}
    finally:
        os.remove(My_file)
