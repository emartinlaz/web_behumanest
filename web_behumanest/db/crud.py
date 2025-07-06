from .models import *
from .conexion import connect
from sqlmodel import Session, select, func
from sqlalchemy import desc
from datetime import datetime, timedelta, date
import json
from typing import List

max_envios_pruebas = 3
debug = False
        
        
    
#MARK: SESION

def deleted_expired():
    with Session(connect()) as session:
        try:
            query = select(SesionesActivas).where(SesionesActivas.expiration < datetime.now())
            expirados = session.exec(query).all()
            for expirado in expirados:
                if debug: print(f"Expiration: {expirado.token}")
                session.delete(expirado)
                session.commit()
            return expirados
        except:
            print('Fallo al eliminar sesiones expiradas')  
            return None   

def get_sesion_by_token(token: str):
    with Session(connect()) as session:
        query = select(SesionesActivas).where(
                SesionesActivas.token == token,
                SesionesActivas.expiration  > datetime.now()
            )
        sesion = session.exec(query).first()
        return sesion

def create_sesion(token: str, id_facultativo: int = None, id_paciente: int = None, expiration_delta: timedelta = datetime.now()):
    with Session(connect()) as session:
        try:
            conexion = datetime.now()
            expiration = conexion + expiration_delta
            nueva_sesion = SesionesActivas(
                token=token,
                id_facultativo=id_facultativo,
                id_paciente=id_paciente,
                conexion=conexion,
                expiration=expiration
            )
            session.merge(nueva_sesion)
            session.commit()
        except Exception as e:
            print("Error: create_sesion ", e)

def delete_sesion_by_token(token):
    with Session(connect()) as session:
        query = select(SesionesActivas).where(SesionesActivas.token == token)
        sesiones = session.exec(query).all()
        for sesion in sesiones:
            session.delete(sesion)
        session.commit()
            
#MARK: FACTULTATIVOS

def get_facultativo_by_id_facultativo(id_facultativo: int) -> Facultativos:
    with Session(connect()) as session:
        try: 
            query = select(Facultativos).where(Facultativos.id_facultativo == id_facultativo)
            result = session.exec(query).first()
        except:
            if debug: print('Fallo en sql get_facultativo_by_id_facultativo')
            result = None
        return result
    
def get_facultativo_by_usuario(usuario: str) -> Facultativos:
    with Session(connect()) as session:        
        try:
            query = select(Facultativos).where(Facultativos.usuario == usuario)
            result = session.exec(query).first()
        except:
            if debug: print('Fallo en sql get_facultativo_by_usuario')
            result = None
        return result
    
def create_facultativo(usuario: str, 
                       password: str, 
                       nombre: str, 
                       apellidos: str, 
                       telefono: str, 
                       activo: bool = True, 
                       cambiar_contraseña: bool = True,
                       eliminado: bool = False,
                       admin: bool = False, 
                       super_admin: bool = False, 
                       ):
    with Session(connect()) as session:
        try:
            nuevo_facultativo = Facultativos(
                usuario=usuario,
                password_hash=Facultativos.hash_password(password),
                nombre=nombre,
                apellidos=apellidos,
                telefono=telefono,
                activo=activo,
                fecha_alta=date.today(),
                cambiar_contraseña=cambiar_contraseña,
                eliminado=eliminado,
                admin=admin,
                super_admin=super_admin,
            )
            session.add(nuevo_facultativo)
            session.commit()
            session.refresh(nuevo_facultativo)
            if debug: print(f"Facultativo creado con ID: {nuevo_facultativo.id_facultativo}")
            return nuevo_facultativo.id_facultativo
        except Exception as e:
            print("Error: create_facultativo ", e)
            return 0

def get_facultativo_by_activo(activo: bool, eliminado: bool = False, super_admin: bool = False) -> Facultativos:
    with Session(connect()) as session:  
        try:
            query = select(Facultativos).where((Facultativos.activo==activo) & (Facultativos.eliminado==eliminado) & (Facultativos.super_admin==super_admin)).order_by(desc(Facultativos.id_facultativo))
            result = session.exec(query).all()
        except:
            result =None
            print("No existen facultativos activos")
        return result
    
