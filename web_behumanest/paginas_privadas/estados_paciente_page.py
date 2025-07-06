import reflex as rx
from ..routes import Route
from ..componentes.protected import *
from ..componentes.modales import *
from ..db import crud
from ..db.models import EstadosPaciente
from ..styles.colors import Color
from ..componentes.cabecera import cabecera
from ..componentes.menu_lateral import menu_lateral
from ..styles import styles

debug = False


class EstadosPacienteState(ProtectedState):
    estados_paciente : list [EstadosPaciente] = []

    def init_pagina(self):
        if self.token_validado:
            self.load_datos()
            
    def load_datos(self):
        self.estados_paciente = crud.get_estados_paciente()
           
    def bajar_una_posicion(self, estado_paciente_seleccionado: EstadosPaciente): #  orden_actual: int):
        try:
            numero_items = len(self.estados_paciente)
            if estado_paciente_seleccionado.orden < numero_items:
                self.estados_paciente[estado_paciente_seleccionado.orden-1].orden += 1
                self.estados_paciente[estado_paciente_seleccionado.orden].orden -= 1  
            for estado in self.estados_paciente:
                crud.update_estado_paciente_by_id(
                    id_estado=estado.id_estado,
                    orden=estado.orden
                    )
                if debug: print(f"Estado: {estado.descripcion_estado}  orden: {estado.orden}")
            self.load_datos()
        except:
            print("Error al ordenar")
        
    def subir_una_posicion(self, estado_paciente_seleccionado: EstadosPaciente): #  orden_actual: int):
        try:
            if estado_paciente_seleccionado.orden > 1:
                self.estados_paciente[estado_paciente_seleccionado.orden-1].orden -= 1
                self.estados_paciente[estado_paciente_seleccionado.orden-2].orden += 1  
            for estado in self.estados_paciente:
                crud.update_estado_paciente_by_id(
                    id_estado=estado.id_estado,
                    orden=estado.orden
                    )
                if debug: print(f"Estado: {estado.descripcion_estado}  orden: {estado.orden}")
            self.load_datos()
        except:
            print("Error al ordenar")
        
        
        
        
@rx.page(route=Route.ESTADOS_PACIENTES.value,title='Estados Paciente', on_load=EstadosPacienteState.init_pagina)
@admin_requerido  #Dejará continuar sólo si eres admin (en base al get sesion token consultado)
def estados_paciente() -> rx.Component: 
    return rx.hstack(
        menu_lateral(),
        rx.vstack(
            cabecera(titulo="Estados paciente", mostrar_link_area_privada=True),
            tabla_estados_paciente(),   
            modales_estados_paciente(),     
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
    
def carga_fila_estado(estado_paciente: EstadosPaciente):
    return rx.table.row(
        rx.table.cell(
            rx.image(
                src="/Editar_1.png",
                height="30px",
                min_width="30px",   
                min_height="30px",  
                object_fit="contain",
                cursor="pointer",
                on_click=lambda:  ModalState.abrir_modal_add_edicion_estados_paciente(estado_paciente=estado_paciente, origen="edicion_estados_paciente"),
                title="Editar estado",
            ),
        width="50px",
        align="center",
        padding_y="0px",
        ),
        rx.table.cell(
            rx.text(
                    estado_paciente.descripcion_estado,
                    width="100%",  
                    overflow="hidden",
                    text_overflow="ellipsis",
                    white_space="nowrap", 
                ),
                width="100%",  
                padding_x="10px",
                padding_y="0px",
                vertical_align="middle",
        ),
        rx.table.cell(
            rx.vstack(
                rx.image(
                    src="/flecha_arriba_4.png",
                    height="12px",
                    min_width="30px",   
                    min_height="12px",  
                    object_fit="contain",
                    cursor="pointer",
                    on_click=lambda:  EstadosPacienteState.subir_una_posicion(estado_paciente),
                    title="Subir orden estado",
                ),
                rx.image(
                    src="/flecha_abajo_4.png",
                    height="12px",
                    min_width="30px",   
                    min_height="12px",  
                    object_fit="contain",
                    cursor="pointer",
                    on_click=lambda:  EstadosPacienteState.bajar_una_posicion(estado_paciente),
                    title="Bajar orden estado",
                margin_top="-10px",
                ),
            margin_top="5px",
            align="center",
            ),
        align="center",
        padding_x="10px",
        padding_y="0px",
        ),
        rx.table.cell(
            rx.image(
                src="/Eliminar_1.png",
                height="30px",
                min_width="30px",   
                min_height="30px",  
                object_fit="contain",  
                cursor="pointer",
                #on_click=lambda:  EstadosPacienteState.abrir_modal_eliminar(estado_paciente),
                on_click=lambda:  ModalState.abrir_modal_confirmacion_si_no(
                    titulo="Confirmación de eliminación", 
                    mensaje_1=f"¿Desea eliminar el estado: {estado_paciente.descripcion_estado}?",
                    origen="eliminar_estado_paciente",
                    estado_paciente=estado_paciente,
                    ),
                title="Eliminar",
            ),
        align="center",
        padding_x="10px",
        padding_y="0px",
        ),
    align="center",
    )
            
def tabla_estados_paciente() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(
                "Listado de estados del paciente",
                size="5",
                width="auto",
                weight="medium", 
                margin_top="20px",
            ),
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
                            #on_click=EstadosPacienteState.abrir_modal_añadir,
                            on_click=ModalState.abrir_modal_add_edicion_estados_paciente(origen="add_estado_paciente"),
                            title="Añadir estado",
                            margin_left="-5px",
                        ),    
                    align="center", 
                    width="60px",                     
                    ),
                    rx.table.column_header_cell(rx.text("Descripción estado"),width="250px"),
                    rx.table.column_header_cell(rx.text("Orden"),),
                    rx.table.column_header_cell(rx.text("Eliminar"),),     
                    ),    
                ),
                rx.table.body(
                    rx.foreach(
                        EstadosPacienteState.estados_paciente, carga_fila_estado
                    )
                ),
            width="100%",    
            ),
        align="center",
        width="100%",
        ),
    width="100%",
    max_width="500px",
    border_width="2px",
    border_color=styles.Color.BORDER_CARD.value,
    border_radius="14px",  
    margin_x="5px", 
    ),     
    
