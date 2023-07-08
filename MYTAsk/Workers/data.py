
from sqlalchemy import ForeignKey, Integer,Column,String
from database import Base
from fireDepartments import data

class Workers(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    secondName = Column(String)
    age = Column(Integer)
    phoneNumber = Column(String)
    position = Column(String)
    shift_number = Column(Integer)
    fireDeparmentID = Column('fire_department_id', Integer, ForeignKey(data.FireDeparments.id))


    