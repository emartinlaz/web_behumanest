import reflex as rx
from ..routes import Route
from ..componentes.protected import *
from ..db import crud
from ..styles import styles
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral

debug = False


class LoginState(ProtectedState):
    usuario: str = ""
    error_message: str = ""
    mostrar_check_condiciones: bool = False
    condiciones_aceptadas: bool = False
    escanear_qr: bool = False
    boton_submit: str = "" #Para controlar si el submit ha sido enviado por la camara o inicio sesión

    
    def init_pagina(self):
        self.error_message = "" 
        self.mostrar_check_condiciones = False
        self.condiciones_aceptadas = False
        self.usuario = ""
        #self.contraseña = ""
        return rx.set_focus("usuario") 
        
    @rx.event
    def set_usuario(self, value: str):
        #self.usuario = value.strip().upper()
        self.usuario = value  
    
    @rx.event
    def detectar_enter_usuario(self, key):
        if key == "Enter":
            return rx.set_focus("contraseña")

    def onblur_usuario(self):
        paciente_existe = crud.get_paciente_by_usuario(self.usuario)
        if paciente_existe:
            self.mostrar_check_condiciones = True
        else:
            self.mostrar_check_condiciones = False
        
    def on_doble_click(self):
        self.escanear_qr = not self.escanear_qr

    def on_submit_inicio_sesion(self, form_data: dict | None = None):
        self.escanear_qr = False
        if not form_data: 
            self.error_message = "El usuario no puede estar vacio" 
            return rx.set_focus("usuario")  
        form_usuario = form_data.get("usuario")
        if not form_usuario:
            self.error_message = "El usuario no puede estar vacio" 
            return rx.set_focus("usuario")
        if self.boton_submit == "qr_camara":
            self.usuario = form_usuario
            return rx.set_focus("contraseña") 
        #analizar si hay que mostar el aceptar condiciones
        es_paciente = crud.get_paciente_by_usuario(form_usuario)
        if es_paciente:
            self.mostrar_check_condiciones = True
        else:
            self.mostrar_check_condiciones = False
        #form_contraseña = "" if form_data.get("contraseña") is None else form_data.get("contraseña")
        #if form_contraseña == "": return rx.set_focus("contraseña")  
        form_contraseña = form_data.get("contraseña")
        if not form_contraseña:
            self.error_message = "La contraseña no puede estar vacia" 
            return rx.set_focus("contraseña")     
        facultativo = crud.get_facultativo_by_usuario(usuario=self.usuario)
        paciente = crud.get_paciente_by_usuario(usuario=self.usuario)    
        if not facultativo and not paciente:
            self.error_message = "El usuario o la contraseña no son correctos"  
            return [
                rx.set_value("usuario", ""),
                rx.set_value("contraseña", ""),
                rx.set_focus("usuario"),
            ]      
        if facultativo and facultativo.activo:
            #El usuario es un facultativo -> verificaccion del password
            if facultativo.check_password(form_contraseña): 
                self._login(token=self.router.session.client_token, id_facultativo=facultativo.id_facultativo)
                return rx.redirect(Route.FACULTATIVO.value)
            else:
                self.error_message = "El usuario o la contraseña no son correctos"  
                return [
                    rx.set_value("contraseña", ""),
                    rx.set_focus("contraseña"),
                ] 
        if paciente and paciente.activo:
            #El usuario es un paciente -> verificaccion del password
            if not self.condiciones_aceptadas:
                self.error_message = "Para poder iniciar sesión, se deben aceptar la política de privacidad"  
                return
            if paciente.check_password(form_contraseña): 
                self._login(token=self.router.session.client_token, id_paciente=paciente.id_paciente)                
                return rx.redirect(Route.PACIENTE.value)
            else:
                self.error_message = "El usuario o la contraseña no son correctos"  
                return [
                    rx.set_value("contraseña", ""),
                    rx.set_focus("contraseña"),
                ]     
        self.error_message = "Error desconocido" 
        return     
   
    @rx.event
    def cambiar_condiciones(self, value: bool):
        self.condiciones_aceptadas = value

    @rx.event
    def on_click_boton_submit(self, boton: str):
        self.boton_submit = boton

       


