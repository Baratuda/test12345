
from sqlalchemy import ForeignKey, Integer, Column, String
import sys
sys.path.append('/Users/User/PycharmProjects/MYTAsk/Cars1')
from database import Base
from fireDepartments import data


class Cars(Base):
    __tablename__ = 'Cars1'
    id = Column(Integer, primary_key=True, index=True)
    car_brand = Column(String)
    car_number = Column(String)
    chassis_number = Column(String)
    height = Column(Integer)
    speed = Column(Integer)
    type_of_car = Column(String)
    tons_of_water = Column(Integer)
    min_combat_crew = Column(Integer)
    fire_department_ID = Column('fire_department_id', Integer, ForeignKey(data.FireDeparments.id))


    