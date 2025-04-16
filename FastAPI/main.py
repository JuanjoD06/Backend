from fastapi import FastAPI

app = FastAPI()

#Documentación Oficial: https://fastapi.tiangolo.com/

#Instala FastAPI: pip install "fastapi[all]"
 
@app.get("/")  #se hace get(obtiene) a la ruta "/"
async def root(): #"async" con esta linea se especifica que sea asincrono (para poder llamar al servidor de la api)
    return {"message": "Hello World"}

#Url local: http://127.0.0.1:8000

@app.get("/url")
async def url():
    return {"url_curso":"https://www.youtube.com/watch?v=8vX2g0c4Y1E&list=PLzH6i7a3j5qk9d2xG4b7f3m5e6n8Q0l4r&index=1"}

#Inicia el server: uvicorn main:app --reload
#uvicorn es un servidor asincro para ejecutar la api
##main es el nombre del archivo
##app es el nombre de la variable que contiene la instancia de FastAPI
#/docs es la documentacion de la api
#/redoc es la documentacion alternativa