import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.UBICACION_ACCESO_INGRESO.value, title="Ingreso")
def ubicacion_acceso_ingreso() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Ingreso", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "UBICACIÓN DE ACCESO PARA EL INGRESO", 
                            size="7",
                            text_align="center",
                            ),
                        rx.image(
                            "/ubicacion_acceso.png",
                            width=["100%", "100%", "80%", "80%"],
                            border_radius="14px",
                        ),
                    align="center",
                    spacing=styles.Spacing.LARGE.value,
                    width="100%",
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"],
                    ),
                    rx.vstack(
                        rx.text(
                            "El día del ingreso, en primer lugar se deberá acudir a  ", 
                            rx.text.strong("Admisión."),
                            #text_align="justify",
                        ),
                        rx.text(
                            rx.list_item("De lunes a viernes a partir de las 8 a.m, ", rx.text.strong("planta Baja del Hospital General"),),
                            rx.list_item("Fines de semana y festivos o antes de las 8 a.m, ", rx.text.strong("Urgencias de la planta -1 (entrando por el Hospital de Traumatología)."),),
                        ),
                        rx.text("Posteriormente, deberá acceder a las instalaciones del ", rx.text.strong("Servcio de Cirugía Cardiovascular Planta 5 del Hospital Miguel Servet"),),
                    align="start",
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"], 
                    ),
                    rx.vstack(  
                         rx.text("Acceso Servicio Cirugía", 
                                font_weight="bold",
                                text_decoration="underline", ),
                        rx.image(
                            "/acceso_cirugia1.png", 
                            border_radius="14px", 
                             width=["100%", "100%", "80%", "80%"],
                        ), 
                        rx.image(
                            "/acceso_cirugia2.png", 
                            border_radius="14px", 
                             width=["100%", "100%", "80%", "80%"],
                        ), 
                    align="center",
                    #spacing=styles.Spacing.LARGE.value,
                    #width="100%",
                    #padding_x=["10px", "10px", "10px", "80px"],
                    #padding_y=["10px", "10px", "10px", "20px"], 
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


