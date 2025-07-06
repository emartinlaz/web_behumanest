import reflex as rx
from ..routes import Route
from ..componentes.protected import *
from ..db import crud
from ..db.models import Facultativos
import qrcode
from io import BytesIO
import base64
from ..componentes.funciones import *  
from ..componentes.modales import *  
from ..componentes.cabecera import cabecera
from ..componentes.mensajes import *
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles
from unidecode import unidecode



class GestionFacultativoState(ProtectedState):
    facultativos : list [Facultativos] = []
    valor_filtro: str = "Activos"
    #Campo busqueda y paginacion
    filtro: str = ""
    pagina: int = 1
    elementos_por_pagina: int = 15


    @rx.var(cache=True)
    def filtrados(self) -> list[Facultativos]:
        if not self.filtro:
            return self.facultativos
        texto = unidecode(self.filtro.lower())
        def contiene(valor):
            return texto in unidecode(str(valor).lower()) if valor else False
        return [
            i for i in self.facultativos
            if contiene(i.usuario)
            or contiene(i.nombre)
            or contiene(i.apellidos)
            or contiene(i.telefono)
            or contiene(i.fecha_alta)
        ]
        
    @rx.var
    def total_paginas(self) -> int:
        if not self.filtrados:
            return 1  # incluso si es None o lista vacía, devolvemos 1 página
        total = len(self.filtrados)
        return max((total + self.elementos_por_pagina - 1) // self.elementos_por_pagina, 1)

    @rx.var(cache=True)
    def pagina_actual(self) -> list[Facultativos]:
        inicio = (self.pagina - 1) * self.elementos_por_pagina
        fin = inicio + self.elementos_por_pagina
        return self.filtrados[inicio:fin] if self.filtrados else []

    @rx.var
    def sin_resultados(self) -> bool:
        return not self.filtrados

    def pagina_inicial(self):
        self.pagina = 1
            
    def pagina_final(self):
        self.pagina = self.total_paginas
        
    def siguiente_pagina(self):
        if self.pagina < self.total_paginas:
            self.pagina += 1

    def anterior_pagina(self):
        if self.pagina > 1:
            self.pagina -= 1

    def ir_a_pagina(self, nueva_pagina: int):
        self.pagina = nueva_pagina
        
    def load_datos(self):
        if self.valor_filtro == "Activos":
            self.facultativos = crud.get_facultativo_by_activo(activo=True, eliminado=False)
        else:
            self.facultativos = crud.get_facultativo_by_activo(activo=False, eliminado=False)
        for facultativo in self.facultativos:
            if facultativo.fecha_alta: facultativo.fecha_alta = facultativo.fecha_alta.strftime('%d/%m/%y')
            if facultativo.fecha_baja: facultativo.fecha_baja = facultativo.fecha_baja.strftime('%d/%m/%y')

    def init_pagina(self):
        self.filtro = ""
        self.pagina = 1
        if self.token_validado:
            self.load_datos()
        
    def set_valor_filtro(self, value):
        self.valor_filtro = value
        self.pagina = 1
        self.load_datos()
           
    def generar_qr(self, facultativo_seleccionado: Facultativos):
        img = qrcode.make(facultativo_seleccionado.usuario)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        qr_base64 = f"data:image/png;base64,{img_str}"
        return ModalState.abrir_modal_gest_facul_qr(usuario=facultativo_seleccionado.usuario, qr=qr_base64)
        
    def set_filtro(self, value):
        self.filtro = value
        self.pagina = 1

    def limpiar_filtro(self):
        self.filtro = ""    

@rx.page(route=Route.GESTION_FACULTATIVOS.value,title='Gestionar Facultativos', on_load=GestionFacultativoState.init_pagina)
@admin_requerido  #Dejará continuar sólo si eres admin (en base al get sesion token consultado)
def gestion_facultativos() -> rx.Component: 
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Gestión de facultativos", mostrar_link_area_privada=True),
            rx.cond(
                GestionFacultativoState.valor_filtro == "Activos",
                tabla_activos(),  
                tabla_no_activos(),
            ),  
            modales_gestion_facultativos(),
            controles_paginacion(),
            script_impresion(),
        width="100%",
        padding_left=["5px", "5px", "5px", "360px"],
        padding_right=["5px", "5px", "5px", "20px"],
        padding_top=["90px", "90px", "90px", "100px"], 
        align="center",
        spacing="0",
        ),
    align="center",
    width="100%",  
    spacing="0",
    on_mount=ProtectedState.comprobar_sesion_caducada,
    )

