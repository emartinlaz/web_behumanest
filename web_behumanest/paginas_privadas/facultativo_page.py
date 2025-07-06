import reflex as rx
from ..db import crud
from ..routes import Route
from ..styles import styles
from ..componentes.cabecera import cabecera
from ..componentes.protected import *
from ..componentes.mensajes import *
from ..componentes.modales import *
from ..componentes.funciones import *
from ..componentes.menu_lateral import menu_lateral


debug = False


class FacultativoState(ProtectedState):
    error_mensaje_validacion: str = ""
    id_paciente: int = 0
    usuario_paciente: str = ""
    datos_paciente: str = ""
    estado_actual_paciente: str = ""
    nuevo_estado_paciente: str = ""
    observaciones: str = ""
    email_contacto: str = ""
    telefono_contacto: str = ""
    esta_el_paciente_en_gestion: bool = False
    combo_estados : list [str] = []

    
    def iniciar_pagina(self): 
        if not self.facultativo_logueado: return
        self.error_mensaje_validacion = ""
        self.load_combo_estado()
        self.reset_cambio_paciente()
        self.esta_el_paciente_en_gestion = False
        if debug: print("Iniciando pagina")
        if self.facultativo_logueado and self.facultativo_logueado.cambiar_contraseña:
            return ModalState.abrir_modal_cambio_contraseña_inicial  #Obliga a cambiar la contraseña la primera vezz que entra
        else:
            return rx.set_focus("ar_paciente")  
    
    def reset_cambio_paciente(self):
        self.error_mensaje_validacion = ""
        self.id_paciente = 0
        self.usuario_paciente = ""
        self.reset_paciente_en_gestion()
        
    def reset_paciente_en_gestion(self):
        self.esta_el_paciente_en_gestion = False
        self.datos_paciente = ""
        self.estado_actual_paciente = ""
        self.nuevo_estado_paciente = ""
        self.observaciones = ""

    def buscar_paciente(self, form_data: dict | None = None):
        if not form_data: return rx.set_focus("ar_paciente")     
        valor_input_usuario_paciente = form_data.get("ar_paciente", "")
        if valor_input_usuario_paciente:
            valor_input_usuario_paciente = valor_input_usuario_paciente.strip()
            self.usuario_paciente = valor_input_usuario_paciente
        else:
            self.usuario_paciente = ""
        self.error_mensaje_validacion = ""
        if self.usuario_paciente == "":
            self.error_mensaje_validacion = "Debe introducir el AR del paciente" 
            return rx.set_focus("ar_paciente")             
        self.reset_paciente_en_gestion()
        paciente_en_gestion = crud.get_paciente_by_usuario(usuario=self.usuario_paciente)
        if not paciente_en_gestion:
            self.error_mensaje_validacion = "El paciente no se encuentra dado de alta en el sistema" 
            return rx.set_focus("ar_paciente") 
        if not paciente_en_gestion.activo:
            self.error_mensaje_validacion = "El paciente no está activo. Puede activarlo desde el área gestión de pacientes" 
            return rx.set_focus("ar_paciente") 
        if paciente_en_gestion:
            self.id_paciente = paciente_en_gestion.id_paciente
            self.datos_paciente = f"{paciente_en_gestion.apellidos}, {paciente_en_gestion.nombre}"
            estado_actual_paciente_en_gestion = crud.get_estado_paciente_by_id_estado(id_estado=paciente_en_gestion.estado_actual)
            if estado_actual_paciente_en_gestion:
                #El paciente tiene un estado actual -> buscar el siguiente estado
                self.estado_actual_paciente = estado_actual_paciente_en_gestion.descripcion_estado
                self.nuevo_estado_paciente = self.estado_actual_paciente
                nuevos_estado = crud.get_estado_paciente_by_orden(estado_actual_paciente_en_gestion.orden+1)
                if nuevos_estado:
                    self.nuevo_estado_paciente = nuevos_estado.descripcion_estado 
                self.esta_el_paciente_en_gestion = True
            else:
                #El paciente no tiene aun ningun estado actual
                self.estado_actual_paciente = "-- Dado de alta en el sistema, sin estado asignado --"
                nuevos_estado = crud.get_estado_paciente_by_orden(1)
                if nuevos_estado:
                    self.nuevo_estado_paciente = nuevos_estado.descripcion_estado 
                self.esta_el_paciente_en_gestion = True           
            self.email_contacto = opcionalstr_to_str(paciente_en_gestion.email_contacto)
            self.telefono_contacto = opcionalstr_to_str(paciente_en_gestion.telefono_contacto)
    
    def nueva_busqueda_paciente(self):
        self.reset_cambio_paciente()
        return [
            rx.set_value("ar_paciente", ""),
            rx.set_value("observaciones", ""),
            rx.set_focus("ar_paciente"),
        ]
    
    def set_usuario_paciente(self, value: str):
        self.usuario_paciente = value  

    def set_nuevo_estado_paciente(self, value: str):
        self.nuevo_estado_paciente = value             
    
    def set_observaciones(self, value: str):
        self.observaciones = value      

    def detectar_enter_usuario_paciente(self, key):
        if key == "Enter":
            self.buscar_paciente() 

    def onclick_boton_enviar_comunicacion(self):
        if not is_valid_telefono(self.telefono_contacto, permitir_nulo=False) and not is_valid_email(self.email_contacto, permitir_nulo=False):
            #El paciente no tiene ningun contacto 
            return ModalState.abrir_modal_info(titulo="Comunicación no enviada",mensaje_1="El paciente no tiene definidos contactos para el envío de la comunicación") 
        else:
            #El paciente tiene al menos un contacto
            return ModalState.abrir_modal_confirmacion_envio_comunicacion(usuario=self.usuario_paciente,
                                                                          id_paciente=self.id_paciente,
                                                                          nuevo_estado=self.nuevo_estado_paciente,
                                                                          observaciones=self.observaciones,
                                                                          email_contacto=self.email_contacto,
                                                                          telefono_contacto=self.telefono_contacto,
                                                                          origen="facultativo", 
                                                                          )
    
    def abrir_modal_confirmar_comunicacion(self):
        self.modal_confirmar_comunicacion_abierto = True
        
    def load_combo_estado(self):
        self.combo_estados.clear()
        estados_paciente = crud.get_estados_paciente()
        for estado in estados_paciente:
            self.combo_estados.append(estado.descripcion_estado)

    
