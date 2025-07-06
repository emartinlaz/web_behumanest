import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.QUE_LLEVAR_INGRESO.value, title="Ingreso")
def que_llevar_ingreso() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Ingreso", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "¿QUÉ DEBO LLEVAR EL DÍA DEL INGRESO?",
                            text_align="center",
                        ),
                        rx.image(
                            "/maleta_hospital.png",
                            align="center",
                            width="40%",   
                            margin_top=["0px", "0px", "0px", "20px"],
                        ),
                        rx.text("Se ", 
                                rx.text.strong("recomienda"), 
                                " seguir las siguientes ", 
                                rx.text.strong("pautas"), 
                                " a tener en cuenta para el día del ingreso:", 
                                padding_top="15px",
                                text_align="start",
                            ),
                        rx.list.unordered(
                            rx.list_item(
                                "Llevar su ",
                                rx.text.strong("medicación habitual"),
                                ", incluyendo los inhaladores si los utiliza.",
                                text_align="justify",
                                ),
                            rx.list_item(
                                rx.text.strong("Zapatillas y utensilios de uso personal"),
                                " como cepillo de dientes, pasta dental, peine, entre otros.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            rx.list_item(
                                "Es importante  ",
                                rx.text.strong("retirar el esmalte de uñas"),
                                " en caso de llevarlo.",
                                margin_top="10px",
                                text_align="justify",
                                ),
                            padding_left=["0px", "0px", "0px", "60px"],
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
    

