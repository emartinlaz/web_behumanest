import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles



@rx.page(route=Route.INDICACIONES_ESPECIFICAS_HIERRO.value, title="Indicaciones Generales")
def indicaciones_especificas_hierro() -> rx.Component:
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
                                text_align="justify",
                            ),
                            rx.image(
                                "/indicaciones_especificas.png",
                                width=["80%", "80%", "50%", "50%"],
                                margin_top="20px",
                            ),
                            rx.text(
                                "Tratamiento con Hierro Intravenoso", 
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
                            rx.text("En algún caso será necesario poner un ", 
                                    rx.text.strong("gotero de hierro."),
                                    text_align="justify",
                            ),
                            rx.text("Se deberá acudir al ", 
                                    rx.text.strong("Hospital de Día Polivalente, Planta Primera del Hospital General, Sala 101."),
                                    text_align="justify",
                            ),
                                                align="start",
                        width="100%", 
                        ),
                        rx.image(
                            "/hospital_dia.png", 
                            border_radius="14px",
                            width=["100%", "100%", "70%", "70%"],
                        ),
                        rx.vstack(
                            rx.text(
                                "En caso de ser ",
                                rx.text.strong(" fuera de Zaragoza",),
                                ", existe la posibilidad de hacerlo en el ", rx.text.strong("hospital de referencia"), " del paciente.",
                                text_align="justify",
                                margin_top="20px",
                            ),
                            rx.text(
                                "Si es posible, se recibe en el ", 
                                rx.text.strong("Hospital Miguel Servet el mismo día"), 
                                " de la consulta de anestesia (sólo si es posible por agenda).",
                                text_align="justify",
                            ),
                            rx.text(
                                "En la consulta de anestesia, se indicará el ", 
                                rx.text.strong("día y la hora"), 
                                " para llevar a cabo el ", 
                                rx.text.strong("tratamiento"), 
                                " junto con una hoja informativa.",
                                text_align="justify",
                            ),
                        align="start",
                        spacing=styles.Spacing.DEFAULT.value,
                        width="100%", 
                        ),
                        rx.vstack(
                            rx.image(
                                "/tratamiento_hierro.png", 
                                width=["100%", "100%", "70%", "70%"],
                                border_radius="14px",
                                margin_top="20px",
                            ),
                        align="center",
                        width="100%",                   
                        ),
                        rx.vstack(
                            rx.text(
                                "La duración aproximada del tratamiento es de ", 
                                rx.text.strong("una hora"),
                                ". Después se podrá hacer ", 
                                rx.text.strong("vida normal."),
                                text_align="justify",
                                margin_top="20px",
                            ),
                            rx.text(
                                rx.text.strong("No es necesario"), 
                                " acudir en ", 
                                rx.text.strong("ayunas"), 
                                " para llevar a cabo el tratamiento.",
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