def script_impresion():
    return rx.script("""
                var style = document.createElement("style");
                style.innerHTML = `
                @media print {
                body * {
                    visibility: hidden;
                    margin: 0;
                    padding: 0;
                }
                .qrprint, .qrprint * {
                    visibility: visible;
                }
                .qrprint {
                    position: fixed;
                    top: 0;
                    left: 20mm;
                    width: 30mm;
                    height: 40mm;
                    text-align: center;
                    font-size: 10pt;
                    margin: 0;
                    padding: 0;
                }
                .qrprint img {
                    width: 100%;
                    height: auto;
                }
                }`;
                document.head.appendChild(style);
            """)

def carga_fila_activos(facultativo: Facultativos):
    return rx.table.row(
        rx.table.cell(
            rx.image(
                    src="/Editar_1.png",
                    height="30px",
                    min_width="30px",   
                    min_height="30px",  
                    object_fit="contain", 
                    cursor="pointer",
                    on_click=lambda:  ModalState.abrir_modal_edicion_facultativo(facultativo=facultativo, origen="edicion_facultativo"),
                    title="Editar facultativo",
                ),
        width="50px",
        align="center",
        padding_y="0px",
        ),
        rx.table.cell(
            rx.box(
                rx.text(facultativo.usuario),
                flex="1",  
                padding_x="5px",
            ),
            padding_y="0px",
            vertical_align="middle",
        ),
        rx.table.cell(
            rx.box(
                rx.text(facultativo.nombre, white_space="nowrap",),
                flex="1",
                padding_x="5px",
            ),
            padding_y="0px",
            vertical_align="middle",
        ),
        rx.table.cell(
            rx.box(
                rx.text(facultativo.apellidos, white_space="nowrap",),
                flex="1",
                padding_x="5px",
            ),
            padding_y="0px",
            vertical_align="middle",
        ),
        rx.table.cell(
            rx.box(
                rx.text(facultativo.telefono),
                flex="1",
                padding_x="5px",
            ),
            padding_y="0px",
            vertical_align="middle",
        ),
        rx.table.cell(
            rx.box(
                rx.text(facultativo.fecha_alta),
                flex="1",
                padding_x="5px",
            ),
            padding_y="0px",
            vertical_align="middle",
        ),
        rx.table.cell(
            rx.image(
                    src="/QR.jpg",
                    height="30px",
                    min_width="30px",   
                    min_height="30px",  
                    object_fit="contain",  
                    cursor="pointer",
                    on_click=lambda: GestionFacultativoState.generar_qr(facultativo),
                    title="Generar QR usuario",
                ),
        width="auto",
        max_width="40px",
        padding_x="10px",
        padding_y="5px",
        ),
        rx.table.cell(
            rx.image(
                    src="/switch_on_2.png",
                    width="40px",
                    height="30px",
                    min_width="40px",   
                    min_height="30px",  
                    object_fit="contain", 
                    cursor="pointer",
                    on_click=lambda: ModalState.abrir_modal_confirmacion_si_no(titulo="Confirmación desactivación",
                                                                               mensaje_1=f"¿Desea desactivar al facultativo: {facultativo.usuario}?",
                                                                               origen="desactivar_facultativo",
                                                                               facultativo=facultativo,),
                    title="Desactivar facultativo",
                ),
        width="auto",
        max_width="40px",
        padding_x="10px",
        padding_y="0px",
        ),
    align="center",
    )
            
