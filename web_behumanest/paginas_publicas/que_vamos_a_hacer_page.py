import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.QUE_VAMOS_A_HACER.value, title="Que vamos a hacer")
def consentimientos() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="En consulta", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "¿QUÉ VAMOS A HACER?", 
                            size="7",
                            text_align="center",
                        ),
                        rx.text(
                            "Encuentro con un miembro del equipo de anestesia cardíaca",
                            size="4",
                            text_align="justify",
                        ),
                        rx.image(
                            "/grupo_medicos_1.png",
                            align="center",
                            width="60%",    
                            margin_y="10px",
                        ),
                        rx.list.unordered(
                            rx.list_item(
                                "Se realizará una ",
                                rx.text.strong("anamnesis completa"),
                                ", mediante preguntas para conocer su historial médico.",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se llevará a cabo una ",
                                rx.text.strong("exploración física"),
                                " y/o ",
                                rx.text.strong("pruebas complementarias"),
                                " si se considera necesario.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se explicarán las ",
                                rx.text.strong("pautas a seguir"),
                                " antes de la llamada de ingreso, aunque aún ",
                                rx.text.strong("no haya una fecha confirmada"),
                                " para el procedimiento quirúrgico.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se indicará si es necesario  ",
                                rx.text.strong("modificar o suspender algún tratamiento"),
                                " previo, en función de su situación clínica.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se podrá ",
                                rx.text.strong("prescribir un tratamiento específico"),
                                " y se le explicará detalladamente cómo seguirlo.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se le informará acerca de la ",
                                rx.text.strong("técnica anestésica"),
                                " que se empleará durante su cirugía.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se solicitará la ",
                                rx.text.strong("firma del consentimiento informado"),
                                " para la administración de anestesia.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Se le ofrecerá la posibilidad de ",
                                rx.text.strong("participar en el proyecto BeHumanest;"),
                                " en caso de aceptar, también deberá firmar el ",
                                rx.text.strong("consentimiento correspondiente"),
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "En algunos casos, se realizará una ",
                                rx.text.strong("revisión médica"),
                                " adicional, generalmente no presencial.",
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
    

