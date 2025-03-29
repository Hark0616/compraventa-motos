# app/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Moto, MotoDB, Compra, CompraDB, Persona, PersonaDB, Venta, VentaDB


router = APIRouter()

# Base de datos temporal en memoria (lista)
motos_db = []

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/motos")
def registrar_moto(moto: Moto, db: Session = Depends(get_db)):
    moto_nueva = MotoDB(
        placa=moto.placa,
        modelo=moto.modelo,
        color=moto.color,
        ciudad_procedencia=moto.ciudad_procedencia,
        chasis=moto.chasis,
        motor=moto.motor,
        tiene_soat=moto.tiene_soat,
        soat_vencimiento=moto.soat_vencimiento,
        tiene_tecnomecanica=moto.tiene_tecnomecanica,
        tecno_vencimiento=moto.tecno_vencimiento,
        tiene_multas=moto.tiene_multas,
        valor_multas=moto.valor_multas,
    )
    db.add(moto_nueva)
    db.commit()
    db.refresh(moto_nueva)
    return {"message": "Moto guardada en Supabase correctamente", "moto": moto.placa}

@router.post("/compras")
def registrar_compra(compra: Compra, db: Session = Depends(get_db)):
    # Buscar persona por cédula
    persona_existente = db.query(PersonaDB).filter_by(cedula=compra.vendedor.cedula).first()

    # Si no existe, la creamos
    if not persona_existente:
        persona_nueva = PersonaDB(
            nombre=compra.vendedor.nombre,
            cedula=compra.vendedor.cedula,
            telefono=compra.vendedor.telefono
        )
        db.add(persona_nueva)
        db.commit()
        db.refresh(persona_nueva)
        persona_id = persona_nueva.id
    else:
        persona_id = persona_existente.id

    # Buscar moto por placa
    moto = db.query(MotoDB).filter_by(placa=compra.moto_placa).first()
    if not moto:
        return {"error": "Moto no encontrada"}

    # Registrar la compra
    nueva_compra = CompraDB(
        moto_id=moto.id,
        vendedor_id=persona_id,
        fecha_compra=compra.fecha_compra,
        valor_compra=compra.valor_compra
    )

    db.add(nueva_compra)
    db.commit()
    db.refresh(nueva_compra)

    return {"message": "Compra registrada exitosamente", "compra_id": nueva_compra.id}

@router.post("/ventas")
def registrar_venta(venta: Venta, db: Session = Depends(get_db)):
    # Buscar persona por cédula
    persona_existente = db.query(PersonaDB).filter_by(cedula=venta.comprador.cedula).first()

    if not persona_existente:
        persona_nueva = PersonaDB(
            nombre=venta.comprador.nombre,
            cedula=venta.comprador.cedula,
            telefono=venta.comprador.telefono
        )
        db.add(persona_nueva)
        db.commit()
        db.refresh(persona_nueva)
        persona_id = persona_nueva.id
    else:
        persona_id = persona_existente.id

    # Buscar moto por placa
    moto = db.query(MotoDB).filter_by(placa=venta.moto_placa).first()
    if not moto:
        return {"error": "Moto no encontrada"}

    # Registrar la venta
    nueva_venta = VentaDB(
        moto_id=moto.id,
        comprador_id=persona_id,
        fecha_venta=venta.fecha_venta,
        valor_venta=venta.valor_venta,
        destrate=venta.destrate
    )

    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)

    return {"message": "Venta registrada exitosamente", "venta_id": nueva_venta.id}

