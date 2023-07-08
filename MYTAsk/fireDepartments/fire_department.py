import uvicorn
from fastapi import FastAPI
from database import Base,engine
import router

Base.metadata.create_all(bind= engine)
app = FastAPI()
app.include_router(router.router,prefix='/fire_departmen')


if __name__ == '__main__':
   uvicorn.run(
      'fire_department:app',
      host = 'localhost',
      port = 8080,
      reload = True
   )