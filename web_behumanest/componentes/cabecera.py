import reflex as rx
from ..styles.colors import Color
from ..routes import Route
from .protected import *
from .modales import *


def link_facultativo():
    return rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.hstack(
                    rx.text(
                        ProtectedState.facultativo_logueado.nombre, 
                    color="white", 
                    size="5",
                    margin_top="8px",
                    cursor="pointer",
                    ),
                    rx.image(
                        src="/user_white.png",
                    width="40px",
                    title="Usuario",
                    cursor="pointer",
                    ),
                ),
            ),
            rx.menu.content(
                menu_usuario_facultativo(),
            padding="10px",
            ),
        ),
    )         

def link_paciente():
    return rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.hstack(
                    rx.text(
                        ProtectedState.paciente_logueado.usuario, 
                    color="white", 
                    size="5",
                    margin_top="8px",
                    cursor="pointer",
                    ),
                    rx.image(
                        src="/user_white.png",
                    width="40px",
                    title="Usuario",
                    cursor="pointer",
                    ),
                ),
            ),
            rx.menu.content(
                menu_usuario_paciente(),
            padding="10px",
            ),
        ),
    )

def link_usuario_logueado():
    return rx.fragment(
        rx.cond(
            ProtectedState.es_facultativo,
            link_facultativo(),
        ),
        rx.cond(
            ProtectedState.es_paciente,
            link_paciente(),
        ),     
    )
    
def link_area_privada():
    return rx.link(
        rx.hstack(
            rx.icon("lock-keyhole", color="white", font_weight="bold"),
            rx.text("Área privada", color="white", font_weight="bold", size="5"),
        spacing="2",
        
        ),
    margin_top="8px",
    href=Route.LOGIN.value,
    )

def mostrar_area_usuario():
    return rx.cond(
        #menu_usuario != None,
        ProtectedState.token_validado,
        #Si esta usuario logueado
        link_usuario_logueado(),      
        #No esta usuario logueado
        link_area_privada(),
    )

def cabecera(titulo: str, mostrar_link_area_privada: bool = True) -> rx.Component:
    return rx.box(
        #rx.vstack(
            rx.hstack(
                rx.image(
                    src="/menu_1.png",
                    width="40px",
                    margin_top="1px",
                    title="Menu",
                    cursor="pointer",
                    display=["flex", "flex", "flex", "none"],
                    on_click=ProtectedState.toggle_menu_lateral,
                ),
                rx.text(
                    titulo,
                size="6",
                font_weight="medium",
                style={"color": "white"},
                margin_top="6px",
                display=["none", "none", "none", "block"],
                ),
                rx.spacer(),
                # Derecha: Area privada
                rx.cond(
                    mostrar_link_area_privada,
                    mostrar_area_usuario(),
                ),      
            width="100%",
            #align="center",
            #justify="between",
            padding_left=["20px", "20px", "20px", "240px"],         # Espacio a izquierda y derecha
            padding_right=["30px", "30px", "30px", "300px"],        # Espacio a izquierda y derecha
            #padding_y="10px",
            margin_top="8px",
            ),
        #justify="center",
        #align="center",
        #width="100%",
        #margin_top="10px",
        ##padding_right="100px",
        #),
    background_color=Color.CABECERA.value,
    position="fixed",
    top="0px",
    z_index="5",
    height="60px",
    width="100%",
    ),

def menu_usuario_facultativo() -> rx.Component:
    from ..paginas_privadas.facultativo_page import FacultativoState
    return rx.fragment(
        rx.menu.item(
            rx.text("Comunicar estados", size="5", weight="regular"),
            on_click=rx.redirect(Route.FACULTATIVO.value),
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ), 
        rx.menu.item(
            rx.text("Mi cuenta", size="5", weight="regular"),
            on_click=rx.redirect(Route.FACULTATIVO.value),
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ), 
        rx.menu.item(
            rx.text("Cambio contraseña", size="5", weight="regular"),
            on_click=ModalState.abrir_modal_cambio_contraseña(origen="cabecera"),
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ),   
        rx.menu.separator(margin_top="10px",),
        rx.menu.item(
            rx.text("Cerrar sesión", size="5", weight="regular"),
            on_click=ProtectedState.do_logout,
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ),    
    )

def menu_usuario_paciente() -> rx.Component:
    from ..paginas_privadas.paciente_page import PacienteState
    return rx.fragment(
        rx.menu.item(
            rx.text("Contactos comunicaciones", size="5", weight="regular"),
            on_click=rx.redirect(Route.PACIENTE.value),
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ),   
        rx.menu.item(
            rx.text("Mi cuenta", size="5", weight="regular"),
            on_click=rx.redirect(Route.PACIENTE.value),
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ),  
        rx.menu.item(
            rx.text("Cambio contraseña", size="5", weight="regular"),
            on_click=ModalState.abrir_modal_cambio_contraseña(origen="cabecera"),
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ),   
        rx.menu.separator(margin_top="10px",),
        rx.menu.item(
            rx.text("Cerrar sesión", size="5", weight="regular"),
            on_click=ProtectedState.do_logout,
            #margin_left="-10px",
            _hover={"background-color": "transparent ", "color":"blue"}
        ),    
    )


