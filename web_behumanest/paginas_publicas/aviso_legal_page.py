import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.AVISO_LEGAL.value, title="BeHumanest")
def aviso_legal() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Aviso Legal", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "AVISO LEGAL DE BEHUMANEST", 
                                size="7",
                                text_align="center",
                            ), 
                        align="center",                       
                        width="100%",
                        ),                        
                        rx.vstack(
                            rx.text(rx.text.strong("1.- Identificación del titular del sitio web:"),),
                                rx.list.unordered(
                                    rx.list_item("Denominación Social: BEHUMANEST"),
                                    rx.list_item("Correo electrónico de contacto: behumanest@gmail.com"),
                                    margin_top="5px",
                                    text_align="justify",
                                    ),
                            rx.text(rx.text.strong("2.- Normas de uso del sitio web"),),
                            rx.text(
                                "El usuario se compromete a utilizar el sitio web de forma diligente, de acuerdo con la legalidad y las condiciones de uso aquí descritas. Se prohíbe el uso del sitio web para fines ilícitos o perjudiciales.",
                                text_align="justify",
                            ),
                            rx.text(rx.text.strong("3.- Propiedad intelectual e industrial"),),
                            rx.text(
                                "El usuario se compromete a utilizar el sitio web de forma diligente, de acuerdo con la legalidad y las condiciones de uso aquí descritas. Se prohíbe el uso del sitio web para fines ilícitos o perjudiciales.",
                                text_align="justify",
                            ),
                            rx.text(rx.text.strong("4.-  Enlaces externos"),),
                            rx.text(    
                                "El sitio web no contiene enlaces a sitios web de terceros.",
                                text_align="justify",
                            ),
                            rx.text(rx.text.strong("5.-  Responsabilidad"),),
                            rx.text(
                                "BEHUMANEST no garantiza la disponibilidad permanente del sitio web ni se hace responsable de los daños derivados de su uso.",
                                text_align="justify",
                            ),
                            rx.text(rx.text.strong("6.-  Legislación Aplicable y juridiscción"),),
                            rx.text(
                                "Este aviso legal se rige por la legislación española. Cualquier controversia se someterá a los juzgados y tribunales del domicilio del usuario o, en su defecto, de Zaragoza.",
                                text_align="justify",
                            ),
                        align="start",
                        spacing=styles.Spacing.DEFAULT.value,
                        margin_top="20px",
                        width="100%",
                        ),
                    align="start",
                    width="100%",    
                    padding_x=["10px", "10px", "10px", "80px"],
                    padding_y=["10px", "10px", "10px", "20px"], 
                    ),
                width="100%",
                max_width="800px",
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



