from fastapi import FastAPI

app = FastAPI()

@app.get("/")  #se hace get(obtiene) a la ruta "/"
async def root(): #"async" con esta linea se especifica que sea asincrono (para poder llamar al servidor de la api)
    return {"message": "Hello World"}