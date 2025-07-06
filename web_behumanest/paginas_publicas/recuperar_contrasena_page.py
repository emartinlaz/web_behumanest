import reflex as rx
from ..routes import Route
from ..componentes.protected import *
from ..componentes.modales import *
from ..componentes.funciones import * 
from ..db import crud
from ..styles import styles
from ..componentes.cabecera import cabecera
from ..componentes.mensajes import *
from ..componentes.menu_lateral import menu_lateral
import os

debug = True


class RecuperarContraseñaState(ProtectedState):
    usuario: str = ""
    email: str = ""
    telefono: str = ""
    error_message: str = ""
    via_contacto: str = "Email"

    
    def init_pagina(self):
        self.reset_campos()
        return rx.set_focus("usuario") 
        
    def set_usuario(self, value: str):
        self.usuario = value

    def set_email(self, value: str):
        self.email = value    

    def set_telefono(self, value: str):
        self.telefono = value  
        
    def set_via_contacto(self, value: str):
        self.email = ""
        self.telefono = ""
        self.via_contacto = value    
        return [
            rx.set_value("email", ""),
            rx.set_value("telefono", ""),
        ]

    def reset_campos(self):
        self.error_message = "" 
        self.telefono = ""
        self.usuario = ""
        self.via_contacto = "Email"

    def onclick_recuperar_contraseña(self):
        self.error_message = ""
        if len(self.usuario) == 0 or self.usuario == "":
            self.error_message = "El usuario no puede estar vacio" 
            return rx.set_focus("usuario")     
        if self.via_contacto == "Email":             
            if not is_valid_email(self.email, permitir_nulo=False):
                self.error_message = "Debe introducir un email válido" 
                return rx.set_focus("email")  
        else:          
            if not is_valid_telefono(self.telefono, permitir_nulo=False):
                self.error_message = "Debe introducir un teléfono válido" 
                return rx.set_focus("telefono")  
        contraseña = get_nueva_contraseña(longitud=6) 
        #Comprobacion de si es facultativo
        facultativo = crud.get_facultativo_by_usuario(usuario=self.usuario)
        actualizar_bd_contraseña_facultativo = False   
        if facultativo and facultativo.activo:
            #El usuario es un facultativo -> verificaccion del contacto seleccionado
            mensaje_a_enviar_email = get_mensaje_email_reenvio_contraseña(contraseña=contraseña)
            mensaje_a_enviar_sms = get_mensaje_sms_reenvio_contraseña(contraseña=contraseña)
            if self.via_contacto == "Email": 
                if facultativo.usuario == self.email:
                    actualizar_bd_contraseña_facultativo = True
                    if ENVIAR_MENSAJES: 
                        enviar_email(
                            destinatario=self.email,
                            asunto="Acceso a Behumanest",
                            mensaje_a_enviar=mensaje_a_enviar_email
                            )
                    else:
                        print(contraseña)
            else:
                if facultativo.telefono == self.telefono:
                    actualizar_bd_contraseña_facultativo = True
                    if ENVIAR_MENSAJES: 
                        enviar_sms(
                            destinatario=self.telefono,
                            mensaje_a_enviar=mensaje_a_enviar_sms,                
                        )    
                    else:
                        print(contraseña)
        #Comprobacion de si es paciente
        paciente = crud.get_paciente_by_usuario(usuario=self.usuario)
        actualizar_bd_contraseña_paciente = False
        if paciente and paciente.activo:
            #El usuario es un paciente -> verificaccion del contacto seleccionado
            mensaje_a_enviar_email = get_mensaje_email_reenvio_contraseña(contraseña=contraseña)
            mensaje_a_enviar_sms = get_mensaje_sms_reenvio_contraseña(contraseña=contraseña)
            if self.via_contacto == "Email": 
                if paciente.email_paciente == self.email:
                    actualizar_bd_contraseña_paciente = True
                    if ENVIAR_MENSAJES: 
                        enviar_email(
                            destinatario=self.email,
                            asunto="Acceso a Behumanest",
                            mensaje_a_enviar=mensaje_a_enviar_email
                            )
                    else:
                        print(contraseña)
            else:
                if paciente.telefono_paciente == self.telefono:
                    actualizar_bd_contraseña_paciente = True
                    if ENVIAR_MENSAJES: 
                        enviar_sms(
                            destinatario=self.telefono,
                            mensaje_a_enviar=mensaje_a_enviar_sms,                
                        )    
                    else:
                        print(contraseña)
        if actualizar_bd_contraseña_facultativo:
            crud.update_contraseña_facultativo_by_id(
                id_facultativo=facultativo.id_facultativo, 
                contraseña=contraseña,
                cambiar_contraseña=True)            
        if actualizar_bd_contraseña_paciente:
            crud.update_contraseña_paciente_by_id(
                id_paciente=paciente.id_paciente, 
                contraseña=contraseña,
                cambiar_contraseña=True)
        if actualizar_bd_contraseña_facultativo or actualizar_bd_contraseña_paciente:
            return ModalState.abrir_modal_info(titulo="Confirmación de envío", 
                                               mensaje_1="La contraseña ha sido enviada.", 
                                               mensaje_2="Al pulsar \"Cerrar\" será redirigido a la página de inicio de sesión.",
                                               origen="recuperar_contraseña",)
        else:
            self.error_message = "No hay existe ningún usuario con los datos introducidos" 
            return [
                    rx.set_value("usuario", ""),
                    rx.set_value("email", ""),
                    rx.set_value("telefono", ""),
                    rx.set_focus("usuario"),
                ]           
        
    


