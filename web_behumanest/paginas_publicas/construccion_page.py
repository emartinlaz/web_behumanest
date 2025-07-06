import reflex as rx
from ..routes import Route
from ..db import crud
from ..styles import styles
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral




@rx.page(route=Route.CONSTRUCCION.value, title="En construcción")
def index() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo=" ", mostrar_link_area_privada=True),
            rx.vstack(
                rx.image(
                    "/construccion_1.jpg",
                    width="900px",   
               ),
            align="center",
            ),          
        width="100%",
        padding_left=["5px", "5px", "5px", "360px"],
        padding_right=["5px", "5px", "5px", "20px"],
        padding_top=["70px", "70px", "70px", "100px"], 
        padding_bottom=["30px", "30px", "30px", "0px"],
        align="center",
        spacing="0",
        ),
    width="100%",
    align="center",
    spacing="0",
    ),


