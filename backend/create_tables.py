# backend/create_tables.py

from app.db import Base, engine
from app.models import MotoDB

print("Creando tablas...")
Base.metadata.create_all(bind=engine)
print("¡Listo!")
