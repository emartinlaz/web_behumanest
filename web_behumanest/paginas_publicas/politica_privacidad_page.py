import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.POLITICA_PRIVACIDAD.value, title="BeHumanest")
def politica_privacidad() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Política de Privacidad", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "POLÍTICA DE PRIVACIDAD DE BEHUMANEST", 
                                size="7",
                                text_align="center",
                            ),      
                        align="center",
                        width="100%",
                        ),                        
                        rx.vstack(
                            rx.text(
                                "En cumplimiento de lo establecido en el Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo, de 27 de abril de 2016, relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales y a la libre circulación de estos datos (RGPD), y en la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD), se informa a los usuarios de la presente plataforma de los aspectos relacionados con el tratamiento de sus datos personales",
                                text_align="justify",
                            ),
                            rx.text(rx.text.strong("1.- Responsable del tratamiento:"),),
                                rx.list.unordered(
                                    rx.list_item("Responsable: Unidad de Anestesia de Cardiotorácica"),
                                    rx.list_item("Correo electrónico de contacto: behumanest@gmail.com"),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("2.- Finalidad del tratamiento:"),),
                                rx.list.unordered(
                                    rx.list_item("Gestionar el registro y acceso de los usuarios a la plataforma behumanest."),
                                    rx.list_item("Facilitar la utilización de las funcionalidades disponibles."),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("3.- Base Legal del tratamiento:"),),
                                rx.list.unordered(
                                    rx.list_item("Consentimiento expreso del usuario."),
                                    #rx.list_item("CFacilitar la utilización de las funcionalidades disponibles."),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("4.- Datos tratados:"),),
                                rx.list.unordered(
                                    rx.list_item("Datos identificativos: nombre, apellidos."),
                                    rx.list_item("Datos de contacto: correo electrónico."),
                                    rx.list_item("Datos de acceso: usuario y contraseña cifrada."),
                                    rx.list_item("Datos de actividad en la plataforma."),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("5.- Conservación de los datos:"),),
                                rx.list.unordered(
                                    rx.list_item("Mientras la cuenta del usuario esté activa."),
                                    rx.list_item("Posteriormente, bloqueados durante el plazo necesario para atender responsabilidades legales."),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("6.- Destinatarios:"),),
                                rx.list.unordered(
                                    rx.list_item("No se cederán datos a terceros salvo obligación legal."),
                                    rx.list_item("Los datos se tratarán en servidores ubicados en la Unión Europea."),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("7.- Derechos de los usuarios:"),),
                                rx.list.unordered(
                                    rx.list_item("Acceso, rectificación, supresión, oposición, limitación, portabilidad y retirada del consentimiento."),
                                    rx.list_item("Ejercicio de derechos mediante solicitud a [correo electrónico de contacto]."),
                                    rx.list_item("Derecho a presentar reclamación ante la Agencia Española de Protección de Datos, a través de la aepd.es"),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            align="start",
                            spacing=styles.Spacing.DEFAULT.value,
                            width="100%",
                            margin_top="20px",
                        ),
                    align="start",
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



