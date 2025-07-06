import reflex as rx
from ..styles.colors import Color
from ..routes import Route
from .protected import *

SIZE_ICON_DEFAULT = 23

def menu_lateral():
    return rx.box(
        menu_lateral_escritorio(),
        overlay_cierre_menu(),
        menu_lateral_movil(),
    )

def menu_lateral_escritorio():
    return rx.box(
        rx.vstack(
            cabecera_menu(),
            rx.cond(
                ProtectedState.es_facultativo,
                rx.cond(
                    ProtectedState.es_admin,
                    items_menu_admin(),
                    items_menu_facultativo(),
                ),
                items_menu_publico(),
            ),
            footer_menu(),
        spacing="0",
        ),
    position="fixed",
    left="0",
    top="0",
    width="340px",
    height="100vh",
    #bg="#1A202C",  # Fondo oscuro
    bg="white",
    #bg="#EFF1F5",
    #bg="#171F26",
    #padding="20px 10px",
    box_shadow="md",
    z_index="1000",
    #overflow_y="auto",
    border_right="2px solid white",
    display=["none", "none", "none", "block"]
    )
    
def menu_lateral_movil():
    return rx.box(
        rx.vstack(
            rx.cond(
                ProtectedState.es_facultativo,
                rx.cond(
                    ProtectedState.es_admin,
                    items_menu_admin(),
                    items_menu_facultativo(),
                ),
                items_menu_publico(),
            ),
            footer_menu(),
        spacing="0",
        ),
    position="fixed",
    left="0",
    top="0",
    width="300px",
    height="100vh",
     #bg="#EFF1F5",
    bg="white",
     #bg="#171F26",
    box_shadow="md",
    z_index="1000",
    #overflow_y="auto",
    border_right="2px solid #599DA2",
    margin_top="60px",
    transition="transform 0.5s ease",
    transform=rx.cond(ProtectedState.menu_lateral_movil_abierto, "translateX(0)", "translateX(-100%)"),
     #display=["none", "block", "block"],
     #display=["none", "none", "none", "block"]
    )

def cabecera_menu() -> rx.Component:
    return rx.hstack(
        rx.hstack(
                rx.image(src="/logo_2.png", width="auto", height="40px"),
                rx.text("Behumanest", font_size="xl", 
                        font_weight="medium", 
                        color="white", size='6'),
            spacing="3",
            align="center",
            margin_bottom="4",
            margin_left="10px",
            ),
            
        rx.spacer(),
        align="center",
        width="100%",
        padding="10px",
        bg=Color.CABECERA.value,
    )
    
def titulo_menu(icono: str, titulo: str, link: str = None, size_icon: int = SIZE_ICON_DEFAULT, offset: str = "0px") -> rx.Component:
    if link and link != "":
        return rx.link(
            rx.hstack(
                rx.icon(icono, font_weight="bold", size=size_icon, margin_top=offset),
                rx.text(titulo, font_weight="bold"), 
            ),
        on_click=lambda: ProtectedState.onclick_menu_lateral(link),
        spacing="3",
        color="black",  # color normal
        text_decoration="none",  # opcional: quita el subrayado
        _hover={"color": "blue",},
        )
    else:
        return rx.hstack(
            rx.icon(icono, font_weight="bold", size=size_icon, margin_top=offset),
            rx.text(titulo, font_weight="bold", width="100%",), 
        )


def subtitulo_menu(titulo: str, link: str) -> rx.Component:
    return rx.link(
            rx.text(titulo, font_size="sm"),
        on_click=lambda: ProtectedState.onclick_menu_lateral(link),
        color="black",  # color normal
        text_decoration="none",  # opcional: quita el subrayado
        _hover={"color": "blue",},
        padding_left="35px",
        margin_top="-8px",
        )

def area_privada_sin_loguear():
    return titulo_menu(icono="lock-keyhole", titulo="Área privada", link=Route.LOGIN.value) 
    
def area_privada_paciente_logueado():
    return rx.fragment(
        titulo_menu(icono="lock-keyhole-open", titulo="Área privada"),  
        subtitulo_menu(titulo="Contactos comunicaciones", link=Route.PACIENTE.value),
        subtitulo_menu(titulo="Cerrar sesión", link="cerrar_sesion"),
    )

def area_privada_facultativo_logueado():
    return rx.fragment(
        titulo_menu(icono="lock-keyhole-open", size_icon=23, titulo="Área privada",link=Route.FACULTATIVO.value),  
        subtitulo_menu(titulo="Cerrar sesión", link="cerrar_sesion"),
    )
        