@rx.page(route=Route.FACULTATIVO.value,title='Facultativos', on_load=FacultativoState.iniciar_pagina)
@facultativo_requerido
def facultativo() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(  
            cabecera(titulo=f"Área facultativo", mostrar_link_area_privada=True),
            ficha_gestion_paciente(),
            alta_paciente(),
        width="100%",
        padding_left=["5px", "5px", "5px", "360px"],
        padding_right=["5px", "5px", "5px", "20px"],
        padding_top=["90px", "90px", "90px", "100px",], 
        align="center",
        spacing="5",
        ),
        modales_facultativo(),
    align="center",
    width="100%", 
    spacing="0",
    on_mount=ProtectedState.comprobar_sesion_caducada,
)
    
def handle_paciente_detectado(event):
    decoded_text = event['detail']
    FacultativoState.set_usuario_paciente(decoded_text)

def ficha_gestion_paciente() -> rx.Component:
    return rx.card(
            rx.vstack(
                rx.text(f"Comunicar cambio de estado del paciente", 
                    size="6",  
                    margin_y="10px", 
                    weight="medium",
                    align="center",
                    ),
                rx.vstack(
                    rx.cond(
                        FacultativoState.error_mensaje_validacion != "",
                        rx.callout(
                            FacultativoState.error_mensaje_validacion,
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                            width="100%",
                        ), 
                    ),
                    rx.form(
                        rx.text(
                            "Paciente",
                            size="3",
                            weight="medium",
                            text_align="left",
                            margin_top="10px",
                        ),
                        rx.hstack(
                            rx.input(
                                name="ar_paciente",
                                id="ar_paciente",
                                placeholder="Introduzca el AR del paciente",
                                max_length=50,
                                size="3",
                                width="60%",
                                margin_top="-10px", 
                                on_key_up=FacultativoState.detectar_enter_usuario_paciente,
                                autocomplete="new-password",
                            ),
                            rx.button("Buscar",
                                size="4",
                                name="boton_buscar",
                                id="boton_buscar",
                                width="40%",
                                height="40px",
                                margin_top="-10px", 
                                type_="submit", #"button",
                            ),
                        margin_top="10px",
                        width="100%",  
                        ),
                    on_submit=FacultativoState.buscar_paciente, 
                    ),
                    lector_qr(),
                    rx.cond(
                        FacultativoState.esta_el_paciente_en_gestion,
                        cambio_estado(),
                    ), 
                align="start", 
                width="100%",   
                ),
            align="center", 
            padding="20px",
            width="100%",
            ),  
        width="100%",
        max_width="580px",
        border_width="2px",
        border_color=styles.Color.BORDER_CARD.value,
        border_radius="14px",  
        margin_x="5px", 
        )

def alta_paciente() -> rx.Component:
    from .gestion_pacientes_page import GestionPacienteState
    return rx.card(
            rx.vstack(
                rx.text(f"Acceso directo", 
                    size="6",  
                    margin_y="10px", 
                    weight="medium",
                    align="center",
                    ),
                rx.vstack(
                    rx.button("Añadir nuevo paciente",
                        size="4",
                        name="registrar",
                        type="button",
                        width="70%",
                        height="40px",
                        margin_top="-10px", 
                        on_click=ModalState.abrir_modal_añadir_paciente("facultativo"),
                    ),
                align="center", 
                width="100%",   
                ),
            align="center", 
            padding="20px",
            width="100%",
            spacing="5",
            ),  
        width="100%",
        max_width="580px",
        border_width="2px",
        border_color=styles.Color.BORDER_CARD.value,
        border_radius="14px",  
        margin_x="5px", 
        )


