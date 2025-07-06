import reflex as rx
from typing import Optional
from sqlmodel import Column, Field, func, JSON
from datetime import datetime
from passlib.context import CryptContext
import json
from datetime import date

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

#MARK: FACULTATIVOS

class Facultativos(rx.Model, table=True):
    __tablename__ = "facultativos"

    id_facultativo: int = Field(primary_key=True, index=True, nullable=False)
    usuario: str = Field(primary_key=False, nullable=False)
    password_hash: str = Field(primary_key=False, nullable=False)
    nombre: str = Field(primary_key=False, nullable=False)
    apellidos: str = Field(primary_key=False, nullable=False)
    telefono: Optional[str] = Field(primary_key=False, nullable=True)
    admin: bool = Field(primary_key=False, nullable=False)
    activo: bool = Field(primary_key=False, nullable=False)
    fecha_alta: date = Field(primary_key=False, nullable=False)
    fecha_baja: Optional[date] = Field(primary_key=False, nullable=True)
    cambiar_contraseña: bool = Field(primary_key=False, nullable=False)
    eliminado: bool = Field(primary_key=False, nullable=False)
    admin: bool = Field(primary_key=False, nullable=False)
    super_admin: bool = Field(primary_key=False, nullable=False)
    
    # Funciones de hash de contraseña
    @staticmethod
    def hash_password(secret: str) -> str:
        return pwd_context.hash(secret)
    
    def check_password(self, secret: str) -> bool:
        try:
            return pwd_context.verify(
                secret,
                self.password_hash,
            )
        except:
            print("Error formato de contraseña")
            return False


#MARK: PACIENTES

class Pacientes(rx.Model, table=True):
    __tablename__ = "pacientes"

    id_paciente: int = Field(primary_key=True, index=True, nullable=False)
    usuario: str = Field(primary_key=False, nullable=False)
    password_hash: str = Field(primary_key=False, nullable=False)
    nombre: str = Field(primary_key=False, nullable=False)
    apellidos: str = Field(primary_key=False, nullable=False)
    estado_actual: Optional[int] = Field(primary_key=False, nullable=True)
    activo: bool = Field(primary_key=False, nullable=False)
    fecha_alta: date = Field(primary_key=False, nullable=False)
    fecha_baja: Optional[date] = Field(primary_key=False, nullable=True)
    cambiar_contraseña: bool = Field(primary_key=False, nullable=False)
    email_paciente: Optional[str] = Field(primary_key=False, nullable=True)
    telefono_paciente: Optional[str] = Field(primary_key=False, nullable=True)
    email_contacto: Optional[str] = Field(primary_key=False, nullable=True)
    telefono_contacto: Optional[str] = Field(primary_key=False, nullable=True)
    envios_pruebas: int = Field(primary_key=False, nullable=False)
    contacto_valido: bool = Field(primary_key=False, nullable=False)
    eliminado: bool = Field(primary_key=False, nullable=False)
    
    # Funciones de hash de contraseña
    @staticmethod
    def hash_password(secret: str) -> str:
        return pwd_context.hash(secret)
    
    def check_password(self, secret: str) -> bool:
        return pwd_context.verify(
            secret,
            self.password_hash,
        )

   
#MARK: ESTADOS PACIENTE

class EstadosPaciente(rx.Model, table=True):
    __tablename__ = "estados_paciente"

    id_estado: int = Field(primary_key=True, index=True, nullable=False)
    descripcion_estado: str = Field(primary_key=False, nullable=False)
    orden: int = Field(primary_key=False, nullable=False)
   
#MARK: SESIONES_ACTIVAS

class SesionesActivas(rx.Model, table=True):
    __tablename__ = "sesiones_activas"

    token: str = Field(primary_key=True, nullable=False)
    id_facultativo: Optional[int] = Field(primary_key=False, nullable=True)
    id_paciente: Optional[int] = Field(primary_key=False, nullable=True)
    conexion: datetime = Field(default_factory=lambda: datetime.now(), nullable=False)
    expiration: datetime = Field(nullable=False)
    
