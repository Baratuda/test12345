from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, PrimaryKeyConstraint, UniqueConstraint, \
    ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
import sys
from sqlalchemy.orm import relationship
sys.path.append('/Users/User/PycharmProjects/MYTAsk')
from Cars1.data import Cars
from Workers.data import Workers
Base = declarative_base()
class Сonstruction(Base):
    __tablename__ = 'Сonstruction'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey(Cars.id),nullable=False)
    worker_id = Column(Integer, ForeignKey(Workers.id),nullable=False)

    car = relationship(Cars,backref="parent")
    worker = relationship(Workers, backref="parent")

    def __str__(self):
        return f'[car_id:{self.car_id}, worker_id:{self.worker_id}]         '
