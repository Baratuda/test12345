import uvicorn
from fastapi import FastAPI
from database import Base, engine
import router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router.router, prefix='/worker')


if __name__ == '__main__':
   uvicorn.run(
      'workers:app',
      host='localhost',
      port=8081,
      reload=True
   )