def update_facultativo_by_id(id_facultativo: int, 
                             usuario: str, 
                             nombre: str, 
                             apellidos: str, 
                             telefono: str = "",
                             ):
    with Session(connect()) as session:
        try:
            query = select(Facultativos).where(Facultativos.id_facultativo == id_facultativo)
            facultativo = session.exec(query).one_or_none()
            if facultativo is None: return False
            facultativo.nombre = nombre
            facultativo.apellidos = apellidos
            facultativo.usuario = usuario
            if telefono != "": facultativo.telefono = telefono
            session.commit()
            return True
        except:
            print('Fallo al actualizar facultativo')
            return False

def update_activo_facultativo_by_id(id_facultativo: int, 
                                    activo: bool, 
                                    fecha_alta: date = None, 
                                    fecha_baja: date = None, 
                                    borrar_fecha_baja:bool = False
                                    ):
    with Session(connect()) as session:
        try:
            query = select(Facultativos).where(Facultativos.id_facultativo == id_facultativo)
            facultativo = session.exec(query).one_or_none()
            if facultativo is None: return False
            facultativo.activo = activo
            if fecha_alta: facultativo.fecha_alta = fecha_alta
            if borrar_fecha_baja: 
                facultativo.fecha_baja = None
            elif fecha_baja: facultativo.fecha_baja = fecha_baja
            session.commit()
            return True        
        except:
            print('Fallo al actualizar facultativo')
            return False         

def update_contraseña_facultativo_by_id(id_facultativo: int, contraseña: str, cambiar_contraseña: bool):
    with Session(connect()) as session:
        try:
            query = select(Facultativos).where(Facultativos.id_facultativo == id_facultativo)
            facultativo = session.exec(query).one_or_none()
            if not facultativo: return False
            facultativo.password_hash=Facultativos.hash_password(contraseña)
            facultativo.cambiar_contraseña=cambiar_contraseña
            session.commit()
            return True        
        except:
            print('Fallo al actualizar contraseña facultativo')
            return False        

def update_eliminar_facultativo_by_id(id_facultativo: str, eliminado: bool):
    with Session(connect()) as session:
        try:
            query = select(Facultativos).where(Facultativos.id_facultativo == id_facultativo)
            facultativo = session.exec(query).first()
            if not facultativo: return False         
            facultativo.eliminado=eliminado
            session.commit()
            return True
        except:
            print('Fallo al update eliminar')
            return False
            
def delete_facultativo_by_id(id_facultativo: str):
    with Session(connect()) as session:
        try:
            query = select(Facultativos).where(Facultativos.id_facultativo == id_facultativo)
            facultativo = session.exec(query).first()
            session.delete(facultativo)
            session.commit()
        except:
            print('Fallo al eliminar facultativo') 



#MARK: PACIENTES

def get_paciente_by_id_paciente(id_paciente: int) -> Pacientes:
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            result = session.exec(query).first()
        except:
            print('Fallo en sql get_paciente_by_id_paciente')
            result = None
        return result
    
def get_paciente_by_usuario(usuario: str) -> Pacientes:
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.usuario == usuario)
            result = session.exec(query).first()
        except:
            print('Fallo en sql get_paciente_by_usuario')
            result = None
        return result

def get_pacientes_by_activo(activo: bool, eliminado: bool = False) -> Pacientes:
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where((Pacientes.activo==activo) & (Pacientes.eliminado==eliminado)).order_by(desc(Pacientes.id_paciente))
            result = session.exec(query).all()
        except:
            result =None
            print("No existen pacientes activos")
        return result

def get_paciente_by(usuario: str, activo: bool = True) -> Facultativos:
    with Session(connect()) as session:           
        try:
            query = select(Pacientes).where((Pacientes.usuario==usuario) & (Pacientes.activo==activo))
            result = session.exec(query).all()
        except:
            result =None
            print("No existen pacientes activos")
        return result

