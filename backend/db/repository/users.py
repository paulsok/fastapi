from core.hashing import Hasher
from db.models.users import User
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create_new_job(job: JobCreate,db: Session,owner_id:int):
    job_object = Job(**job.dict(),owner_id=owner_id)
    db.add(job_object)
    db.commit()
    db.refresh(job_object)
    return job_object


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user
