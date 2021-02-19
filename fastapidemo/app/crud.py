from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()

def get_people(db: Session, skip: int = 0, limit: int = 100):        
    return db.query(models.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.Person):    
    db_person = models.Person(
      name=person.name, 
      last_name=person.last_name,
      mother_last_name=person.mother_last_name,
      date_of_birth=person.date_of_birth
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, db_person: models.Person, person: schemas.Person):
    db_person.name=person.name
    db_person.last_name=person.last_name
    db_person.mother_last_name=person.mother_last_name
    db_person.date_of_birth=person.date_of_birth    
    db.commit()
    return db_person

def delete_person(db: Session, person: schemas.Person):
    db.delete(person)
    db.commit()
    return True