@rx.page(route=Route.RECUPERAR_CONTRASEÑA.value, title="Recuperar contraseña", on_load=RecuperarContraseñaState.init_pagina)
def login_usuario() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        #modal_info(),
        rx.vstack(
            cabecera(titulo="Recuperar contraseña", mostrar_link_area_privada=False),
            rx.card(
                rx.vstack(                
                    rx.image(
                        src="/SALUD.png",
                        #width="2.5em",
                        width="40%",
                        height="auto",
                        #   border_radius="25%",
                    ),
                    rx.cond(
                        RecuperarContraseñaState.error_message != "",
                        rx.callout(
                            RecuperarContraseñaState.error_message,
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                            width="100%",
                        ), 
                    ),
                    rx.vstack(
                        rx.text(
                            "Usuario",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            id="usuario",
                            name="usuario",
                            placeholder="Introduzca el usuario",
                            #type="email",
                            size="3",
                            width="100%",
                            on_change=RecuperarContraseñaState.set_usuario,
                            autocomplete="new-password",
                        ),
                        rx.vstack(
                            rx.radio(
                                ["Email", "Teléfono"],
                                default_value="Email",
                                on_change=RecuperarContraseñaState.set_via_contacto,
                                direction="row",
                                spacing="5",
                            ),
                        align="center",
                        width="100%",
                        margin_top="20px",
                        ),
                        rx.cond(
                            RecuperarContraseñaState.via_contacto == "Email",
                            contacto_email(),
                            contacto_telefono(),
                        ),
                        rx.vstack(
                            rx.button(
                                "Recuperar contraseña", 
                                size="4", 
                                width="100%",
                                #type="sumit",
                                margin_top="20px",
                                on_click=RecuperarContraseñaState.onclick_recuperar_contraseña,
                            ),
                            rx.link(
                                rx.text("Inicio sesión", size='2'),
                                href=Route.LOGIN.value,
                                is_external=False,
                                margin_top="10px",
                            ),
                        align="center",
                        width="100%",
                        ),
                    modales_recuperar_contraseña(),
                    spacing="1",  
                    align="start",
                    width="100%",
                    ),   
                align="center",
                spacing=styles.Spacing.LARGE.value,
                padding="20px", 
                width="100%",
                ),
            width="100%",
            max_width="480px",
            border_width="2px",
            border_color=styles.Color.BORDER_CARD.value,
            border_radius="14px",  
            margin_x="10px",
            ),
        width="100%",
        padding_left=["10px", "10px", "10px", "360px"],
        padding_right=["10px", "10px", "10px", "20px"],
        padding_top=["90px", "90px", "90px", "100px",],
        align="center",
        spacing="0",
        ),
    width="100%",
    align="center",
    spacing="0",
    )

def contacto_email()-> rx.Component:
    return rx.fragment(
        rx.text(
            "Email",
            size="3",
            weight="medium",
            text_align="left",
            margin_top="10px",
        ),
        rx.input(
            id="email",
            name="email",
            placeholder="Introduzca el email del usuario",
            size="3",
            width="100%",
            on_change=RecuperarContraseñaState.set_email,
            autocomplete="new-password",
        ),
    )

def contacto_telefono()-> rx.Component:
    return rx.fragment(
        rx.text(
            "Teléfono",
            size="3",
            weight="medium",
            text_align="left",
            margin_top="10px",
        ),
        rx.input(
            id="telefono",
            name="telefono",
            placeholder="Introduzca el teléfono del usuario",
            size="3",
            width="100%",
            on_change=RecuperarContraseñaState.set_telefono,
            autocomplete="new-password",
        ),
    )

