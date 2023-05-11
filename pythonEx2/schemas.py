from typing import Optional
from sqlite3 import Date
from pydantic import BaseModel, HttpUrl


class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: Date
    main_phone: str
    cell_phone: str
    address: str
    positive_date: Optional[Date] | None
    recovery_date: Optional[Date] | None

    class Config:
        orm_mode = True


class Injection(BaseModel):
    id: int
    producer: str
    date: Date

    class Config:
        orm_mode = True


class Result(BaseModel):
    date: Date