def tabla_activos() -> rx.Component:
    return rx.card(
        rx.vstack(
            cabera_tabla(),
            rx.box(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                        rx.table.column_header_cell(
                            rx.image(
                                src="/add_3.png",
                                height="28px",
                                min_width="28px",   
                                min_height="28px",  
                                object_fit="contain", 
                                cursor="pointer",
                                on_click=ModalState.abrir_modal_añadir_facultativo(origen="add_facultativo"),
                                title="Añadir facultativo",
                                margin_left="-5px",
                            ),     
                        align="center", 
                        width="60px",             
                        ),
                        rx.table.column_header_cell(rx.text("Usuario"),),
                        rx.table.column_header_cell(rx.text("Nombre"),),
                        rx.table.column_header_cell(rx.text("Apellidos"),),
                        rx.table.column_header_cell(rx.text("Teléfono")),
                        rx.table.column_header_cell(rx.text("Fecha Alta"),),
                        rx.table.column_header_cell(rx.text("QR"),),
                        rx.table.column_header_cell(rx.text("Activo"),),     
                        ),    
                    ),
                    rx.table.body(
                        rx.foreach(
                            GestionFacultativoState.pagina_actual,
                            lambda i: carga_fila_activos(i)
                        )
                    ),
                width="100%",    
                ),
            width="100%",
            overflow_x="auto",
            ),
        align="center",
        width="100%",
        ),
    width="100%",
    max_width="1400px",
    border_width="2px",
    border_color=styles.Color.BORDER_CARD.value,
    border_radius="14px",  
    margin_x="5px", 
    )
      
      
def carga_fila_no_activos(facultativo: Facultativos):
    return rx.table.row(
        rx.table.cell(facultativo.usuario),
        rx.table.cell(facultativo.nombre),
        rx.table.cell(facultativo.apellidos),
        rx.table.cell(facultativo.telefono),
        rx.table.cell(facultativo.fecha_alta),
        rx.table.cell(facultativo.fecha_baja),
        rx.table.cell(
            rx.image(
                src="/switch_off_1.png",
                width="40px",
                height="30px",
                min_width="40px",   
                min_height="30px",  
                object_fit="contain", 
                cursor="pointer",
                on_click=lambda: ModalState.abrir_modal_confirmacion_si_no(titulo="Confirmación activación",
                                                                           mensaje_1=f"¿Desea activar al facultativo: {facultativo.usuario}?",
                                                                           origen="reactivar_facultativo",
                                                                           facultativo=facultativo,),
                title="Reactivar facultativo",
            ),
        width="50px",
        padding_y="5px",
        ),
        rx.table.cell(
            rx.image(
                src="/Eliminar_1.png",
                height="30px",
                min_width="30px",   
                min_height="30px",  
                object_fit="contain",  
                cursor="pointer",
                on_click=lambda: ModalState.abrir_modal_confirmacion_si_no(titulo="Confirmación eliminación",
                                                                           mensaje_1=f"¿Desea eliminar al facultativo:  {facultativo.usuario}?",
                                                                           origen="eliminar_facultativo",
                                                                           facultativo=facultativo,),
                title="Eliminar",
            ),
        width="50px",
        align="center",
        padding_x="10px",
        padding_y="0px",
        ),
    align="center",
    )
            
def tabla_no_activos() -> rx.Component:
    return rx.card(
        rx.vstack(
            cabera_tabla(),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                    rx.table.column_header_cell(rx.text("Usuario"),),
                    rx.table.column_header_cell(rx.text("Nombre"),),
                    rx.table.column_header_cell(rx.text("Apellidos"),),
                    rx.table.column_header_cell(rx.text("Teléfono"),),
                    rx.table.column_header_cell(rx.text("Fecha Alta"),),
                    rx.table.column_header_cell(rx.text("Fecha Baja"),),
                    rx.table.column_header_cell(rx.text("Activo"),),
                    rx.table.column_header_cell(rx.text("Eliminar"),), 
                    ),    
                ),
                rx.table.body(
                    rx.foreach(
                        GestionFacultativoState.pagina_actual,
                        lambda i: carga_fila_no_activos(i)
                    )
                ),
            width="100%",    
            ),   
        align="center",
        width="100%",
        ),
    width="100%",
    max_width="1400px",
    border_width="2px",
    border_color=styles.Color.BORDER_CARD.value,
    border_radius="14px",  
    margin_x="5px", 
    )   
    