def items_menu_publico() -> rx.Component:
    return rx.box(
        rx.vstack(
            titulo_menu(icono="home", titulo="Inicio", link=Route.INDEX.value),
            titulo_menu(icono="stethoscope", titulo="En consulta"),
            subtitulo_menu(titulo="Ubicación", link=Route.UBICACION_CONSULTA.value),
            subtitulo_menu(titulo="¿Qué vamos a hacer?", link=Route.QUE_VAMOS_A_HACER.value),
            subtitulo_menu(titulo="Consentimientos", link=Route.CONSENTIMIENTOS.value),
            subtitulo_menu(titulo="Proyecto Behumanest", link=Route.PROYECTO_BEHUMANEST.value),
            titulo_menu(icono="notebook-text", titulo="Indicaciones preoperatorio"),
            subtitulo_menu(titulo="Generales", link=Route.INDICACIONES_GENERALES.value),
            #subtitulo_menu(titulo="Específicas", link=Route.CONSTRUCCION.value),
            titulo_menu(icono="hospital", titulo="Ingreso"),
            subtitulo_menu(titulo="Comunicación telefónica", link=Route.COMUNICACION_INGRESO.value),
            subtitulo_menu(titulo="Ubicación", link=Route.UBICACION_ACCESO_INGRESO.value),
            subtitulo_menu(titulo="¿Qué debo llevar?", link=Route.QUE_LLEVAR_INGRESO.value),     
            subtitulo_menu(titulo="Preparación", link=Route.PREPARACION_PREVIA.value),
            titulo_menu(icono="activity", titulo="Día de la intervención"),
            subtitulo_menu(titulo="En la planta", link=Route.EN_PLANTA.value),
            subtitulo_menu(titulo="Traslado a quirófano", link=Route.TRASLADO_QUIROFANO.value),     
            titulo_menu(icono="info", titulo="Información para las familias"),
            subtitulo_menu(titulo="Ubicaciones de espera", link=Route.UBICACION_ESPERA.value),
            subtitulo_menu(titulo="Comunicación Behumanest", link=Route.COMUNICACION_BEHUMANEST.value),    
            titulo_menu(icono="phone", titulo="Teléfonos de intéres", link=Route.TELEFONOS_INTERES.value), 
            titulo_menu(icono="globe-lock", titulo="Política de Privacidad", link=Route.POLITICA_PRIVACIDAD.value), 
            titulo_menu(icono="message-circle", titulo="Aviso Legal", link=Route.AVISO_LEGAL.value),     
            rx.cond(
                ProtectedState.token_validado & ProtectedState.es_paciente,
                area_privada_paciente_logueado(), 
            ),    
            rx.cond(
                ProtectedState.token_validado & ProtectedState.es_facultativo,
                area_privada_facultativo_logueado(),
            ), 
            rx.cond(
                ProtectedState.token_validado == False,
                area_privada_sin_loguear(),
            ), 
        align="start",
        spacing="3",
        padding="20px",
        margin_bottom="60px",
        width="100%",
        ),
    overflow_y="auto",
    height="calc(100vh - 110px)", 
    )
    
def items_menu_facultativo() -> rx.Component:
    return rx.box(
        rx.vstack(
            titulo_menu(icono="send-horizontal",  titulo="Comunicar cambio de estado", link=Route.FACULTATIVO.value),
            titulo_menu(icono="settings", titulo="Gestión", size_icon=34, offset="-6px"),
            subtitulo_menu(titulo="Pacientes", link=Route.GESTION_PACIENTES.value),
            titulo_menu(icono="lock-keyhole-open",  titulo="Cerrar sesión", link="cerrar_sesion"),     
        align="start",
        spacing="3",
        padding="20px",
        width="100%",
        margin_bottom="60px",
        ),
    overflow_y="auto",
    height="calc(100vh - 110px)", 
    )    
    
def items_menu_admin() -> rx.Component:
    return rx.box(
        rx.vstack(
            titulo_menu(icono="send-horizontal", titulo="Comunicar cambio de estado", link=Route.FACULTATIVO.value),
            titulo_menu(icono="settings", titulo="Gestión", size_icon=34, offset="-6px"),
            subtitulo_menu(titulo="Facultativos", link=Route.GESTION_FACULTATIVOS.value),
            subtitulo_menu(titulo="Pacientes", link=Route.GESTION_PACIENTES.value),
            subtitulo_menu(titulo="Estados del paciente", link=Route.ESTADOS_PACIENTES.value),
            titulo_menu(icono="lock-keyhole-open", titulo="Cerrar sesión", link="cerrar_sesion"),     
        align="start",
        spacing="3",
        padding="20px",
        width="100%",
        margin_bottom="60px",
        ),
    overflow_y="auto",
    height="calc(100vh - 110px)", 
    )      
    
def footer_menu() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(src="/SALUD.png", width="auto", height="30px"),  # Asegurate de tener el logo en assets/
            rx.vstack(
                rx.text("© 2025 Behumanest. Proyecto piloto", size="1", fc="", color="gray.800",),
                rx.text("de humanización al paciente.", size="1", margin_top="-5px", color="gray.800",),
            spacing="1",
            ),
        spacing="3",
        align="center",
        ),
    #position="fixed",
    #bottom="0",
    width="100%",
    bg="gray.100",
    #padding="1em",
    box_shadow="md",
    #z_index="100",
    margin_left="20px",
    margin_top="10px",
    #height="30px",
    )

def overlay_cierre_menu():
    return rx.cond(
        ProtectedState.menu_lateral_movil_abierto,
        rx.box(
            on_click=lambda: ProtectedState.set_menu_lateral_movil_abierto(False),
            position="fixed",
            top="60px",
            left="0",
            width="100vw",
            height="100vh",
            bg="rgba(0, 0, 0, 0.0)",  # transparente
            z_index="999",  # justo debajo del menú
        ),
    )