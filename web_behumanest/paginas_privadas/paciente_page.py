import reflex as rx
from ..db import crud
from ..routes import Route
from ..componentes.protected import *
from ..componentes.modales import *
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..componentes.mensajes import *
from ..componentes.funciones import *
from ..styles import styles

debug = False


class PacienteState(ProtectedState):
    error_mensaje_validacion_contactos: str = ""
    error_mensaje_validacion_cuenta: str = ""
    mensaje_informacion_modal_contactos: str = ""
    mensaje_informacion_modal_contactos_2: str = ""
    mensaje_informacion_modal_cuenta: str = "Prueba 2"
    enviar_email: bool = False
    email_contacto: str = ""
    enviar_telefono: bool = False
    telefono_contacto: str = ""
    guardar_cambios: bool = False
    mostrar_boton_prueba_comunicacion: bool = False

    
    def iniciar_pagina(self): #  -> rx.event.EventSpec | None:
        if not self.paciente_logueado: return
        self.email_contacto = ""
        self.telefono_contacto = ""
        self.error_mensaje_validacion_contactos = ""
        self.error_mensaje_validacion_cuenta = ""
        self.enviar_email = False
        self.enviar_telefono = False
        self.guardar_cambios = False
        self.load_info_contactos()
        self.load_datos_contacto()
        if self.paciente_logueado and self.paciente_logueado.cambiar_contraseña:
            return ModalState.abrir_modal_cambio_contraseña_inicial  #Obliga a cambiar la contraseña la primera vezz que entra

    def load_datos_contacto(self):
        if not self.paciente_logueado: return
        self.email_contacto = opcionalstr_to_str(self.paciente_logueado.email_contacto)
        self.telefono_contacto = opcionalstr_to_str(self.paciente_logueado.telefono_contacto)
        self.enviar_email = False
        self.enviar_telefono = False
        if self.email_contacto != "": self.enviar_email = True
        if self.telefono_contacto != "": self.enviar_telefono = True
    
    def load_info_contactos(self):
        self.mensaje_informacion_modal_contactos: str = "Los datos de contacto introducidos en este apartado, será la persona o personas que recibirán las comunicaciones durante el proceso quirúrgico, el día de la intervención"
        self.mensaje_informacion_modal_contactos_2: str = "Puede introducir una dirección de correo electrónico para la comunicación por email y/o un télefono móvil para la comunicación por mensaje de texto (SMS)"
        self.error_mensaje_validacion_contactos = ""

    def load_info_guardar(self):
        self.mensaje_informacion_modal_contactos: str = "NOTA: Una vez introducidos los datos de contacto pulse el botón Guardar"
        self.mensaje_informacion_modal_contactos_2: str = ""
        self.error_mensaje_validacion_contactos = ""
    
    def load_info_mensaje_prueba(self):
        self.mensaje_informacion_modal_contactos: str = "NOTA: Para comprobar que los datos introducidos son correctos, puede envíar una comunicación de prueba (máximo 3 comunicaciones de prueba por paciente)"
        self.mensaje_informacion_modal_contactos_2: str = ""
        self.error_mensaje_validacion_contactos = ""

    def set_enviar_email(self, value):
        self.load_info_guardar()
        self.guardar_cambios = True
        self.ocultar_boton_pruebas()
        self.enviar_email = value
        if value == False:
            self.email_contacto = ""
    
    def set_email(self, value):
        self.load_info_guardar()
        self.guardar_cambios = True
        self.ocultar_boton_pruebas()
        self.email_contacto = value

    def set_enviar_telefono(self, value):
        self.load_info_guardar()
        self.guardar_cambios = True
        self.ocultar_boton_pruebas()
        self.enviar_telefono = value
        if value == False:
            self.telefono_contacto = ""

    def set_telefono(self, value):
        self.load_info_guardar()
        self.guardar_cambios = True
        self.ocultar_boton_pruebas()
        self.telefono_contacto = value

    def onclick_guardar(self):
        if not self.paciente_logueado: return
        if self.enviar_email:
            if not is_valid_email(self.email_contacto, permitir_nulo=False):
                self.mensaje_informacion_modal_contactos = ""
                self.mensaje_informacion_modal_contactos_2 = ""
                self.error_mensaje_validacion_contactos = "El email introducido no es correcto, si no quiere comunicar por email desmarque el check" 
                return 
        if self.enviar_telefono:
            if not is_valid_telefono(self.telefono_contacto, permitir_nulo=False):
                self.mensaje_informacion_modal_contactos = ""
                self.mensaje_informacion_modal_contactos_2 = ""
                self.error_mensaje_validacion_contactos = "El teléfono introducido no es correcto, si no quiere comunicar por teléfono desmarque el check"    
                return       
        contacto_valido = False
        if self.email_contacto != "" or self.telefono_contacto:
             contacto_valido = True
        crud.update_datos_contacto_paciente_by_id(
            id_paciente=self.paciente_logueado.id_paciente,
            email_contacto=str_to_opcionalstr(self.email_contacto),
            telefono_contacto=str_to_opcionalstr(self.telefono_contacto),
            contacto_valido=contacto_valido,
        )
        self.guardar_cambios = False
        if (self.enviar_email or self.enviar_telefono) and self.paciente_logueado.envios_pruebas > 0: 
            self.mostrar_boton_pruebas()
            self.load_info_mensaje_prueba()
            return ModalState.abrir_modal_info(titulo="Guardar", mensaje_1="Contactos guardados correctamente.", mensaje_2="Para confirmar que los contactos introducidos son correctos, puede realizar una comunicación de prueba pulsando en 'Enviar comunicación de prueba'")
            
        else:
            self.load_info_contactos()
            return ModalState.abrir_modal_info(titulo="Guardar", mensaje_1="No ha introducido ningún contacto.", mensaje_2="Advertencia: Debe haber registrado al menos un contacto para poder enviar las comunicaciones.")

    def mostrar_boton_pruebas(self):
        self.mostrar_boton_prueba_comunicacion = True
        
    def ocultar_boton_pruebas(self):
        self.mostrar_boton_prueba_comunicacion = False
        