def cambio_estado() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Datos del paciente",
            size="3",
            weight="medium",
            text_align="left",
        ),
        rx.text(
            FacultativoState.datos_paciente,
            margin_top="-10px",
            padding="8px",
            border="1px solid #ccc",
            border_radius="6px",
            background_color=styles.Color.FONDO_INPUT_TEXT.value,
            color="black",
            font_size="16px",
            width="100%",
            cursor="default",
            style={
                "box-shadow": "inset 0 1px 3px rgba(0,0,0,0.1)",  # como un input real
                "user-select": "none",  # evita que el usuario seleccione el texto
            }
        ),
        rx.text(
            "Estado actual",
            size="3",
            weight="medium",
            text_align="left",
        ),
        rx.text(
            FacultativoState.estado_actual_paciente,
            margin_top="-10px",
            padding="8px",
            border="1px solid #ccc",
            border_radius="6px",
            background_color=styles.Color.FONDO_INPUT_TEXT.value,
            color="black",
            font_size="16px",
            width="100%",
            cursor="default",
            style={
                "box-shadow": "inset 0 1px 3px rgba(0,0,0,0.1)",  # como un input real
                "user-select": "none",  # evita que el usuario seleccione el texto
            }
        ),
        rx.text(
            "Nuevo estado",
            size="3",
            weight="medium",
            text_align="left",
            margin_top="20px",
        ),  
        rx.box(
            rx.select(
                FacultativoState.combo_estados,
                value=FacultativoState.nuevo_estado_paciente,
                on_change=FacultativoState.set_nuevo_estado_paciente,
            size='3',
            width="100%",
            ),
        width="100%",
        margin_top="-10px",
        padding="0px",
        ),
        rx.text(
            "Observaciones (máximo 50 caracteres)",
            size="3",
            weight="medium",
            text_align="left",
            margin_top="10px",
        ),  
        rx.input(
            name="observaciones",
            id="observaciones",
            placeholder="Introduzca las observaciones a enviar en el mensaje",
            max_length=50,
            size="3",
            width="100%",
            margin_top="-10px", 
            on_change=FacultativoState.set_observaciones,
            autocomplete="new-password",
        ),
        rx.hstack(
            rx.button(
                "Enviar comunicación", 
                on_click=FacultativoState.onclick_boton_enviar_comunicacion, 
                size="3",
                flex="1",
            ),  
            rx.button("Nueva búsqueda", 
                on_click=FacultativoState.nueva_busqueda_paciente, 
                size="3",
                flex="1",
            ),
        spacing="4",
        width="100%",
        padding_top = "20px"
        ),
    #margin_top="20px",
    width="100%",
    )
    

def lector_qr() -> rx.Component:
    return rx.vstack(
        rx.html('''
            <div id="reader" style="width: 300px; margin-top: 20px;"></div>
        '''),
        rx.cond(
            FacultativoState.esta_el_paciente_en_gestion == False,
            rx.button(
                "Escanear QR con cámara",
                on_click=rx.call_script(f'''
                        if (typeof Html5Qrcode === "undefined") {{
                            const script = document.createElement("script");
                            script.src = "/html5-qrcode.min.js";
                            script.onload = function() {{
                                iniciarEscaneoQR();
                            }};
                            document.body.appendChild(script);
                        }} else {{
                            iniciarEscaneoQR();
                        }}

                        function iniciarEscaneoQR() {{
                            var inputPaciente = document.getElementById("ar_paciente");
                            if (inputPaciente) {{
                                inputPaciente.value = "";
                            }}               
                            const qrReader = new Html5Qrcode("reader");
                            qrReader.start(
                                {{ facingMode: "environment" }},
                                {{ fps: 10, qrbox: 250 }},
                                (decodedText, decodedResult) => {{
                                    console.log("Código QR detectado:", decodedText);

                                    if (inputPaciente) {{
                                        inputPaciente.value = decodedText;
                                        console.log("Codigo enviado.");
                                    }}
                                        
                                    var botoBuscar = document.getElementById("boton_buscar");
                                    if (botoBuscar) {{
                                        botoBuscar.click();
                                    }}
                                        
                                    qrReader.stop().then(function() {{
                                        console.log("Cámara detenida después de escanear.");
                                    }}).catch(function(err) {{
                                        console.error("Error al detener cámara:", err);
                                    }});
                                }},
                                (errorMessage) => {{
                                    //console.log("Error de escaneo:", errorMessage);
                                }}
                            ).catch(err => {{
                                console.error("Error iniciando lector QR:", err);
                                alert("Este dispositivo no tiene acceso a la cámara.");
                            }});              
                        }}
                    '''),
                color="primary", 
                size="4", 
            ),

        ),
        width="100%",
        align="center",
        margin_top="-10px",
    )