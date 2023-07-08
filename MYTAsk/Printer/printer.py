# import uvicorn
# from fastapi import FastAPI
# import requests
#
# # Создание веб-сервера на FastAPI
# app = FastAPI()
#
# @app.get('/print/{id}')
# async def test_api(id: int = None):
#    res = requests.get(f'http://localhost:8083/token/use/{id}').json()
#    if 'token_count' in res and res['token_count']<res['token_limit']:
#       task=requests.get(f'http://localhost:8082/task_generator').json()
#       print(f"{task['first_number']}{task['operation_symbol']}{task['second_number']}=")
#       return task
#    else:
#       print(res)
#       return res
#
# if __name__ == '__main__':
#    uvicorn.run(
#       'printer:app',
#       host = 'localhost',
#       port = 8080,
#       reload = True
#    )
from httpx import AsyncClient
client = AsyncClient()


import uvicorn
from fastapi import FastAPI
import requests

# Создание веб-сервера на FastAPI
app = FastAPI()

@app.get('/print')
async def main():
    r = await client.get('http://127.0.0.1:8000/get_constructions')
    return r.text


if __name__ == '__main__':
   uvicorn.run(
      'printer:app',
      host = 'localhost',
      port = 8085,
      reload = True
   )