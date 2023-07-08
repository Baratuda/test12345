from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import service

router = APIRouter()

@router.post('/create/{firstName}/{secondName}/{age}/{phoneNumber}/{position}/{shipt_number}/{fire_department_id}')
async def create(firstName: str, 
                 secondName: str, 
                 age: int, 
                 phoneNumber: str, 
                 position: str, 
                 shipt_number: int,
                 fire_department_id: int,
                 db:Session = Depends(get_db)):
   service.create_token(firstName, secondName, age, phoneNumber, position, shipt_number,fire_department_id, db)

@router.get('/update_worker/{id}/{row_name}/{newParameter}')
async def updateWorker(id: int, row_name:str, newParameter: str, db:Session = Depends(get_db)):
   service.updateWorker(id,row_name,newParameter,db)

@router.get('/list')
async def get_list(db:Session = Depends(get_db)):
   return service.get_all(db)      
