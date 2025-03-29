# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TU URL de conexión: obténla desde Supabase > Project > Settings > Database
DATABASE_URL = "postgresql://postgres:To5FzXQKC34ftKep@db.ysipbncafcwmgmynvmmg.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
