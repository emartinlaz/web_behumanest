import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles


class IndexState(rx.State):
    @rx.event
    def init_pagina(self):
        pass


@rx.page(route=Route.INDEX.value, title="BeHumanest", on_load=IndexState.init_pagina)
def index() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Inicio", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "PROYECTO PILOTO", 
                            size="7",
                            text_align="center",
                        ),
                        rx.text(
                            rx.text.strong("BeHumanest"),
                            " nace con el objetivo de facilitar " ,
                            rx.text.strong("recursos prácticos"),
                            " que sean de utilidad al " ,
                            rx.text.strong("paciente"),
                            ", ofreciendo información en un " ,
                            rx.text.strong("lenguaje claro"), 
                            " y de manera accesible.",
                            text_align="justify",
                            size="4",       
                        ),
                        rx.text(
                            "Además, se pretende brindar ",
                            rx.text.strong("apoyo emocional"),
                            " a los ",
                            rx.text.strong("familiares"), 
                            " que acompañen al paciente en determinados procedimientos quirúrgicos.",
                            text_align="justify",
                            size="4",       
                        ),
                        rx.image(
                            "/mundo_sanitario2.png",
                            border_radius="14px",
                        ),
                        rx.text(
                            "La creación de esta aplicación combinando ",
                            rx.text.strong("empatía y tecnología"), 
                            " ayuda a que el proceso quirúrgico esté también enfocado en el ",
                            rx.text.strong("bienestar"), 
                            " integral del ",
                            rx.text.strong("paciente"),
                            " y su entorno ",
                            rx.text.strong("familiar."),
                            text_align="justify",
                            size="4",
                        ),
                        rx.text(
                            "Se ha considerado su ",
                            rx.text.strong("aplicación"),
                            " únicamente en pacientes que van a ser sometidos a ",
                            rx.text.strong("intervenciones de cirugía cardiaca con circulación extracorpórea, de forma programada,"),
                            " al tratarse de una cirugía de", rx.text.strong(" larga duración.",),
                            text_align="justify",
                            size="4",
                        ),
                    align="center",
                    spacing=styles.Spacing.DEFAULT.value,
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"], 
                    width="100%",
                    ),
                width="100%",
                max_width="900px",
                border_width="2px",
                border_color=styles.Color.BORDER_CARD.value,
                border_radius="14px",           
                ),    
            align="center",
            spacing=styles.Spacing.LARGE.value,
            width="100%",            
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