@rx.page(route=Route.LOGIN.value, title="Login", on_load=LoginState.init_pagina)
def login_usuario() -> rx.Component:
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Inicio sesión área privada", mostrar_link_area_privada=False),
            rx.card(
                rx.vstack(                
                    rx.image(
                        src="/SALUD.png",
                        #width="2.5em",
                        width="40%",
                        height="auto",
                        #   border_radius="25%",
                    ),
                    rx.cond(
                        LoginState.error_message != "",
                        rx.callout(
                            LoginState.error_message,
                            icon="triangle_alert",
                            color_scheme="red",
                            role="alert",
                            width="100%",
                        ), 
                    ),
                    rx.form(
                        rx.vstack(
                            rx.text(
                                "Usuario",
                                size="3",
                                weight="medium",
                                text_align="left",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("user")),
                                id="usuario",
                                name="usuario",
                                placeholder="Introduzca el usuario",
                                #type="email",
                                size="3",
                                width="100%",
                                on_change=LoginState.set_usuario,
                                on_blur=LoginState.onblur_usuario,
                                #on_key_down=LoginState.detectar_enter_usuario,
                                on_key_up=LoginState.detectar_enter_usuario,
                                autocomplete="new-password",
                                on_double_click=LoginState.on_doble_click,
                            ),
                            rx.cond(
                                LoginState.escanear_qr,
                                lector_qr(),
                            ),
                            rx.cond(
                                LoginState.escanear_qr,
                                ventana_qr(),
                            ),
                            rx.text(
                                "Contraseña",
                                size="3",
                                weight="medium",
                                text_align="left",
                                margin_top="20px",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("lock")),
                                id="contraseña",
                                name="contraseña",
                                placeholder="Introduzca la contraseña",
                                type="password",
                                size="3",
                                width="100%",
                                #on_change=LoginState.set_contraseña,
                                #on_key_down=LoginState.detectar_enter_contraseña,
                                autocomplete="new-password",
                            ),
                            rx.cond(
                                LoginState.mostrar_check_condiciones,
                                rx.box(
                                    rx.hstack(
                                        rx.checkbox(
                                            "Acepto la",
                                            default_checked=False,
                                            spacing="2",
                                            checked=LoginState.condiciones_aceptadas,
                                            on_change=LoginState.cambiar_condiciones,                                
                                        ),
                                        rx.link(
                                            rx.text("Política de Privacidad", size='2', margin_left="-5px",),
                                            href=Route.POLITICA_PRIVACIDAD.value,
                                            is_external=False,
                                        ),
                                    ),
                                    #width="100%",
                                    #padding="0px",
                                    margin_top="20px",
                                ),
                            ),
                            rx.vstack(
                                rx.button(
                                    "Iniciar sesión", 
                                    size="4", 
                                    width="100%",
                                    type="submit",
                                    margin_top="30px",
                                    on_click=LoginState.on_click_boton_submit(boton="inicio_sesión"),
                                ),
                                rx.link(
                                    rx.text("Olvidé mi contraseña", size='2'),
                                    href=Route.RECUPERAR_CONTRASEÑA.value,
                                    is_external=False,
                                    margin_top="10px",
                                ),
                                rx.button(
                                    "Codigo QR leido", 
                                    id="boton_qr_leido",
                                    name="boton_qr_leido",
                                    size="3", 
                                    width="100%",
                                    type="submit",
                                    on_click=LoginState.on_click_boton_submit(boton="qr_camara"),
                                    display="none",
                                ),
                            align="center",
                            width="100%",
                            ),
                        spacing="1",  
                        align="start",
                        width="100%",
                        ),  
                    on_submit=LoginState.on_submit_inicio_sesion, 
                    ), 
                align="center",
                spacing=styles.Spacing.LARGE.value,
                padding="20px", 
                width="100%",
                ),
            width="100%",
            max_width="480px",
            border_width="2px",
            border_color=styles.Color.BORDER_CARD.value,
            border_radius="14px",  
            margin_x="10px",          
            ),
        width="100%",
        padding_left=["10px", "10px", "10px", "360px"],
        padding_right=["10px", "10px", "10px", "20px"],
        padding_top=["90px", "90px", "90px", "100px",], 
        align="center",
        spacing="0",
        ),
    width="100%",
    align="center",
    spacing="0",
    )

def escaneo_QR() -> rx.Component:
    return rx.cond(
        LoginState.escanear_qr,
        lector_qr(),
    )

def ventana_qr() -> rx.Component:
    return rx.vstack(
        rx.html('''
            <div id="reader" style="width: 300px; margin-top: 20px;"></div>
        '''),
    width="100%",
    align="center",
    margin_top="-10px",
    )


def lector_qr() -> rx.Component:
    return rx.vstack(
        rx.html('''
            <div id="reader" style="width: 300px; margin-top: 20px;"></div>
        '''),
        rx.cond(
            LoginState.escanear_qr,
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
                    var inputUsuario = document.getElementById("usuario");
                    if (inputUsuario) {{
                        inputUsuario.value = "";
                    }}                    
                    const qrReader = new Html5Qrcode("reader");
                    qrReader.start(
                        {{ facingMode: "environment" }},
                        {{ fps: 10, qrbox: 250 }},
                        (decodedText, decodedResult) => {{
                            console.log("Código QR detectado:", decodedText);

                            if (inputUsuario) {{
                                inputUsuario.value = decodedText;
                                console.log("Codigo enviado.");
                            }}
                                
                            var botoBuscar = document.getElementById("boton_qr_leido");
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
            type="button",
            size="4", 
            ),
        ),
    width="100%",
    align="center",
    margin_top="-10px",
    )
        #color="primary", 
      #  size="4", 
   # )

