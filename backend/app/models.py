# app/models.py

from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy import Column, String, Integer, Boolean, Date, Float, ForeignKey
from app.db import Base

class MotoDB(Base):
    __tablename__ = "motos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, index=True, nullable=False)
    modelo = Column(Integer)
    color = Column(String)
    ciudad_procedencia = Column(String)
    chasis = Column(String)
    motor = Column(String)
    tiene_soat = Column(Boolean)
    soat_vencimiento = Column(Date, nullable=True)
    tiene_tecnomecanica = Column(Boolean)
    tecno_vencimiento = Column(Date, nullable=True)
    tiene_multas = Column(Boolean)
    valor_multas = Column(Float, nullable=True)



class Persona(BaseModel):
    nombre: str
    cedula: str
    telefono: str


class Moto(BaseModel):
    placa: str
    modelo: int
    color: str
    ciudad_procedencia: str
    chasis: str
    motor: str
    tiene_soat: bool
    soat_vencimiento: Optional[date]
    tiene_tecnomecanica: bool
    tecno_vencimiento: Optional[date]
    tiene_multas: bool
    valor_multas: Optional[float]


class Compra(BaseModel):
    moto_placa: str
    vendedor: Persona
    fecha_compra: date
    valor_compra: float


class Venta(BaseModel):
    moto_placa: str
    comprador: Persona
    fecha_venta: date
    valor_venta: float
    destrate: bool

class PersonaDB(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    cedula = Column(String, unique=True, nullable=False)
    telefono = Column(String, unique=True, nullable=False)

class CompraDB(Base):
    __tablename__ = "compras"

    id = Column(Integer, primary_key=True, index=True)
    moto_id = Column(Integer, ForeignKey("motos.id"))
    vendedor_id = Column(Integer, ForeignKey("personas.id"))
    fecha_compra = Column(Date, nullable=False)
    valor_compra = Column(Float, nullable=False)

class VentaDB(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    moto_id = Column(Integer, ForeignKey("motos.id"), nullable=False)
    comprador_id = Column(Integer, ForeignKey("personas.id"), nullable=False)
    fecha_venta = Column(Date, nullable=False)
    valor_venta = Column(Float, nullable=False)
    destrate = Column(Boolean, nullable=False)
