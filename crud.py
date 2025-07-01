from models import User
from sqlalchemy.orm import Session

# Function to get all users from the database
def get_users(db: Session):
    return db.query(User).all()

# Function to add a new user to the database
def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()  # Save changes
    db.refresh(user)  # Get updated object with ID
    return user