def create_paciente(usuario: str, 
                    password: str, 
                    nombre: str, 
                    apellidos: str, 
                    activo: bool = True, 
                    cambiar_contraseña: bool = True,
                    email_paciente: str = None,
                    telefono_paciente: str = None,
                    email_contacto: str = None,
                    telefono_contacto: str = None,
                    envios_pruebas: str = max_envios_pruebas,
                    contacto_valido: bool = False,
                    eliminado: bool = False,
                    ):
    with Session(connect()) as session:
        try:
            nuevo_paciente = Pacientes(
                usuario=usuario,
                password_hash=Pacientes.hash_password(password),
                nombre=nombre,
                apellidos=apellidos,
                estado_actual=None,
                activo=activo,
                fecha_alta=date.today(),
                fecha_baja=None,
                cambiar_contraseña=cambiar_contraseña,
                email_paciente=email_paciente,
                telefono_paciente=telefono_paciente,
                email_contacto=email_contacto,
                telefono_contacto=telefono_contacto,
                envios_pruebas=envios_pruebas,
                contacto_valido=contacto_valido,
                eliminado=eliminado,
            )
            session.add(nuevo_paciente)
            session.commit()
            session.refresh(nuevo_paciente)
            if debug: print(f"Paciente creado con ID: {nuevo_paciente.id_paciente}")
            return nuevo_paciente.id_paciente
        except Exception as e:
            print("Error: create_paciente ", e)
            return 0
 

def update_contraseña_paciente_by_id(id_paciente: int, contraseña: str, cambiar_contraseña: bool):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            paciente.password_hash=Pacientes.hash_password(contraseña)
            paciente.cambiar_contraseña=cambiar_contraseña
            session.commit()
            return True        
        except:
            if debug: print('Fallo al actualizar contraseña paciente')
            return False  

def update_paciente_by_id(id_paciente: int, 
                          usuario: str, 
                          nombre: str, 
                          apellidos: str,
                          email_paciente: str = "",
                          telefono_paciente: str = "",
                          email_contacto: str = "",
                          telefono_contacto: str = "",
                          ):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            paciente.usuario = usuario
            paciente.nombre = nombre
            paciente.apellidos = apellidos
            if email_paciente != "": paciente.email_paciente = email_paciente
            if telefono_paciente != "": paciente.telefono_paciente = telefono_paciente
            if email_contacto != "": paciente.email_contacto = email_contacto
            if telefono_contacto != "": paciente.telefono_contacto = telefono_contacto
            session.commit()
            return True
        except:
            if debug: print('Fallo al actualizar paciente')
            return False
      
def update_activo_paciente_by_id(
        id_paciente: int, 
        activo: bool, 
        fecha_alta: date = None, 
        fecha_baja: date = None, 
        borrar_fecha_baja:bool = False
    ):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            paciente.activo = activo
            if fecha_alta: paciente.fecha_alta = fecha_alta
            if borrar_fecha_baja: 
                paciente.fecha_baja = None
            elif fecha_baja: paciente.fecha_baja = fecha_baja
            session.commit()
            return True        
        except:
            if debug: print('Fallo al actualizar paciente')
            return False 

def update_estado_actual_paciente_by_id(id_paciente: int, estado_actual: int):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            paciente.estado_actual = estado_actual
            session.commit()
            return True        
        except:
            if debug: print('Fallo al actualizar estado paciente')
            return False      

def update_envios_pruebas_by_id(id_paciente: int, variacion: int = 0, total_envios: int = -1):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            if total_envios >= 0:
                envios_pruebas_restantes = total_envios
            else:
                envios_pruebas_restantes = paciente.envios_pruebas + variacion
                if envios_pruebas_restantes < 0: envios_pruebas_restantes = 0
            paciente.envios_pruebas = envios_pruebas_restantes
            session.commit()
            return paciente.envios_pruebas        
        except:
            if debug: print('Fallo al actualizar envios pruebas paciente')
            return None  

def update_datos_contacto_paciente_by_id(id_paciente: int, 
                                         email_contacto: str = "",
                                         telefono_contacto: str = "",
                                         contacto_valido: bool = False,
                                        ):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            if email_contacto != "": paciente.email_contacto=email_contacto
            if telefono_contacto != "": paciente.telefono_contacto=telefono_contacto
            paciente.contacto_valido = contacto_valido
            session.commit()
            return True        
        except:
            if debug: print('Fallo al actualizar estado datos de contacto')
            return False      

