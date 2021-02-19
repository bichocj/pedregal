from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    mother_last_name = Column(String(80), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    