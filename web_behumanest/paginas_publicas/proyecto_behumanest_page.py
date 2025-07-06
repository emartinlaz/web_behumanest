import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.PROYECTO_BEHUMANEST.value, title="Proyecto BeHumanest")
def proyecto_behumanest() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="En consulta", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "PARTICIPACIÓN EN PROYECTO BEHUMANEST", 
                            size="7",
                            text_align="center",
                        ),
                        rx.text(
                            "Cuando el paciente se encuentre en ",
                            rx.text.strong("consulta, "),
                            "junto con el equipo facultativo, se llevará a cabo:",
                            text_align="justify",
                            margin_top=["0px","0px","0px","10px"],
                        ),
                        rx.hstack(
                            rx.image(
                                "/consulta_1.png", 
                                width="40%",
                            ),
                            rx.list.unordered(
                                rx.list_item(
                                    "Dar a ",
                                    rx.text.strong("conocer"),
                                    " Proyecto Piloto ",
                                    rx.text.strong("BeHumanest."),
                                    text_align="justify",
                                ),
                                rx.list_item(
                                    "Pedir ",
                                    rx.text.strong("autorización"),
                                    " para participar en el proyecto.",
                                    text_align="justify",
                                    margin_top="30px",
                                ),
                            width="60%",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.text(
                            "En caso de que el paciente esté ",
                            rx.text.strong("interesado ",),
                            "en participar, deberá firmar el ",
                            rx.text.strong("consentimiento",),
                            " establecido.",
                            text_align="justify",
                            padding_y="10px",
                        ),
                        rx.hstack(
                            rx.image(
                                "/consentimiento_behumanest.png",
                                width="40%",
                            ),
                            rx.text(
                                "El paciente deberá ",
                                rx.text.strong("firmar ",),
                                "el documento en consulta, " ,
                                rx.text.strong(" autorizando el uso ",),
                                "de sus datos y la ",
                                rx.text.strong("participación ",),
                                "en el proyecto.",
                                text_align="justify",
                                width="60%",
                                margin_left="10px",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.text(
                            "Será entonces cuando el facultativo dé de ",
                            rx.text.strong("alta al paciente en la aplicación."),
                            text_align="justify",
                            margin_y="10px",
                        ),
                        rx.hstack(
                            rx.image(
                                "/consulta_2.png",
                                width="40%",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Se pedirá al paciente los siguientes " ,
                                    rx.text.strong("datos"),
                                    " para su alta en la aplicación:.",
                                    text_align="justify",
                                ),
                                rx.list.unordered(
                                    rx.list_item("Nombre"),
                                    rx.list_item("Apellidos", margin_top="8px",),
                                    rx.list_item("Dirección de correo electrónico", margin_top="8px",),
                                    rx.list_item("Teléfono móvil", margin_top="8px",),
                                ),
                            align="start",
                            spacing=styles.Spacing.DEFAULT.value,
                            margin_left="10px", 
                            width="60%",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.text(
                            "Al crear al usuario, el",   
                            rx.text.strong(" sistema enviará"),
                            " de manera automática ",
                            rx.text.strong("la contraseña del primer acceso al paciente"),
                            text_align="justify",
                            margin_y="10px",
                        ),
                        rx.hstack(
                            rx.image(
                                "/recibir_comunicacion.png",
                                width="20%",                                         
                            ),
                            rx.text(
                                "Si ha facilitado un ",
                                rx.text.strong("correo electrónico"),
                                ", recibirá un ",
                                rx.text.strong("email con la contraseña " ,),
                                text_align="justify",
                                margin_left="20px", 
                                width="80%",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.hstack(
                            rx.image(
                                "/recibir_sms.png",
                                width="20%",
                            ),
                            rx.text(
                                "Si ha facilitado un ",
                                rx.text.strong("telefono móvil"),
                                ", recibirá un ",
                                rx.text.strong("SMS con la contraseña " ,),
                                text_align="justify",
                                margin_left="20px",
                                width="80%",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.hstack(
                            rx.image(
                                "/ambas_coms_familiar.png",
                                width="20%",
                            ),
                            rx.text(
                                "Si ha facilitado ", 
                                rx.text.strong("ambos datos"),
                                ", la contraseña será enviada ",
                                rx.text.strong("por ambos medios " ,),
                                text_align="justify",
                                margin_left="20px",
                                width="80%",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.text(
                            "EL USUARIO YA  ",   
                            rx.text.strong(" PODRÁ ACCEDER AL ÁREA PRIVADA"),
                            " DE LA WEB ",
                            rx.text.strong("BEHUMANEST"),
                            text_align="justify",
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


