from typing import Dict
from pydantic import BaseModel

class ProductoInDB(BaseModel):
    codigo: int
    nombre: str
    precio: int
    descripcion: str
    cantidad: int
    
database_productos = Dict[str, ProductoInDB]

database_productos = {
    1111 : ProductoInDB(**{"codigo":1111,
                             "nombre":"camiseta Tanktop",
                             "precio":150000,
                             "descripcion": "Esta camiseta Tanktop tiene aberturas debajo de las axilas, es perfecta para la temporada de festivales o para tu clase de yoga",
                             "cantidad":10}),
    
    1112 : ProductoInDB(**{"codigo":1112,
                             "nombre":"Coco Loco",
                             "precio":30000,
                             "descripcion": "Este cóctel para la piel tiene también aceite de naranja de Brasil, crema de coco y aceite de hierba limón, un trío tropical que se derrite por ti",
                             "cantidad":20})    
}

def get_producto(codigo: int):
    if codigo in database_productos.keys():
        return database_productos[codigo]
    else:
        return None   
def update_producto(producto_in_db: ProductoInDB):
    database_productos[producto_in_db.codigo]=producto_in_db
    return producto_in_db 