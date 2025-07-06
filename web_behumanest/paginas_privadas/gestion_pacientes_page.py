import reflex as rx
from ..routes import Route
from ..db import crud
from datetime import date
from ..db.models import Pacientes
from ..componentes.funciones import * 
from ..componentes.protected import *
from ..componentes.modales import * 
from ..componentes.mensajes import *
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..componentes.modales import *
from ..styles import styles
from unidecode import unidecode



class GestionPacienteState(ProtectedState):
    pacientes : list [Pacientes] = []
    valor_filtro: str = "Activos"
    refrescar_datos: bool = False
    #Campo busqueda y paginacion
    filtro: str = ""
    pagina: int = 1
    elementos_por_pagina: int = 15


    @rx.var(cache=True)
    def filtrados(self) -> list[Pacientes]:
        if not self.filtro:
            return self.pacientes
        texto = unidecode(self.filtro.lower())
        def contiene(valor):
            return texto in unidecode(str(valor).lower()) if valor else False
        return [
            i for i in self.pacientes
            if contiene(i.usuario)
            or contiene(i.nombre)
            or contiene(i.apellidos)
            or contiene(i.email_paciente)
            or contiene(i.telefono_paciente)
            or contiene(i.fecha_alta)
        ]
        
    @rx.var
    def total_paginas(self) -> int:
        if not self.filtrados:
            return 1  # incluso si es None o lista vacía, devolvemos 1 página
        total = len(self.filtrados)
        return max(1, (total + self.elementos_por_pagina - 1) // self.elementos_por_pagina)

    @rx.var(cache=True)
    def pagina_actual(self) -> list[Pacientes]:
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
        
    def load_datos(self) -> bool:
        if self.valor_filtro == "Activos":
            self.pacientes = crud.get_pacientes_by_activo(activo=True, eliminado=False)
        else:
            self.pacientes = crud.get_pacientes_by_activo(activo=False, eliminado=False)
        for paciente in self.pacientes:
            if paciente.fecha_alta: paciente.fecha_alta = paciente.fecha_alta.strftime('%d/%m/%y')
            if paciente.fecha_baja: paciente.fecha_baja = paciente.fecha_baja.strftime('%d/%m/%y')

    def init_pagina(self):
        self.filtro = ""
        self.pagina = 1
        if self.token_validado:
            self.load_datos()
        
    def set_valor_filtro(self, value):
        self.valor_filtro = value
        self.pagina = 1
        self.load_datos()
           
    '''
    def detectar_enter_añadir_paciente_usuario(self, key):
        if key == "Enter":
            return rx.set_focus("nombre")
    '''

    def set_filtro(self, value):
        self.filtro = value
        self.pagina = 1

    def limpiar_filtro(self):
        self.filtro = ""  


@rx.page(route=Route.GESTION_PACIENTES.value,title='Gestionar pacientes', on_load=GestionPacienteState.init_pagina)
@facultativo_requerido  #Dejará continuar sólo si eres admin (en base al get sesion token consultado)
def gestion_pacientes() -> rx.Component: 
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Gestión de pacientes", mostrar_link_area_privada=True),
            rx.cond(
                GestionPacienteState.valor_filtro == "Activos",
                tabla_activos(),  
                tabla_no_activos(),
            ),
            controles_paginacion(),
            modales_gestion_pacientes(),
        width="100%",
        padding_left=["5px", "5px", "5px", "360px"],
        padding_right=["5px", "5px", "5px", "20px"],
        padding_top=["90px", "90px", "90px", "100px",], 
        align="center",
        spacing="0",
        ),
    align="center",
    width="100%",  
    spacing="0",
    on_mount=ProtectedState.comprobar_sesion_caducada,
    )

