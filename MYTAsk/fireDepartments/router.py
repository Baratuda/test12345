from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import service

router = APIRouter()

@router.post('/create/{fireDeparmentsName}/{locationFireDeparment}')
async def create(fireDeparmentsName: str, locationFireDeparment:str, db:Session = Depends(get_db)):
   service.create_token(fireDeparmentsName, locationFireDeparment, db)

@router.get('/updateFDN/{id}/{newName}')
async def updateFireDeparmentsName(id: int, newName: str, db:Session = Depends(get_db)):
   service.updateFireDeparmentsName(id,newName, db)   

@router.get('/list')
async def get_list(db:Session = Depends(get_db)):
   return service.get_all(db)      
