import json

from django.http import HttpResponse
from django.shortcuts import render
import sqlalchemy, sqlalchemy.orm
from .models import Base, Сonstruction

engine = sqlalchemy.create_engine('sqlite:///construction.sqlite')
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

def create(request):
    car_id = request.GET.get("car_id")
    worker_id = request.GET.get("worker_id")
    if car_id and worker_id:
        construction = Сonstruction(car_id=car_id, worker_id=worker_id)
        session.add(construction)
        session.commit()
        return HttpResponse(construction)
    else:
        return HttpResponse("Введите car_id и worker_id")

def update(request):
    id = request.GET.get("id")
    rows_name = request.GET.get("name")
    new_parameter = request.GET.get("new_parameter")
    construction = session.query(Сonstruction).filter(Сonstruction.id==id).first()
    if all([id, rows_name, new_parameter]):
        if rows_name=="worker_id": construction.worker_id = new_parameter
        if rows_name == "car_id": construction.car_id = new_parameter
        session.add(construction)
        session.commit()
        session.refresh(construction)
        return HttpResponse(construction)
    else: return HttpResponse("Введите (id,rows_name,new_parameter)")


def index(request):
    return HttpResponse(session.query(Сonstruction).all())


