from pydantic import BaseModel

class ProductoIn(BaseModel):
    codigo: int
    nombre: str

class ProductoOut(BaseModel):
    nombre: str
    precio: int
    cantidad: int 