import datetime
from typing import List, Optional

from pydantic import BaseModel

class PersonBase(BaseModel):    
    name: str
    last_name: str
    mother_last_name: str
    date_of_birth: datetime.date
    
    class Config:
        orm_mode = True

class Person(PersonBase):
    id: int

class PersonCreate(PersonBase):
    pass