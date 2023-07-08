from sqlalchemy.orm import Session
from data import Workers

def updateWorker(id: int, row_name:str, newParameter: str, db: Session):
    worker = db.query(Workers).filter(Workers.id==id).first()
    if worker:
        if row_name == 'firstName': worker.firstName = newParameter
        elif row_name == 'secondName': worker.secondName = newParameter
        elif row_name == 'age': worker.age = newParameter
        elif row_name == 'phoneNumber': worker.phoneNumber = newParameter
        elif row_name == 'position': worker.position = newParameter
        elif row_name == 'shift_number': worker.shift_number = newParameter
        elif row_name == 'fireDeparmentID': worker.fireDeparmentID = newParameter
        db.add(worker)
        db.commit()
        db.refresh(worker)
        return worker
    else:
        return {
            "Message" : "Данного работника не существует!!!"
        }
    
  

def create_token(firstName: str, secondName: str, age: int, phoneNumber: str,
                 position: str, shipt_number: int, fire_department_id: int, db:Session):
    worker = Workers(firstName=firstName, secondName=secondName, age=age, phoneNumber=phoneNumber,
                     position=position, shift_number=shipt_number, fireDeparmentID=fire_department_id)
    db.add(worker)
    db.commit()
    db.refresh(worker)
    return worker

def get_all(db: Session):
    return db.query(Workers).all()
    