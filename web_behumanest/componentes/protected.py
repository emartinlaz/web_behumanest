from datetime import timedelta
import reflex as rx
from ..db.models import Facultativos, Pacientes
from .funciones import *
from ..db import crud
from ..routes import Route
from typing import Optional
import os


ENVIAR_MENSAJES = os.getenv("ENVIAR_MENSAJES", "true").lower() == "true"
GUARDAR_LOGS = os.getenv("GUARDAR_LOGS", "true").lower() == "true"

debug = False
DEFAULT_AUTH_SESSION_EXPIRATION_DELTA = timedelta(days=1)



class ProtectedState(rx.State):
    #Variables de sesion
    token_validado: bool = False
    facultativo_logueado: Optional[Facultativos] = None
    es_facultativo: bool = False
    paciente_logueado: Optional[Pacientes] = None
    es_paciente: bool = False
    es_admin: bool = False
    es_super_admin: bool = False
    #Variables control globales
    menu_lateral_movil_abierto: bool = False
    

    def set_menu_lateral_movil_abierto(self, abierto: bool):
        self.menu_lateral_movil_abierto = abierto           
    
    def reset_sesion(self):
        self.token_validado = False
        self.es_admin = False
        self.es_super_admin = False
        self.es_facultativo = False
        self.es_paciente = False
        self.facultativo_logueado = None
        self.paciente_logueado = None
    
    def _login(self, token: str, id_facultativo: int = None, id_paciente: int = None, expiration_delta: timedelta = DEFAULT_AUTH_SESSION_EXPIRATION_DELTA):
        self.reset_sesion()
        self.token_validado = True
        #Anaizamos si es facultativo
        if id_facultativo:
            facultativo = crud.get_facultativo_by_id_facultativo(id_facultativo=id_facultativo)
            if facultativo:
                self.facultativo_logueado = facultativo
                self.es_facultativo = True
                if facultativo.admin: self.es_admin = True
                if facultativo.super_admin: self.es_super_admin = True
        #Anaizamos si es paciente
        elif id_paciente:
            paciente = crud.get_paciente_by_id_paciente(id_paciente=id_paciente)
            if paciente:
                self.paciente_logueado = paciente
                self.es_paciente = True
        #self.do_logout(save_log=False) #Borrar todos registros que contengan ese token 
        crud.create_sesion(token=token, id_facultativo=id_facultativo, id_paciente=id_paciente, expiration_delta=expiration_delta)
        
    def do_logout(self):
        crud.delete_sesion_by_token(token=self.router.session.client_token)
        self.reset_sesion()
        return rx.redirect(Route.LOGIN.value)
    
    def redir_paciente(self): 
        if not (self.token_validado and self.es_paciente):
            self.do_logout()
            return rx.redirect(Route.LOGIN.value)

    def redir_facultativo(self): #  -> rx.event.EventSpec | None:
        if not (self.token_validado and self.es_facultativo):
            self.do_logout()
            return rx.redirect(Route.LOGIN.value)
        
    def redir_admin(self):
        if self.token_validado and self.es_facultativo and self.es_admin: 
            return None
        else:
            #self.do_logout()
            #return rx.redirect(Route.LOGIN.value)
            if debug: print(f"No tienes permisos de administrador")
            return rx.redirect(Route.FACULTATIVO.value)
    
    def comprobar_sesion_caducada(self):
        expirados = crud.deleted_expired()
        #Buscar si el token esta en la tabla
        sesion = crud.get_sesion_by_token(token=self.router.session.client_token)
        if not sesion: self.reset_sesion()
        
    #MARK: FUNCIONES MENU LATERAL
    
    def onclick_menu_lateral(self, value):
        if value=="cerrar_sesion":
            self.do_logout()
            value=Route.LOGIN.value
        self.menu_lateral_movil_abierto = False
        return rx.redirect(value)
    
    def toggle_menu_lateral(self):
        self.menu_lateral_movil_abierto = not self.menu_lateral_movil_abierto
    
    
    
def paciente_requerido(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    def protected_page_paciente():
        return rx.fragment(
            rx.cond(
                ProtectedState.token_validado & ProtectedState.es_paciente, 
                page(),
                rx.center(
                    rx.spinner(on_mount=ProtectedState.redir_paciente, margin_top="250px", size="3")
                ),
            ),
        )
    protected_page_paciente.__name__ = page.__name__
    return protected_page_paciente

def facultativo_requerido(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    def protected_page_facultativo():
        return rx.fragment(
            rx.cond(
                ProtectedState.token_validado & ProtectedState.es_facultativo, 
                page(),
                rx.center(
                    rx.spinner(on_mount=ProtectedState.redir_facultativo, margin_top="250px", size="3")
                ),
            ),
        )
    protected_page_facultativo.__name__ = page.__name__
    return protected_page_facultativo

def admin_requerido(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:
    def protected_page_admin():
        return rx.fragment(
            rx.cond(
                ProtectedState.token_validado & ProtectedState.es_facultativo & ProtectedState.es_admin,
                page(),
                rx.center(
                    rx.spinner(on_mount=ProtectedState.redir_admin, margin_top="250px", size="3")
                ),
            )
        )
    protected_page_admin.__name__ = page.__name__
    return protected_page_admin

