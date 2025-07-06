import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles



@rx.page(route=Route.INDICACIONES_GENERALES.value, title="Indicaciones Generales")
def indicaciones_generales() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Indicaciones preoperatorias", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "INDICACIONES GENERALES", 
                                size="7",
                                text_align="center",
                            ),
                            rx.text.quote(
                                "Se deberán seguir las indicaciones dadas por el anestesiólogo en la consulta, excepto que vía telefónica se comuniquen otras instrucciones previo a la cirugía.",
                                font_weight="bold",
                                text_decoration="underline",
                                line_height="30px",
                                text_align="center",
                            ),
                            rx.image(
                                "/preoperatorio_1.png",
                                width=["50%", "50%", "38%", "38%"],
                            ),
                        align="center",
                        spacing=styles.Spacing.DEFAULT.value,
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Se aconseja seguir las",
                                rx.text.strong(" siguientes pautas:",),
                                margin_top="20px",
                            ),
                            rx.list.unordered(
                                rx.list_item(
                                    "Mantener una ", 
                                    rx.text.strong("vida activa."),
                                ),
                                rx.list_item(
                                    "Procurar un ", 
                                    rx.text.strong("buen estado físico y psíquico",)
                                    ,margin_top="8px",
                                ),
                                rx.list_item(
                                    "Mantener un ", 
                                    rx.text.strong("correcto estado nutricional.",),
                                    margin_top="8px",
                                ),
                                rx.list_item(
                                    "Realizar un control estricto de la ", 
                                    rx.text.strong("tensión arterial y de los niveles de azúcar en sangre.",),
                                    margin_top="8px",
                                ),
                                rx.list_item(
                                    rx.text.strong("Abandonar", ), 
                                    " el consumo de ", 
                                    rx.text.strong("tabaco y de otras sustancias nocivas.",),
                                    margin_top="8px",
                                ),
                            padding_left=["5px", "5px", "5px", "40px"],
                            ),
                                rx.text(
                                    "En caso de percibir ", 
                                    rx.text.strong("cualquier deterioro en su estado de salud"), 
                                    " deberá acudir a su ", 
                                    rx.text.strong("médico de atención primaria"), 
                                    " quien, en caso necesario, se pondrá en contacto con su ", 
                                    rx.text.strong("cardiólogo."),
                                    text_align="justify",
                                ),
                                rx.text(
                                    "Asimismo, si en los días previos a la intervención quirúrgica presenta ", 
                                    rx.text.strong("síntomas de resfriado"), 
                                    " u otros problemas de salud, deberá ", 
                                    rx.text.strong("comunicarlo al Servicio de Cirugía Cardiovascular"), 
                                    " a través de la", 
                                    rx.text.strong(" extensión 141573."),
                                    text_align="justify",
                                ), 
                        align="start",
                        spacing=styles.Spacing.DEFAULT.value,
                        width="100%",                   
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


