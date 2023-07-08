from sqlalchemy.orm import Session

from data import Cars


def updateCar(id: int, row_name:str, newParameter: str, db: Session):
    worker = db.query(Cars).filter(Cars.id == id).first()
    if worker:
        if row_name == 'car_brand': worker.car_brand = newParameter
        elif row_name == 'car_number': worker.car_number = newParameter
        elif row_name == 'chassis_number': worker.chassis_number = newParameter
        elif row_name == 'height': worker.height = newParameter
        elif row_name == 'speed': worker.speed = newParameter
        elif row_name == 'type_of_car': worker.type_of_car = newParameter
        elif row_name == 'tons_of_water': worker.tons_of_water = newParameter
        elif row_name == 'min_combat_crew': worker.min_combat_crew = newParameter
        elif row_name == 'fire_department_ID': worker.fire_department_ID = newParameter
        db.add(worker)
        db.commit()
        db.refresh(worker)
        return worker
    else:
        return {
            "Message" : "Данной машины не существует!!!"
        }
    
  

def createCar(car_brand: str, car_number: str, chassis_number: str, height: int, speed: int,
               type_of_car: str, tons_of_water: int, min_combat_crew: int, fire_department_ID: int, db:Session):
    car = Cars(car_brand=car_brand, car_number=car_number, chassis_number=chassis_number, height=height, speed=speed,
               type_of_car=type_of_car, tons_of_water=tons_of_water, min_combat_crew=min_combat_crew,
               fire_department_ID=fire_department_ID)
    db.add(car)
    db.commit()
    db.refresh(car)
    return car

def get_all(db: Session):
    return db.query(Cars).all()
    