def carga_fila_activos(paciente: Pacientes):
    return rx.table.row(
        rx.table.cell(
            rx.image(
                    src="/Editar_1.png",
                    height="30px",
                    min_width="30px",   
                    min_height="30px",  
                    object_fit="contain", 
                    cursor="pointer",
                    on_click=lambda: ModalState.abrir_modal_edicion_paciente(paciente=paciente, origen="edicion_paciente"),
                    title="Editar paciente", 
                ),
        width="50px",
        align="center",
        padding_y="0px",
        ),
        rx.table.cell(rx.text(paciente.usuario), padding_y="0px"),
        rx.table.cell(rx.text(paciente.nombre, white_space="nowrap"), padding_y="0px"),
        rx.table.cell(rx.text(paciente.apellidos, white_space="nowrap"), padding_y="0px"),
        rx.table.cell(rx.text(paciente.email_paciente), padding_y="0px"),
        rx.table.cell(rx.text(paciente.telefono_paciente), padding_y="0px"),
        rx.table.cell(rx.text(paciente.fecha_alta), padding_y="0px"),
        rx.table.cell(
            rx.cond(
                paciente.contacto_valido,
                rx.image(
                        src="/check_ok_4.png",
                        height="30px",
                        min_width="30px",   
                        min_height="30px",  
                        object_fit="contain", 
                        title="Contactos del paciente válidos", 
                    ),
                rx.image(
                        src="/check_error_4.png",
                        height="30px",
                        min_width="30px",   
                        min_height="30px",  
                        object_fit="contain", 
                        title="Contactos del paciente válidos", 
                    ),
            ),
        width="50px",
        padding_y="0px",
        align="center",
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
                                                                               mensaje_1=f"¿Desea desactivar al paciente: {paciente.usuario}?",
                                                                               origen="desactivar_paciente",
                                                                               paciente=paciente,),

                    title="Desactivar paciente",
                ),
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
                                    on_click=ModalState.abrir_modal_añadir_paciente("gestion_pacientes"),
                                    title="Añadir paciente",
                                    margin_left="-5px",
                                ), 
                            align="center", 
                            width="60px",
                            ),
                            rx.table.column_header_cell(rx.text("Usuario"),),
                            rx.table.column_header_cell(rx.text("Nombre"),),
                            rx.table.column_header_cell(rx.text("Apellidos"),),
                            rx.table.column_header_cell(rx.text("Email"),),
                            rx.table.column_header_cell(rx.text("Teléfono"),),
                            rx.table.column_header_cell(rx.text("Fecha Alta"),),
                            rx.table.column_header_cell(rx.text("Contacto válido", line_height="1",),align="center", width="60px", margin_right="40px",),
                            rx.table.column_header_cell(rx.text("Activo"),),     
                        ),    
                    ),
                    rx.table.body(
                        rx.foreach(
                            GestionPacienteState.pagina_actual,
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
      
      
def carga_fila_no_activos(paciente: Pacientes):
    return rx.table.row(
        rx.table.cell(rx.text(paciente. usuario, margin_top="10px",)),
        rx.table.cell(rx.text(paciente.nombre, margin_top="10px",)),
        rx.table.cell(rx.text(paciente.apellidos, margin_top="10px",)),
        rx.table.cell(rx.text(paciente.fecha_alta, margin_top="10px",)),
        rx.table.cell(rx.text(paciente.fecha_baja, margin_top="10px",)),
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
                                                                           mensaje_1=f"¿Desea activar al paciente: {paciente.usuario}?",
                                                                           origen="reactivar_paciente",
                                                                           paciente=paciente,),
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
                                                                           mensaje_1=f"¿Desea eliminar al paciente:  {paciente.usuario}?",
                                                                           origen="eliminar_paciente",
                                                                           paciente=paciente,),
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
            rx.box(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                        rx.table.column_header_cell(rx.text("Usuario"),),
                        rx.table.column_header_cell(rx.text("Nombre"),),
                        rx.table.column_header_cell(rx.text("Apellidos"),),
                        rx.table.column_header_cell(rx.text("Fecha Alta"),),
                        rx.table.column_header_cell(rx.text("Fecha Baja"),),
                        rx.table.column_header_cell(rx.text("Activo"),),
                        rx.table.column_header_cell(rx.text("Eliminar"),), 
                        ),    
                    ),
                    rx.table.body(
                        rx.foreach(
                            GestionPacienteState.pagina_actual,
                            lambda i: carga_fila_no_activos(i)
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
       
def cabera_tabla() -> rx.Component:
    return rx.box(
                rx.box(
                    rx.box(
                        rx.input(
                            id="filtro",
                            name="filtro",
                            placeholder="Buscar...",
                            value=GestionPacienteState.filtro,
                            on_change=GestionPacienteState.set_filtro,
                            size="2",
                            width=["130px", "130px", "130px", "220px"],
                            padding_right="2em",
                            autocomplete="new-password",
                        ),
                        rx.cond(
                            GestionPacienteState.filtro == "",
                            rx.icon("search", position="absolute", right="4px", top="50%", transform="translateY(-50%)", color="gray"),
                            rx.icon("x", position="absolute", right="4px", top="50%", transform="translateY(-50%)", color="red", cursor="pointer", on_click=GestionPacienteState.limpiar_filtro),
                        ),
                    position="absolute",
                    left=["5px", "5px", "5px", "10px"],
                    ),
                    rx.center(
                        rx.hstack(
                            rx.text("Pacientes", size="5", weight="medium"),
                            rx.select(
                                ["Activos", "No activos"],
                                value=GestionPacienteState.valor_filtro,
                                on_change=GestionPacienteState.set_valor_filtro,
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
                f"Pagina {GestionPacienteState.pagina} de {GestionPacienteState.total_paginas}",
            justify="end",
            size="2",
            ),
            rx.hstack(
                rx.icon_button(
                    rx.icon("chevrons-left", size=18),
                    on_click=GestionPacienteState.pagina_inicial,
                    opacity=rx.cond(
                        GestionPacienteState.pagina == 1 | GestionPacienteState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionPacienteState.pagina == 1 | GestionPacienteState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionPacienteState.sin_resultados,
                variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-left", size=18),
                    on_click=GestionPacienteState.anterior_pagina,
                    opacity=rx.cond(
                        GestionPacienteState.pagina == 1 | GestionPacienteState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionPacienteState.pagina == 1 | GestionPacienteState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionPacienteState.sin_resultados,
                variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevron-right", size=18),
                    on_click=GestionPacienteState.siguiente_pagina,
                    opacity=rx.cond(
                        GestionPacienteState.pagina == GestionPacienteState.total_paginas | GestionPacienteState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionPacienteState.pagina == GestionPacienteState.total_paginas | GestionPacienteState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionPacienteState.sin_resultados,
                variant="soft",
                ),
                rx.icon_button(
                    rx.icon("chevrons-right", size=18),
                    on_click=GestionPacienteState.pagina_final,
                    opacity=rx.cond(
                        GestionPacienteState.pagina == GestionPacienteState.total_paginas | GestionPacienteState.sin_resultados,
                        0.6,
                        1
                    ),
                    color_scheme=rx.cond(
                        GestionPacienteState.pagina == GestionPacienteState.total_paginas | GestionPacienteState.sin_resultados,
                        "gray",
                        "accent"
                    ),
                is_disabled=GestionPacienteState.sin_resultados,
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
           
