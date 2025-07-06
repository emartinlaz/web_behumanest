import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.EN_PLANTA.value, title="Día de la intervención")
def en_planta() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Día de la intervención", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "EN LA PLANTA", 
                                size="7",
                                text_align="center",
                            ),
                            rx.image(
                                "/en_planta.png",
                                width="80%",
                                padding_x=["10px", "10px", "10px", "80px"],
                            ),
                        align="center",
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text("El día de la intervención, se llevarán a cabo las siguientes ", rx.text.strong("pautas:"),),
                            rx.list.unordered(
                                rx.list_item("Le despertarán a las ", rx.text.strong("7:30h."), margin_top="8px",),
                                rx.list_item("Le tomarán las ", rx.text.strong("constantes."),  margin_top="8px",),
                                rx.list_item("Si todo es correcto, le porporcionarán un ", rx.text.strong("jabón desinfectante"), " para ducharse antes de la intervención (incluyendo ", rx.text.strong("cuero cabelludo e insistiendo en ingles, axilas y zona púbica"),").", margin_top="8px",),
                                rx.list_item("También se le facilitará un ", rx.text.strong("colutorio")," para hacer enjuages. ", margin_top="8px",),
                            width="100%",
                            ),
                        align="start",
                        width="100%",   
                        padding_y="10px",                
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


