from sqlalchemy import Integer,Column,String
from database import Base

class FireDeparments(Base):
    __tablename__ = 'fire_deparments'
    id = Column(Integer, primary_key=True, index=True)
    fireDeparmentsName = Column(String)
    locationFireDeparment = Column(String)


    