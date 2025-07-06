import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.UBICACION_CONSULTA.value, title="En consulta")
def ubicacion_consulta() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="En consulta", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.heading(
                            "UBICACIÓN DE LA CONSULTA DE ANESTESIA", 
                            size="7",
                            text_align="center",
                            
                        ),
                        rx.image(
                            "/ubicacion_consulta.png",
                            width=["100%", "100%", "95%", "95%"],
                            margin_top="10px",
                            border_radius="14px",
                        ),
                        rx.text(
                            " La ", 
                            rx.text.strong("consulta de visita"), 
                            " de anestesia previo al proceso quirúrgico se ", 
                            rx.text.strong("encuentra"), 
                            " ubicada en:",
                            text_align="justify",
                            margin_top="20px",
                        ),
                        rx.text(
                            "CONSULTAS EXTERNAS", 
                            font_weight="bold",
                            text_decoration="underline",
                            margin_top="20px",    
                        ),
                        rx.link(
                            "Calle Padre Arrupe s/n", 
                            #"CALLE PADRE ARRUPE S/N",
                            font_weight="bold",
                            #text_decoration="underline",
                            href="https://www.google.com/maps/place/C.+del+Padre+Arrupe,+50009+Zaragoza/@41.6333003,-0.9042704,17z/data=!3m1!4b1!4m6!3m5!1s0xd59152bef0deccf:0x633c13da63ae4451!8m2!3d41.6332963!4d-0.9016901!16s%2Fg%2F1hjh2t6sh?entry=ttu&g_ep=EgoyMDI1MDQyNy4xIKXMDSoASAFQAw%3D%3D",
                            is_external="true", 
                        ),
                        rx.text.strong("PLANTA PRIMERA"),
                        rx.text.strong("CONSULTA 2 ANESTESIA"),
                        rx.image(
                            "/puerta_consulta.png", 
                            border_radius="14px",
                            width=["80%", "80%", "60%", "60%"],
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


