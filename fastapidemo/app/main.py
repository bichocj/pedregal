from typing import List

from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from . import crud, models, schemas
from .database import engine, SessionLocal
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app = FastAPI(template_folder='templates')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {"request": request }
    return templates.TemplateResponse("home.html", context)


@app.get("/people/", response_model=List[schemas.Person])
def list_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    people = crud.get_people(db, skip=skip, limit=limit)    
    return people

@app.get("/people/{person_id}", response_model=schemas.Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_person(person_id=person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@app.post("/people/", response_model=schemas.PersonCreate)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db, person=person)

@app.put("/people/{person_id}", response_model=schemas.Person)
def create_person(person_id: int, person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return crud.update_person(db, db_person=db_person, person=person)

@app.delete("/people/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    person = crud.get_person(db, person_id=person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    crud.delete_person(db, person=person)
    return True
