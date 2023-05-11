from typing import Optional, List
from sqlite3 import Date

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import schemas
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# get all employees:
@app.get("/")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()


# get all injections:
@app.get("/injections")
def get_injections(db: Session = Depends(get_db)):
    return db.query(models.Injection).all()


# get all injections date:
@app.get("/injections_date_list")
def injections_date_list(db: Session = Depends(get_db)):
    injectionList = db.query(models.Injection)
    dateList = []
    for injection in injectionList:
        dateList.append(injection.date)
    return dateList


# get all injections producers:
@app.get("/injections_producer_list")
def injections_producer_list(db: Session = Depends(get_db)):
    injectionList = db.query(models.Injection)
    producerList = []
    for injection in injectionList:
        producerList.append(injection.producer)
    return producerList


# get employee by id:
@app.get("/employees/{employee_id}")
def employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    # gourd close
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    return employee


# create new employee:
@app.post("/employees/")
def create_employee(employee: schemas.Employee, db: Session = Depends(get_db)):
    employee_search = db.query(models.Employee).filter(models.Employee.id == employee.id).first()
    # gourd close
    if employee_search is not None:
        raise HTTPException(
            status_code=422,
            detail=f"ID {employee.id} : employee already exist"
        )
    employee_model = models.Employee()
    employee_model.id = employee.id
    employee_model.first_name = employee.first_name
    employee_model.last_name = employee.last_name
    employee_model.birth_date = employee.birth_date
    employee_model.address = employee.address
    employee_model.main_phone = employee.main_phone
    employee_model.cell_phone = employee.cell_phone

    db.add(employee_model)
    db.commit()

    return employee


# add injection to employee by his id:
@app.put("/{employee_id}")
def add_injection(employee_id: int, injection: schemas.Injection, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    # gourd close
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    if db.query(models.Injection).filter(models.Injection.owner_id == employee_id).count() >= 4:
        raise HTTPException(
            status_code=403,
            detail=f"ID {employee_id} : has already 4 injections"
        )
    injection_model = models.Injection()
    injection_model.id = injection.id
    injection_model.date = injection.date
    injection_model.owner_id = employee_id
    injection_model.producer = injection.producer

    db.add(injection_model)
    db.commit()

    return injection


# get all injections of specific employee:
@app.get("/injection/{employee_id}")
def get_employee_injections(employee_id: int, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    # gourd close
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    injections = db.query(models.Injection).filter(models.Injection.owner_id == employee_id).all()
    return injections


# set positive results date:
@app.post("/positive/{employee_id}")
def add_positive_result(employee_id: int, positive_result: schemas.Result, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    employee_model.positive_date = positive_result.date
    db.commit()  # Commit the changes to the database
    db.refresh(employee_model)
    return employee_model


# get positive results date:
@app.get("/positive/{employee_id}")
def get_positive_result(employee_id: int, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    return employee_model.positive_date


# set recovery results date:
@app.post("/recovery/{employee_id}")
def add_positive_result(employee_id: int, recovery_result: schemas.Result, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    if employee_model.positive_date is None:
        raise HTTPException(
            status_code=422,
            detail=f"ID {employee_id} : employee wasn't sick"
        )
    employee_model.recovery_date = recovery_result.date
    db.commit()  # Commit the changes to the database
    db.refresh(employee_model)
    return employee_model


# get recovery results date
@app.get("/recovery/{employee_id}")
def get_recovery_result(employee_id: int, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )
    return employee_model.recovery_date


# delete employee (for personal use)
@app.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee_model = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if employee_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {employee_id} : employee not found"
        )

    db.query(models.Employee).filter(models.Employee.id == employee_id).delete()

    db.commit()

    return {f"ID {employee_id} : deleted "}
