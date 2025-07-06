import reflex as rx
from ..routes import Route
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles




@rx.page(route=Route.COMUNICACION_BEHUMANEST.value, title="Información para las familias")
def comunicacion_behumanest() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Información para las familias", mostrar_link_area_privada=True),
            rx.vstack(
                rx.card(
                    rx.vstack(
                        rx.vstack(
                            rx.heading(
                                "CONFIGURACIÓN COMUNICACIÓN BEHUMANEST", 
                                size="7",
                                text_align="center",
                            ),
                            rx.image(
                                "/comunicacion_proceso.png",
                                width=["80%", "80%", "60%", "60%"],
                            ),
                        align="center",
                        width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Uno de los principales ", 
                                rx.text.strong("objetivos"), 
                                " del proyecto ", 
                                rx.text.strong("BeHumanest"), 
                                " es promover la ", 
                                rx.text.strong("humanización"), 
                                ", no solo del paciente, sino también de sus ", 
                                rx.text.strong("familiares"), ", quienes atraviesan momentos de gran tensión y ansiedad, especialmente en intervenciones quirúrgicas de larga duración.",
                                text_align="justify",
                            ),
                            rx.text(
                                "Por ello, BeHumanest facilita la ", 
                                rx.text.strong("comunicación"), 
                                " entre el ", 
                                rx.text.strong("equipo médico y los contactos"), 
                                " designados por el paciente, permitiendo mantenerlos informados sobre las ", 
                                rx.text.strong("distintas etapas"), 
                                " del procedimiento quirúrgico.",
                                text_align="justify",
                            ),
                            rx.text(
                                "Una vez el paciente haya ", 
                                rx.text.strong("iniciado sesión"), 
                                ", accederá al formulario que permitirá la ", 
                                rx.text.strong("configuración de los Contactos"), 
                                " donde desea que reciban comunicaciones durante el proceso quirúrgico.",
                                text_align="justify",
                            ),
                        align="start",
                        width="100%",                  
                        ),
                        rx.vstack(
                            rx.image(
                                "/contactos_pacientes.png", 
                                width=["80%", "80%", "50%", "50%"],
                            ),
                        align="center",
                        width="100%",                  
                        ),
                        rx.vstack(
                            rx.text(
                                "El sistema permite introducir un correo electrónico y/o un teléfono móvil:",
                                text_align="justify",
                            ),
                        align="start",  
                        width="100%",                   
                        ),
                        rx.hstack(
                            rx.image(
                                "/recibir_comunicacion.png", 
                                width="20%",
                            ),
                            rx.text(
                                "En caso de introducir un ", 
                                rx.text.strong("correo electrónico"), 
                                ", las comunicaciones se enviarán a esa ", 
                                rx.text.strong("dirección de correo."),
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
                                "En caso de introducir un ", 
                                rx.text.strong("teléfono móvil"), 
                                ", las comunicaciones se enviarán a través de un ", 
                                rx.text.strong("SMS."),
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
                                "Si el paciente introduce ", 
                                rx.text.strong("ambos contactos"), 
                                " , los avisos se enviarán por los ambos medios, ", 
                                rx.text.strong("por email y SMS."),
                                text_align="justify",
                                margin_left="20px",
                                width="80%",
                            ),
                        align_items="center",
                        width="100%",
                        ),
                        rx.text(
                            "Para ", 
                            rx.text.strong("confirmar"), 
                            " que el envío se produce de manera correcta, el paciente tendrá la posibilidad de realizar ", 
                            rx.text.strong("tres envíos de prueba"), 
                            " con los datos que haya introducido en ese momento",
                            text_align="justify",
                        ),
                        rx.vstack(
                            rx.image(
                                "/envio_prueba.png", 
                                width=["80%", "80%", "50%", "50%"],
                            ),
                        align="center", 
                        width="100%",                
                        ),
                        rx.vstack(
                            rx.text(
                                "El paciente podrá ", 
                                rx.text.strong("modificar"), 
                                " estos datos siempre que quiera, ", 
                                rx.text.strong("accediendo"), 
                                " a la página web de ", 
                                rx.text.strong("BeHumanest"),".",
                                text_align="justify",
                            ),
                            rx.text(
                                "En caso de que el paciente aporte ", 
                                rx.text.strong("datos de contacto"), 
                                ", dichos contactos recibirán un SMS y/o correo electrónico con los siguientes posibles mensajes: ",
                                text_align="justify",
                            ),
                            rx.list_item( 
                                rx.text.strong("INICIO CIRUGÍA:"),
                                "  Momento en el que el paciente entra en quirófano. Pueden pasar varias horas desde que el paciente sale de la habitación, hasta que entra en quirófano.",
                                text_align="justify",
                                margin_top="10px",
                            ),
                            rx.list_item(
                                rx.text.strong("FIN CIRUGÍA:"), 
                                " Momento en el que termina la intervención. NO se dará información de carácter médico a través de BeHumanest.", 
                                text_align="justify",
                            ),
                            rx.list_item(
                                rx.text.strong("TRASLADO A UCI:"),
                                " Momento en el que el paciente es trasladado a la Unidad de Cuidados Intensivos para su control y observación.",
                                text_align="justify",
                            ),
                        align="start",
                        width="100%",                  
                        ),
                        rx.vstack(
                            rx.text.strong("¡IMPORTANTE!", color="red"),
                        align="center", 
                        width="100%",                   
                        ),
                        rx.list.unordered(
                            rx.list_item(
                                rx.text.strong("Nunca", ), 
                                " se dará ninguna información de ", 
                                rx.text.strong("carácter médico."),
                                text_align="justify",
                            ),
                            rx.list_item(
                                rx.text.strong("No"), 
                                " nos hacemos ", 
                                rx.text.strong("responsables"), 
                                " en caso de que dicha información ", 
                                rx.text.strong("no llegue"), 
                                " por motivos ajenos, mala conectividad, etc.", 
                                text_align="justify",
                            ),
                            rx.list_item(
                                "La ", rx.text.strong("información"), 
                                " de la intervención quirúrgica y situación médica de su familiar la recibirán por los ", 
                                rx.text.strong("facultativos responsables en la UCI."), 
                                text_align="justify",
                            ),
                            rx.list_item(
                                "En caso de haber recibido dicha información, recibirán una ", 
                                rx.text.strong("encuesta para valorar su grado de satisfacción"), 
                                " con la aplicación", 
                                text_align="justify",
                                ),
                        
                        ),
                    align="center",
                    spacing=styles.Spacing.BIG.value,
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


