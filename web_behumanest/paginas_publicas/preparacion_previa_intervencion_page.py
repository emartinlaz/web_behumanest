import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.PREPARACION_PREVIA.value, title="Ingreso")
def preparacion_previa() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Ingreso", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "PREPARACIÓN PREVIA A LA INTERVENCIÓN",
                            text_align="center",
                        ),
                        rx.image(
                            "/preparar_intervencion.png",
                            align="center",
                            width="80%",    
                            border_radius="14px",
                            margin_top=["0px", "0px", "0px", "10px"],
                        ),
                        rx.vstack(
                            rx.text("A su llegada, será recibido por el ", rx.text.strong("equipo de enfermería y cirugía cardiovascular.:",), padding_top="15px",),
                            rx.text("Durante este proceso:"),
                        align="start",
                        #spacing=styles.Spacing.DEFAULT.value,
                        padding_x=["10px", "10px", "10px", "20px"], 
                        width="100%",   
                        padding_y="10px",
                        ),
                        rx.list.unordered(
                            rx.list_item(
                                "Se le realizará una ",
                                rx.text.strong("extracción de sangre"),
                                " para analítica.",
                                text_align="justify",
                            ),
                            rx.list_item(
                                rx.text("Se procederá al ",
                                rx.text.strong("reajuste de su medicación"),
                                " habitual si fuera necesario.",),
                                margin_top="10px",
                                text_align="justify",
                            ),
                            rx.list_item(
                                "Se le explicará ",
                                rx.text.strong("con mayor detalle"),
                                " el procedimiento quirúrgico y se resolverán todas las ", rx.text.strong("dudas"), " que pueda tener.",
                                margin_top="10px",
                                text_align="justify",
                            ),
                            rx.list_item(
                                "Se le entregará una ",
                                rx.text.strong("tabla con las instrucciones del protocolo de ayuno,",),
                                " que deberá seguir rigurosamente.",
                                margin_top="10px",
                                text_align="justify",
                            ),
                            rx.list_item(
                                "Se le proporcionará un ",
                                rx.text.strong("jabón desinfectante",),
                                " para ducharse la noche anterior y la mañana de la intervención, incluyendo el ",
                                rx.text.strong("cuero cabelludo"),
                                " y poniendo especial atención en",
                                rx.text.strong(" ingles, axilas y zona púbica."),
                                margin_top="10px",
                                text_align="justify",
                            ),
                            rx.list_item(
                                "También se le facilitará un ",
                                rx.text.strong("colutorio",),
                                " para realizar enjuagues bucales previos a la cirugía.",
                                margin_top="10px",
                                text_align="justify",
                            ),
                        ),
                    align="center",
                    width="100%",
                    spacing=styles.Spacing.DEFAULT.value,
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"],
                    ),
                    rx.vstack(
                        rx.image(
                        "/ayuno.png",
                        align="center",
                        width="80%",         
                        ),                          
                    align="center",
                    width="100%", 
                    margin_top="10px",   
                    ),
                    rx.vstack(
                        rx.text(rx.text.strong("Importante:",),),
                        rx.text(
                            "Existe la posibilidad de que la intervención pueda ser ",
                            rx.text.strong("cancelada",),
                            " debido a la ",
                            rx.text.strong("atención urgente a otros pacientes pacientes o por falta de disponibilidad de camas en la UCI y/o de personal asistencial."),
                            " En tal caso, se le informará oportunamente y se intentará ",
                            rx.text.strong("reprogramar "),
                            " la cirugía ",
                            rx.text.strong("lo antes posible."),
                            margin_top="10px",
                            text_align="justify",      
                        ),                   
                    align="start",
                    width="100%",
                    spacing=styles.Spacing.DEFAULT.value,
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"], 
                    margin_top="10px"  
                    ),
                width="100%",
                max_width="900px",
                border_width="2px",
                border_color=styles.Color.BORDER_CARD.value,
                border_radius="14px",     
                ),     
            align="center",
            spacing=styles.Spacing.MEDIUM_BIG.value,
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
    
    