def cabera_tabla() -> rx.Component:
    return rx.box(
                rx.box(
                    rx.box(
                        rx.input(
                            id="filtro",
                            name="filtro",
                            placeholder="Buscar...",
                            value=GestionFacultativoState.filtro,
                            on_change=GestionFacultativoState.set_filtro,
                            size="2",
                            width=["130px", "130px", "130px", "220px"],
                            padding_right="2em",
                            debounce_timeout=300,
                            autocomplete="new-password",
                        ),
                        rx.cond(
                            GestionFacultativoState.filtro == "",
                            rx.icon("search", position="absolute", right="4px", top="50%", transform="translateY(-50%)", color="gray"),
                            rx.icon("x", position="absolute", right="4px", top="50%", transform="translateY(-50%)", color="red", cursor="pointer", on_click=GestionFacultativoState.limpiar_filtro),
                        ),
                    position="absolute",
                    left=["5px", "5px", "5px", "10px"],
                    ),
                    rx.center(
                        rx.hstack(
                            rx.text("Facultativos",
                            size="5", 
                            weight="medium"
                            ),
                            rx.select(
                                ["Activos", "No activos"],
                                value=GestionFacultativoState.valor_filtro,
                                on_change=GestionFacultativoState.set_valor_filtro,
                                size="2",
                            ),
                            spacing="3", 
                            align="center",
                        ),
                    width="100%",
                    margin_left=["80px", "80px", "80px", "0px"],
                    ),

                position="relative",
                width="100%",
                ),
            width="100%",
            padding_y="10px",
            )

def controles_paginacion() -> rx.Component:    
    return rx.center(
        rx.hstack(
            rx.text(
                f"Pagina {GestionFacultativoState.pagina} de {GestionFacultativoState.total_paginas}",
            justify="end",
            size="2",
            ),
            rx.hstack(
                rx.icon_button(
                    rx.icon("chevrons-left", size=18),
                    on_click=GestionFacultativoState.pagina_inicial,
                    opacity=rx.cond(
                        GestionFacultativoState.pagina == 1 | GestionFacultativoState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionFacultativoState.pagina == 1 | GestionFacultativoState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionFacultativoState.sin_resultados,
                variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-left", size=18),
                    on_click=GestionFacultativoState.anterior_pagina,
                    opacity=rx.cond(
                        GestionFacultativoState.pagina == 1 | GestionFacultativoState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionFacultativoState.pagina == 1 | GestionFacultativoState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionFacultativoState.sin_resultados,
                variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-right", size=18),
                    on_click=GestionFacultativoState.siguiente_pagina,
                    opacity=rx.cond(
                        GestionFacultativoState.pagina == GestionFacultativoState.total_paginas | GestionFacultativoState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionFacultativoState.pagina == GestionFacultativoState.total_paginas | GestionFacultativoState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionFacultativoState.sin_resultados,
                variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevrons-right", size=18),
                    on_click=GestionFacultativoState.pagina_final,
                    opacity=rx.cond(
                        GestionFacultativoState.pagina == GestionFacultativoState.total_paginas | GestionFacultativoState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionFacultativoState.pagina == GestionFacultativoState.total_paginas | GestionFacultativoState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionFacultativoState.sin_resultados,
                variant="soft",
                ),
                align="center",
                spacing="2",
                justify="end",
            ),
        spacing="5",
        align="center",
        width="100%",
        justify="end",
        margin_right="10px",
        margin_top="10px",
        ),
    max_width="1400px",
    width="100%",   
    )

