from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn main:app --reload
#Iniciar entorno virtual: venv\Scripts\activate

#Entidad user
#BaseModel: es una clase base para crear modelos de datos (crear una entidad)
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User( id = 1, name = "Juan Jose", surname = "jotapar", age = 22),
              User(id = 2, name = "Lucila", surname = "Cilo", age = 54)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Juan Jose", "surname": "jotapar", "age": 22},
           {"name": "Lucila", "surname": "Cilo", "age": 54}]


@app.get("/users")
async def users():
    return users_list

# llamada mediante Path
@app.get("/user/{id}")
async def user(id:int):
    return (search_user(id))

#llamada mediante Query 
@app.get("/userquery/")
async def user(id:int):
    return (search_user(id))



def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}
