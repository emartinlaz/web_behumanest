import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.INDICACIONES_ESPECIFICAS_EPOETINA.value, title="Indicaciones Generales")
def indicaciones_especificas_epoetina() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Indicaciones específicas", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "INDICACIONES ESPECÍFICAS", 
                                size="7",
                                text_align="center",
                            ),
                            rx.text.quote(
                                "Se deberán seguir estas indicaciones siempre y cuando se indique. No siempre será necesario.",
                                font_weight="bold",
                                text_decoration="underline",
                                line_height="30px",
                                text_align="center",
                            ),
                            rx.image(
                                "/indicaciones_especificas_2.png",
                                width=["80%", "80%", "50%", "50%"],
                            ),
                            rx.text(
                                "Tratamiento con Epoetina Alfa", 
                                font_weight="bold",
                                text_decoration="underline", 
                                text_align="center",
                                margin_top="20px",
                            ),
                        align="center",
                        spacing=styles.Spacing.DEFAULT.value,
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text("En algún caso podría ser necesario administrar una medicación llamada eritropoyetina ", 
                                    rx.text.strong("mediante inyección subcutánea."),
                                    text_align="justify",
                            ),
                            rx.text("De ser así, se proporcionará una ", 
                                    rx.text.strong("hoja informativa"), 
                                    " con las instrucciones sobre el tratamiento.",
                                    text_align="justify",
                            ),
                        align="start",
                        width="100%",
                        ),
                        rx.vstack(
                            rx.image(
                                "/epoetina_alfa.png", 
                                width=["100%", "100%", "70%", "70%"],
                                align="center",
                                border_radius="14px",
                                margin_top="20px",
                            ),
                        align="center",
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text("En este caso, el paciente deberá recoger la medicación en el ", 
                                    rx.text.strong("Servicio de Dispensador de Farmacia"), 
                                    " ubicado en la ", 
                                    rx.text.strong("Planta Cero del Hospital General"),
                                    " en horario de:",
                                    text_align="justify",
                                    margin_top="20px",
                            ),
                            rx.list_item(
                                rx.text.strong("Mañanas:"),
                                " Lunes a viernes 9:00 a 15:00",
                                margin_top="5px",
                                text_align="justify",
                                margin_left=["10px", "10px", "80px", "80px"],
                                ),
                            rx.list_item(
                                rx.text.strong("Tardes (Previa Citación):"),
                                " Martes y jueves 15:30 a 19:00",
                                text_align="justify",
                                margin_left=["10px", "10px", "80px", "80px"],
                                ),
                        align="start",
                        width="100%", 
                        ),
                        rx.image(
                            "/farmacia.PNG", 
                            border_radius="20px",
                            margin_top="20px",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Posteriormente, se podrá admnistrar la inyección en el ",
                                rx.text.strong(" domicilio ",),
                                "con la ayuda de un familitar, o acudir ", rx.text.strong("a su Centro de Salud"), " para su aplicación",
                                text_align="justify",
                                margin_top="10px",
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