def update_contacto_valido_paciente_by_id(id_paciente: int, contacto_valido: bool):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).one_or_none()
            if paciente is None: return False
            paciente.contacto_valido = contacto_valido
            session.commit()
            return True        
        except:
            if debug: print('Fallo al actualizar contacto_valido')
            return False  

def update_eliminar_paciente_by_id(id_paciente: str, eliminado: bool):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).first()
            if not paciente: return False         
            paciente.eliminado=eliminado
            session.commit()
            return True
        except:
            print('Fallo al update eliminar paciente')
            return False

def delete_paciente_by_id(id_paciente: str):
    with Session(connect()) as session:
        try:
            query = select(Pacientes).where(Pacientes.id_paciente == id_paciente)
            paciente = session.exec(query).first()
            session.delete(paciente)
            session.commit()
        except:
            print('Fallo al eliminar paciente') 

#MARK: ESTADOS PACIENTES

def get_estados_paciente() -> EstadosPaciente:
    with Session(connect()) as session:
        try:
            query = select(EstadosPaciente).order_by(EstadosPaciente.orden)
            estados_pacientes = session.exec(query).all()
            return estados_pacientes
        except:
            if debug: print('Fallo en sql get_estados_paciente')
            return None

def get_estado_paciente_by_id_estado(id_estado: int) -> EstadosPaciente:
    with Session(connect()) as session:
        try:
            query = select(EstadosPaciente).where(EstadosPaciente.id_estado == id_estado)
            estado_paciente = session.exec(query).first()
            return estado_paciente
        except:
            if debug: print('Fallo en sql get_estados_paciente_by_id')
            return None
        
def get_estado_paciente_by_orden(orden: int) -> EstadosPaciente:
    with Session(connect()) as session:
        try:
            query = select(EstadosPaciente).where(EstadosPaciente.orden == orden)
            estado_paciente = session.exec(query).first()
            return estado_paciente
        except:
            if debug: print('Fallo en sql get_estados_paciente_by_orden')
            return None

def get_estado_paciente_by_descripcion(descripcion: str) -> EstadosPaciente:
    with Session(connect()) as session:
        try:
            query = select(EstadosPaciente).where(EstadosPaciente.descripcion_estado == descripcion)
            estado_paciente = session.exec(query).first()
            return estado_paciente
        except:
            if debug: print('Fallo en sql get_estados_paciente_by_descripcion')
            return None

def update_estado_paciente_by_id(id_estado: int, 
                                 descripcion: str = "", 
                                 orden: int = ""
                                 ):
    with Session(connect()) as session:
        try:
            query = select(EstadosPaciente).where(EstadosPaciente.id_estado == id_estado)
            estado = session.exec(query).one_or_none()
            if estado is None: return False
            if descripcion != "": estado.descripcion_estado = descripcion
            if orden != "": estado.orden = orden
            session.commit()
            return True
        except:
            if debug: print('Fallo al actualizar estado paciente')
            return False

def delete_estado_pacientes_by_id(id_estado: int):
    with Session(connect()) as session:
        try:
            query = select(EstadosPaciente).where(EstadosPaciente.id_estado == id_estado)
            estado = session.exec(query).first()
            if estado:
                session.delete(estado)
                session.commit()
                estados = session.exec(select(EstadosPaciente).order_by(EstadosPaciente.orden)).all()
                for idx, estado in enumerate(estados, start=1):
                    estado.orden = idx
                    session.add(estado) 
                session.commit()
                return True
        except:
            if debug: print('Fallo al eliminar sesiones expiradas') 
            return False

def create_estado(descripcion: str):
    with Session(connect()) as session:
        try:
            resultado  = session.exec(func.max(EstadosPaciente.orden)).one()
            ultimo_orden = (resultado[0] or 0) + 1 
        except:
            if debug: print('Fallo al orden') 
            return False
        try:
            nuevo_estado = EstadosPaciente(
                descripcion_estado=descripcion,
                orden=ultimo_orden
            )
            session.add(nuevo_estado)
            session.commit()
            session.refresh(nuevo_estado)
            return nuevo_estado.id_estado
        except Exception as e:
            print("Error: create_estado ", e)
            return 0

       
