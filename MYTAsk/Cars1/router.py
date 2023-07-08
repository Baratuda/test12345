from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import service
from database import get_db

router = APIRouter()

@router.post('/create/{car_brand}/{car_number}/{chassis_number}/{height}/{speed}/{type_of_car}/{tons_of_water}/{min_combat_crew}/{fire_department_id}')
async def create(car_brand: str, car_number: str, chassis_number: str, height: int, speed: int,
                 type_of_car: str, tons_of_water: int, min_combat_crew: int, fire_department_ID: int,
                 db:Session = Depends(get_db)):
   service.createCar(car_brand, car_number, chassis_number, height, speed,
                     type_of_car, tons_of_water, min_combat_crew, fire_department_ID, db)

@router.get('/update_worker/{id}/{row_name}/{newParameter}')
async def updateWorker(id: int, row_name:str, newParameter: str, db:Session = Depends(get_db)):
   service.updateCar(id, row_name, newParameter, db)

@router.get('/list')
async def get_list(db:Session = Depends(get_db)):
   return service.get_all(db)      
