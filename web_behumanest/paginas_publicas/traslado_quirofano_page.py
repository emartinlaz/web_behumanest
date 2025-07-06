import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.TRASLADO_QUIROFANO.value, title="Día de la intervención")
def traslado_quirofano() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Día de la intervención", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "TRASLADO A QUIRÓFANO", 
                                size="7",
                                text_align="center",
                            ),
                            rx.image(
                                "/traslado_quirofano.png",
                                width=["100%", "100%", "70%", "70%"],
                                border_radius="14px",
                            ),
                        align="center",
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Será trasladado por un celador al ", rx.text.strong("área de quirófanos"), " donde será recibido por el personal de quirófano.",
                                text_align="justify",
                            ),
                        align="start",
                        width="100%",   
                        padding_y="10px",                
                        ),
                        rx.vstack(
                            rx.text(
                                "Acceso Área Quirófanos", 
                                font_weight="bold",
                                text_decoration="underline", 
                                text_align="center",
                            ),
                            rx.image(
                                "/acceso_quirofanos.png", 
                                border_radius="14px",
                            ),
                        align="center",
                        width="100%", 
                        ),
                        rx.vstack(
                            rx.text(
                                "Inicialmente el celador le trasladará a la ", rx.text.strong("Acogida (dentro del bloque quirúrgico).",),
                                text_align="justify",
                            ),
                            rx.text(
                                "Aquí se presentará el personal de ", rx.text.strong("enfermería y auxiliares"), " le realizarán una serie de preguntas para completar un listado de verificación de seguridad quirúrgica y se le canalizará una vía venosa en el brazo, en caso de que no lleve niguna o no sea del calibre adecuado. ",
                                text_align="justify",
                            ),
                            rx.text(
                                "Por dicha vía se administrará ", rx.text.strong("antibiótico para prevenir infecciones"), " y cualquier otra medicación que necesite para estar más tranquilo o entrar en mejores condiciones a quirófano. ",
                                text_align="justify",
                            ),
                            rx.text(
                                "Posteriormente y tras comprobar que ", rx.text.strong("todo es correcto"), ", conocerá a la enfermera resposable de la perfusión durante la cirugía y al anestesiólogo responsable de su quirófano. ",
                                text_align="justify",
                            ),
                        align="start",
                        width="100%",    
                        margin_top="10px", 
                        ),
                    align="center",
                    spacing=styles.Spacing.DEFAULT.value,
                    width="100%",
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


