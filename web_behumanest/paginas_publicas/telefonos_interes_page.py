import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.TELEFONOS_INTERES.value, title="Teléfonos de interés")
def telefonos_interes() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Teléfonos de interés", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading("TELÉFONOS DE INTERÉS", size="7",padding_y=["5px", "5px", "5px", "10px"],),
                            rx.image("/telefonos_interes.png",padding_x=["10px", "10px", "10px", "40px"],width="100%",),
                        align="center",
                        spacing=styles.Spacing.DEFAULT.value,
                        padding_x=["10px", "10px", "10px", "20px"], 
                        width="100%",
                        ),
                    width="100%",
                    padding="20px", 
                    ),
                width="100%",
                max_width="900px",
                border_width="2px",
                border_color=styles.Color.BORDER_CARD.value,
                border_radius="14px",  
                margin_x="10px",        
                ),    
            align="center",
            spacing=styles.Spacing.LARGE.value,
            padding="20px", 
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