@rx.page(route=Route.PACIENTE.value,title='Pacientes', on_load=PacienteState.iniciar_pagina)
@paciente_requerido
def paciente() -> rx.Component: 
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Área paciente", mostrar_link_area_privada=True),
            ficha_contacto(),
            modales_paciente(),
        width="100%",
        padding_left=["5px", "5px", "5px", "360px"],
        padding_right=["5px", "5px", "5px", "20px"],
        padding_top=["90px", "90px", "90px", "100px",],
        align="center",
        spacing="0",
        ),
    align="center",
    width="100%", 
    spacing="0",
    on_mount=ProtectedState.comprobar_sesion_caducada,
    )


def ficha_contacto() -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.text(f"Contactos para las comunicaciones durante el proceso quirúrgico", 
                    size="6",  
                    margin_y="10px", 
                    weight="medium",
                    align="center",
                    text_align="center",
                    ),
                rx.vstack(
                    rx.cond(
                        PacienteState.error_mensaje_validacion_contactos != "",
                        rx.callout(
                            rx.text(PacienteState.error_mensaje_validacion_contactos, text_align="justify",),
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                            width="100%",
                        ), 
                    ),
                    rx.cond(
                        PacienteState.mensaje_informacion_modal_contactos != "",
                        rx.callout(
                            rx.text(PacienteState.mensaje_informacion_modal_contactos, text_align="justify",),
                            icon="info",
                            width="100%",
                            size="1",
                            #padding="10px", 
                            margin_top="10px",
                            text_align="justify",
                        ),
                    ),
                    rx.cond(
                        PacienteState.mensaje_informacion_modal_contactos_2 != "",
                        rx.callout(
                            rx.text(PacienteState.mensaje_informacion_modal_contactos_2, text_align="justify",),
                            icon="info",
                            width="100%",
                            size="1",
                            #padding="10px", 
                            margin_top="10px",
                        ),
                    ),
                    rx.box(
                        rx.checkbox(
                            "Acepto el envío de comunicaciones por correo electrónico",
                            default_checked=False,
                            size="3",
                            spacing="2",
                            checked=PacienteState.enviar_email,
                            on_change=PacienteState.set_enviar_email,                                
                        ),
                    margin_top="10px",
                    ),
                    rx.cond(
                        PacienteState.enviar_email,
                        rx.fragment(
                            rx.text(
                                "Email",
                                size="3",
                                weight="medium",
                                text_align="left",
                            ),
                            rx.input(
                                name="email_contacto",
                                id="email_contacto",
                                placeholder="Introduzca el email para comunicaciones",
                                max_length=50,
                                size="3",
                                width="100%",
                                margin_top="-10px",
                                value=PacienteState.email_contacto,
                                on_change=PacienteState.set_email,
                                autocomplete="new-password",
                            ),
                        ),
                    ),
                    rx.box(
                        rx.checkbox(
                            "Acepto el envío de comunicaciones por teléfono (SMS)",
                            default_checked=False,
                            size="3",
                            spacing="2",
                            checked=PacienteState.enviar_telefono,
                            on_change=PacienteState.set_enviar_telefono,                                
                        ),
                    margin_top="10px",
                    ), 
                    rx.cond(
                        PacienteState.enviar_telefono,
                        rx.fragment(
                            rx.text(
                                "Teléfono",
                                size="3",
                                weight="medium",
                                text_align="left",
                            ),
                            rx.input(
                                name="telefono_contacto",
                                id="telefono_contacto",
                                placeholder="Introduzca el telefóno para comunicaciones",
                                max_length=9,
                                size="3",
                                width="100%",
                                margin_top="-10px",
                                value=PacienteState.telefono_contacto,
                                on_change=PacienteState.set_telefono,
                                autocomplete="new-password",
                            ),
                        ),
                    ),
                    rx.cond(
                        PacienteState.guardar_cambios,
                        rx.button(
                            "Guardar", 
                            size="4", 
                            width="100%",
                            type="button",
                            margin_top="30px",
                            on_click=PacienteState.onclick_guardar,
                        ),
                    ),
                    rx.cond(
                        PacienteState.mostrar_boton_prueba_comunicacion & (PacienteState.enviar_email | PacienteState.enviar_telefono),
                        rx.button(
                            "Enviar comunicación de prueba", 
                            size="4", 
                            width="100%",
                            type="button",
                            margin_top="30px",
                            on_click=ModalState.abrir_modal_confirmar_envio_prueba(email=PacienteState.email_contacto,
                                                                                   telefono=PacienteState.telefono_contacto,
                                                                                   origen="confirmar_envio_prueba",)
                        ),
                    ),
                align="start", 
                width="100%",   
                ),
            align="center", 
            padding="20px",
            width="100%",
            ),  
        width="100%",
        max_width="580px",
        border_width="2px",
        border_color=styles.Color.BORDER_CARD.value,
        border_radius="14px",  
        margin_x="5px", 
        )

def ficha_personal() -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.text(f"Datos cuenta Behumanest", 
                    size="6",  
                    margin_y="10px", 
                    weight="medium",
                    align="center",
                    ),
                rx.vstack(
                    rx.cond(
                        PacienteState.error_mensaje_validacion_cuenta != "",
                        rx.callout(
                            PacienteState.error_mensaje_validacion_cuenta,
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                            width="100%",
                        ), 
                    ),
                    rx.cond(
                        PacienteState.mensaje_informacion_modal_cuenta != "",
                        rx.callout(
                            PacienteState.mensaje_informacion_modal_cuenta,
                            icon="info",
                            width="100%",
                            size="1",
                            #padding="10px", 
                            margin_top="10px",
                        ),
                    ),
                align="start", 
                width="100%",   
                ),

            spacing=styles.Spacing.VERY_SMALL.value,
            align="center", 
            padding="20px",
            ),  
        )
