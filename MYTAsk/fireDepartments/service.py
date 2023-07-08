from sqlalchemy.orm import Session
from data import FireDeparments

def updateFireDeparmentsName(fire_deparment_id:int, newName:str, db: Session):
    fire_deparment = db.query(FireDeparments).filter(FireDeparments.id==fire_deparment_id).first()
    if fire_deparment:
        fire_deparment.fireDeparmentsName = newName
        db.add(fire_deparment)
        db.commit()
        db.refresh(fire_deparment)
        return fire_deparment
    else:
        return {
            "Message" : "Данной пожарной части не существует!!!"
        }
    
  

def create_token(fireDeparmentsName: str, locationFireDeparment:str, db: Session):
    fireDeparments = FireDeparments(fireDeparmentsName = fireDeparmentsName, locationFireDeparment = locationFireDeparment)
    db.add(fireDeparments)
    db.commit()
    db.refresh(fireDeparments)
    return fireDeparments

def get_all(db: Session):
    return db.query(FireDeparments).all()
    