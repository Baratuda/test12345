import uvicorn
from fastapi import FastAPI

import router
from database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router.router, prefix='/car')


if __name__ == '__main__':
   uvicorn.run(
      'cars:app',
      host='localhost',
      port=8083,
      reload=True
   )