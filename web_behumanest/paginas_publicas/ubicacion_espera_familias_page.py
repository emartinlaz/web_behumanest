import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.UBICACION_ESPERA.value, title="Información para las familias")
def ubicacion_espera_familias() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Información para las familias", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "UBICACIÓN DE ESPERA PARA LAS FAMILIAS", 
                                size="7",
                                text_align="center",
                            ),
                            rx.image(
                                "/sala_espera.png",
                                margin_top="10px",
                                width=["100%", "100%", "80%", "80%"],
                            ),
                        align="center",
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Los familiares esperarán a recibir información, cuando ", 
                                rx.text.strong("finalice la cirugía"), 
                                " y el paciente haya sido trasladado a la ", 
                                rx.text.strong("Unidad de Cuidados Intensivos"), 
                                " en las Salas de Espera destinadas para ello, en la ", 
                                rx.text.strong("planta primera del edifico de Traumatología del Hospital Universitario Miguel Servet."),
                                text_align="justify",
                            ),
                        align="start",
                        width="100%",                  
                        ),
                        rx.vstack(
                            rx.text(
                                "Acceso Traumatología", 
                                font_weight="bold",
                                text_decoration="underline", 
                                text_align="center",
                            ),
                            rx.image(
                                "/acceso_trauma.png", 
                                border_radius="14px",
                            ),
                            rx.text(
                                "Unidad de Cuidados Intensivos", 
                                font_weight="bold",
                                text_decoration="underline", 
                                text_align="center",
                                margin_top="20px",
                            ),
                            rx.image(
                                "/unidad_ci.png", 
                                border_radius="14px",
                            ),
                            rx.text(
                                "Sala Espera Unidad de Cuidados Intensivos", 
                                font_weight="bold",
                                text_decoration="underline", 
                                text_align="center",
                                margin_top="20px",
                            ),
                            rx.image(
                                "/sala_espera_uci.png", 
                                border_radius="14px",
                            ),
                        spacing=styles.Spacing.DEFAULT.value,
                        align="center",
                        width="100%",
                        ),
                    width="100%",
                    spacing=styles.Spacing.BIG.value,
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"], 
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


