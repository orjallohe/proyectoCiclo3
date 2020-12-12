from db.Producto_db import ProductoInDB
from db.Producto_db import database_productos
from db.Producto_db import update_producto, get_producto
from models.Producto_models import ProductoIn, ProductoOut  
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.get("/producto")
async def listar_producto():
    return {"Lista de productos": database_productos}  
  
'''Mostrar productos por el codigo'''
@api.get("/producto/{codigo}")
async def buscar_producto(codigo: int):
    producto_in_db = get_producto(codigo)
    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    producto_out = ProductoOut(**producto_in_db.dict())
    return producto_out

'''Crear productos'''
@api.post("/producto/{codigo}")
async def crear_producto(producto: ProductoInDB):
    database_productos[producto.codigo]=producto
    return producto

'''Modificar productos'''
@api.put("/producto/")
async def modificar_producto(producto: ProductoInDB):
    database_productos[producto.codigo]=producto
    return producto

'''Eliminar productos'''
@api.delete("/producto/")
async def eliminar_producto(producto: ProductoInDB):
    del database_productos[producto.codigo]
    return producto

