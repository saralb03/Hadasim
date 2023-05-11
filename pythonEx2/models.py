from pydantic import validator, HttpUrl
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Date
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    main_phone = Column(String)
    cell_phone = Column(String)
    address = Column(String)
    positive_date = Column(Date)
    recovery_date = Column(Date)
    injections = relationship("Injection", back_populates="owner")


class Injection(Base):
    __tablename__ = "injections"

    id = Column(Integer, primary_key=True, index=True)
    producer = Column(String)
    date = Column(Date)
    owner_id = Column(Integer, ForeignKey("employees.id"))

    owner = relationship("Employee", back_populates="injections")

