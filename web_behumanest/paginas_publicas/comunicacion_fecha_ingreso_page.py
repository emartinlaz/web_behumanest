import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles



@rx.page(route=Route.COMUNICACION_INGRESO.value, title="Ingreso")
def comunicacion_fecha_ingreso() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Ingreso", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "COMUNICACIÓN TELEFÓNICA FECHA INGRESO", 
                                size="7",
                                text_align="center",
                                padding_x=["10px", "10px", "10px", "40px"],
                            ),
                            rx.image(
                                "/aviso_fecha.png",
                                width=["80%", "80%", "50%", "50%"],
                            ),
                        align="center", 
                        width="100%",
                        ),
                        rx.vstack(
                            rx.list.unordered(
                                rx.list_item(
                                    "La ", 
                                    rx.text.strong("comunicación",), 
                                    " con el paciente se realizará ", 
                                    rx.text.strong("mediante llamada telefónica."),
                                    margin_top="20px",
                                    text_align="justify",
                                ),
                                rx.list_item(
                                    "El contacto se efectuará utilizando los ", 
                                    rx.text.strong("números de teléfono registrados en su historia clínica.",),
                                    margin_top="9px",
                                    text_align="justify",
                                ),
                                rx.list_item(
                                    "En caso de querer actualizar o modificar algún número de contacto, deberá gestisonarlo a través de ", 
                                    rx.text.strong("Citaciones,",),
                                    " o del ",
                                    rx.text.strong("Servicio de Atención al Paciente.",),
                                    margin_top="9px",
                                    text_align="justify",
                                ),
                                rx.list_item(
                                    "Tenga en cuenta que el número de teléfono utilizado para la llamada puede ", 
                                    rx.text.strong("no coincidir"), 
                                    " con el facilitado para esta aplicación.",
                                    margin_top="9px",
                                    text_align="justify",
                                ),
                                rx.list_item(
                                    "Habitualmente, la llamada se realiza ", 
                                    rx.text.strong("varios días antes de la intervención quirúrgica.",),
                                    margin_top="9px",
                                    text_align="justify",
                                ),
                                rx.list_item(
                                    "Durante la misma, se le informará del ", 
                                    rx.text.strong("día, la hora y el lugar de ingreso"), 
                                    " así como de las ", 
                                    rx.text.strong("indicaciones finales relativas a la medicación."),
                                    margin_top="9px",
                                    text_align="justify",
                                ),
                            ),
                        padding_x=["10px", "10px", "10px", "80px"],
                        align="start",
                        width="100%",
                        ),
                    align="center",
                    spacing=styles.Spacing.DEFAULT.value,
                    #padding_x=["10px", "10px", "10px", "80px"],
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


