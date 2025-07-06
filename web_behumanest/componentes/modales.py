import reflex as rx
from ..db import crud
from ..db.models import EstadosPaciente
from .funciones import * 
from .protected import *
from ..componentes.mensajes import *
from datetime import date



class ModalState(ProtectedState):
    boton_on_submit: str = ""
    #Facultativo
    facultativo_id = ""
    facultativo_usuario = ""
    facultativo_nombre = ""
    facultativo_apellidos = ""
    facultativo_telefono = ""
    #Paciente
    paciente_id = ""
    paciente_usuario = ""
    paciente_nombre = ""
    paciente_apellidos = ""
    paciente_email = ""
    paciente_telefono = ""
    #Estados paciente
    estado_paciente_id = ""
    estado_paciente_descripcion = ""
    #MODALES...
    #Modal info
    origen_modal_info: str = ""
    titulo_info: str = ""
    mensaje_info_1: str = ""
    mensaje_info_2: str = ""
    modal_info_abierto: bool = False
    #Modal añadir paciente    
    origen_modal_añadir_paciente: str = ""
    mensaje_error_añadir_paciente: str = ""
    modal_añadir_paciente_abierto: bool = False
    #Modal edicion paciente
    origen_modal_edicion_paciente: str = ""
    mensaje_error_edicion_paciente: str = ""
    modal_edicion_paciente_abierto: bool = False
    #Modal cambio contraseña sin actual
    origen_modal_cambio_contraseña_inicial: str = ""
    mensaje_error_cambio_contraseña_inicial: str = ""
    mensaje_informacion_cambio_contraseña_inicial_1: str = ""
    mensaje_informacion_cambio_contraseña_inicial_2: str = ""
    modal_cambio_contraseña_inicial_abierto: bool = False
    #Modal cambio contraseña con actual
    origen_modal_cambio_contraseña: str = ""
    mensaje_error_cambio_contraseña: str = ""
    mensaje_informacion_cambio_contraseña: str = ""
    modal_cambio_contraseña_abierto: bool = False
    #Modal confirmacion si no
    origen_modal_confirmacion_si_no: str = ""
    titulo_confirmacion: str = ""
    mensaje_confirmacion_1: str = ""
    mensaje_confirmacion_2: str = ""
    modal_confirmar_si_no_abierto: bool = False
    #Modal add-edicion estados paciente
    origen_modal_add_edicion_estados_paciente: str = ""
    titulo_add_edicion_estados_paciente: str = ""
    mensaje_error_add_edicion_estados_paciente: str = ""
    modal_add_edicion_estados_paciente_abierto: bool = False
    #Modal confirmar envio comnicación
    origen_modal_confirmar_envio_comunicacion: str = ""
    confirmar_envio_id_paciente: int = 0
    confirmar_envio_observaciones: str = ""
    confirmar_envio_usuario: str = ""
    confirmar_envio_nuevo_estado: str = ""
    confirmar_envio_email_contacto: str = ""
    confirmar_envio_telefono_contacto: str = ""
    modal_confirmar_envio_comunicacion_abierto: bool = False
    #Modal gestion facultativos QR
    origen_modal_gest_facul_QR: str = ""
    gest_facul_usuario: str = ""
    qr_base64: str = ""
    modal_gest_facul_QR_abierto: bool = False    
    #Modal añadir facultativo
    origen_modal_añadir_facultativo: str = ""
    titulo_añadir_facultativo: str = ""
    mensaje_error_añadir_facultativo: str = ""
    modal_añadir_facultativo_abierto: bool = False
    #Modal edicion facultativo
    origen_modal_edicion_facultativo: str = ""
    mensaje_error_edicion_facultativo: str = ""
    modal_edicion_facultativo_abierto: bool = False
    #Modal confirmar envio pruebas
    origen_modal_confirmar_envio_prueba: str = ""
    confirmar_envio_prueba_email: str = ""
    confirmar_envio_prueba_telefono: str = ""
    modal_confirmar_envio_prueba_abierto: bool = False
    #Modal edicion datos paciente
    origen_modal_edicion_datos_paciente: str = ""
    mensaje_error_edicion_datos_paciente: str = ""
    modal_edicion_datos_paciente_abierto: bool = False

    
    async def load_datos_gestion_facultativos(self):
        from ..paginas_privadas.gestion_facultativos_page import GestionFacultativoState
        gestion_facultativos_state: GestionFacultativoState = await self.get_state(GestionFacultativoState)
        gestion_facultativos_state.load_datos()    
    
    async def load_datos_estados_pacientes(self):
        from ..paginas_privadas.estados_paciente_page import EstadosPacienteState
        estado_paciente_state: EstadosPacienteState = await self.get_state(EstadosPacienteState)
        estado_paciente_state.load_datos()
    
    async def load_datos_gestion_pacientes(self):
        from ..paginas_privadas.gestion_pacientes_page import GestionPacienteState
        gestion_paciente_state: GestionPacienteState = await self.get_state(GestionPacienteState)
        gestion_paciente_state.load_datos() 

    async def oculta_boton_envio_comunicacon_prueba(self):
        from ..paginas_privadas.paciente_page import PacienteState
        paciente_state: PacienteState = await self.get_state(PacienteState)
        paciente_state.ocultar_boton_pruebas()
    
    def set_facultativo(self, facultativo: Facultativos):
        self.facultativo_id = str(facultativo.id_facultativo)
        self.facultativo_usuario = facultativo.usuario
        self.facultativo_nombre = facultativo.nombre
        self.facultativo_apellidos = facultativo.apellidos
        self.facultativo_telefono = opcionalstr_to_str(facultativo.telefono)
    
    def set_paciente(self, paciente: Pacientes):
        self.paciente_id = str(paciente.id_paciente)
        self.paciente_usuario = paciente.usuario
        self.paciente_nombre = paciente.nombre
        self.paciente_apellidos = paciente.apellidos
        self.paciente_email = opcionalstr_to_str(paciente.email_paciente)
        self.paciente_telefono = opcionalstr_to_str(paciente.telefono_paciente)

    def set_estado_paciente(self, estado_paciente: EstadosPaciente):
        self.estado_paciente_id = str(estado_paciente.id_estado)
        self.estado_paciente_descripcion = estado_paciente.descripcion_estado
    
    def reset_facultativo(self):
        self.facultativo_id = ""
        self.facultativo_usuario = ""
        self.facultativo_nombre = ""
        self.facultativo_apellidos = ""
        self.facultativo_telefono = ""
    
    def reset_paciente(self):
        self.paciente_id = ""
        self.paciente_usuario = ""
        self.paciente_nombre = ""
        self.paciente_apellidos = ""
        self.paciente_email = ""
        self.paciente_telefono = ""

    def reset_estado_paciente(self):
        self.estado_paciente_id = ""
        self.estado_paciente_descripcion = ""
    
    def sacar_facultativo_papelera(self, 
                                   id_facultativo: int,
                                   usuario: str,
                                   nombre: str,
                                   apellidos: str,
                                   telefono: str,
                                   ):
        crud.update_eliminar_facultativo_by_id(id_facultativo=id_facultativo, eliminado=False)
        crud.update_activo_facultativo_by_id(id_facultativo=id_facultativo, activo=True)
        crud.update_facultativo_by_id(
            id_facultativo=id_facultativo,
            usuario=usuario,
            nombre=nombre,
            apellidos=apellidos,
            telefono=str_to_opcionalstr(telefono),
        )
        contraseña=get_nueva_contraseña(longitud=6) 
        crud.update_contraseña_facultativo_by_id(
            id_facultativo=id_facultativo,
            contraseña=contraseña,
            cambiar_contraseña=True,
        ) 
        if ENVIAR_MENSAJES: 
            self.enviar_contraseña(email=usuario,
                                   telefono=telefono,
                                   contraseña=contraseña)
        else:
            print(contraseña)
            
    def sacar_paciente_papelera(self, 
                                   id_paciente: int,
                                   usuario: str,
                                   nombre: str,
                                   apellidos: str,
                                   email: str,
                                   telefono: str,
                                   ):
        crud.update_eliminar_paciente_by_id(id_paciente=id_paciente, eliminado=False)
        crud.update_activo_paciente_by_id(id_paciente=id_paciente, activo=True)
        crud.update_paciente_by_id(
            id_paciente=id_paciente,
            usuario=usuario,
            nombre=nombre,
            apellidos=apellidos,
            email_paciente=str_to_opcionalstr(email),
            telefono_paciente=str_to_opcionalstr(telefono),
        )
        contraseña=get_nueva_contraseña(longitud=6) 
        crud.update_contraseña_paciente_by_id(
            id_paciente=id_paciente,
            contraseña=contraseña,
            cambiar_contraseña=True,
        ) 
        if ENVIAR_MENSAJES: 
            self.enviar_contraseña(email=email,
                                   telefono=telefono,
                                   contraseña=contraseña)
        else:
            print(contraseña)
    
    def enviar_contraseña(self, email: str, telefono: str, contraseña: str):
        mensaje_a_enviar_email = get_mensaje_email_envio_contraseña(contraseña=contraseña)
        mensaje_a_enviar_sms = get_mensaje_sms_envio_contraseña(contraseña=contraseña)
        if is_valid_email(email, permitir_nulo=False):
            enviar_email(
                destinatario=email,
                asunto="Acceso a Behumanest",
                mensaje_a_enviar=mensaje_a_enviar_email
                )
        if is_valid_telefono(telefono, permitir_nulo=False):
            enviar_sms(
                destinatario=telefono,
                mensaje_a_enviar=mensaje_a_enviar_sms,                
            )
            
    def generar_nueva_contraseña_facultativo(self):
        contraseña=get_nueva_contraseña(longitud=6) 
        crud.update_facultativo_by_id(
            id_facultativo=self.facultativo_id,
            usuario=self.facultativo_usuario,
            nombre=self.facultativo_nombre,
            apellidos=self.facultativo_apellidos,
            telefono=str_to_opcionalstr(self.facultativo_telefono),
        )
        crud.update_contraseña_facultativo_by_id(
            id_facultativo=self.facultativo_id,
            contraseña=contraseña,
            cambiar_contraseña=True,
        )
        if ENVIAR_MENSAJES: 
            pass
            self.enviar_contraseña(email=self.facultativo_usuario,
                                   telefono=self.facultativo_telefono,
                                   contraseña=contraseña)
        else:
            print(contraseña)   
        self.cerrar_modal_confirmacion_si_no()
        self.abrir_modal_info(titulo="Confirmación nueva contraseña", mensaje_1="La nueva contraseña se ha enviado por email y/o SMS")

    def generar_nueva_contraseña_paciente(self):
        contraseña=get_nueva_contraseña(longitud=6) 
        crud.update_paciente_by_id(
            id_paciente=self.paciente_id,
            usuario=self.paciente_usuario,
            nombre=self.paciente_nombre,
            apellidos=self.paciente_apellidos,
            email_paciente=str_to_opcionalstr(self.paciente_email),
            telefono_paciente=str_to_opcionalstr(self.paciente_telefono),
        )
        crud.update_contraseña_paciente_by_id(
            id_paciente=self.paciente_id,
            contraseña=contraseña,
            cambiar_contraseña=True,
        )
        if ENVIAR_MENSAJES: 
            pass
            self.enviar_contraseña(email=self.paciente_email,
                                   telefono=self.paciente_telefono,
                                   contraseña=contraseña,)
        else:
            print(contraseña)   
        self.cerrar_modal_confirmacion_si_no()
        self.abrir_modal_info(titulo="Confirmación nueva contraseña", mensaje_1="La nueva contraseña se ha enviado por email y/o SMS")        

    async def eliminar_facultativo(self):
        crud.update_eliminar_facultativo_by_id(id_facultativo=self.facultativo_id, eliminado=True)
        self.cerrar_modal_confirmacion_si_no()
        await self.load_datos_gestion_facultativos()
        self.abrir_modal_info(titulo="Confirmación eliminación", mensaje_1="El facultativo ha sido eliminado")

    async def eliminar_paciente(self):
        crud.update_eliminar_paciente_by_id(id_paciente=self.paciente_id, eliminado=True)
        self.cerrar_modal_confirmacion_si_no()
        await self.load_datos_gestion_pacientes()
        self.abrir_modal_info(titulo="Confirmación eliminación", mensaje_1="El paciente ha sido eliminado")
        
        

    #MARK: FUNC MODAL INFO
        
    def abrir_modal_info(self, titulo: str, mensaje_1: str = "", mensaje_2: str = "", origen: str = ""):
        self.origen_modal_info = origen
        self.titulo_info = titulo
        self.mensaje_info_1 = mensaje_1
        self.mensaje_info_2 = mensaje_2
        self.modal_info_abierto = True

    def cerrar_modal_info(self):
        self.modal_info_abierto = False 
        if self.origen_modal_info == "recuperar_contraseña":
            return rx.redirect(Route.LOGIN.value)
        
    #MARK: FUNC MODAL AÑADIR PACIENTE
    
    def abrir_modal_añadir_paciente(self, origen: str):
        self.origen_modal_añadir_paciente = origen
        self.mensaje_error_añadir_paciente = ""
        self.modal_añadir_paciente_abierto = True
        
    def cerrar_modal_añadir_paciente(self):
        self.modal_añadir_paciente_abierto = False
        
    async def on_submit_añadir_paciente(self, form_data: dict):
        #Comprobar las validaciones del formulario
        if not form_data: return
        form_usuario = form_data.get("paciente_usuario", "")
        if not form_usuario or len(form_usuario) < 10:
            self.mensaje_error_añadir_paciente = "El usuario tiene que ser un AR válido" 
            return
        paciente_existente = crud.get_paciente_by_usuario(usuario=form_usuario)
        if paciente_existente and paciente_existente.eliminado == False:
            self.mensaje_error_añadir_paciente = "Ya hay un paciente con ese usuario dado de alta" 
            return 
        form_nombre = form_data.get("paciente_nombre")
        if not form_nombre or  len(form_nombre) < 3:
            self.mensaje_error_añadir_paciente = "El nombre tiene que tener al menos 3 caracteres" 
            return
        form_apellidos = form_data.get("paciente_apellidos")
        if not form_apellidos or  len(form_apellidos) < 3:
            self.mensaje_error_añadir_paciente = "Los apellidos tienen que tener al menos 3 caracteres" 
            return
        form_email = "" if form_data.get("paciente_email") is None else form_data.get("paciente_email") 
        if not is_valid_email(form_email, permitir_nulo=True):
            self.mensaje_error_añadir_paciente = "El email introducido no es correcto" 
            return
        form_telefono = "" if form_data.get("paciente_telefono") is None else form_data.get("paciente_telefono") 
        if not is_valid_telefono(form_telefono, permitir_nulo=True):
            self.mensaje_error_añadir_paciente = "El teléfono introducido no es correcto" 
            return
        #Comprobar si el usuario esta en la papelera
        if paciente_existente and paciente_existente.eliminado == True:
            self.sacar_paciente_papelera(id_paciente=paciente_existente.id_paciente,
                                         usuario=form_usuario,
                                         nombre=form_nombre,
                                         apellidos=form_apellidos,
                                         email=form_email,
                                         telefono=form_telefono,)
            await self.load_datos_gestion_pacientes()
            self.cerrar_modal_añadir_paciente()
            self.abrir_modal_info(titulo="Confirmación alta paciente", mensaje_1="El paciente ya existía y ha sido recuperado de la papelera", mensaje_2="La nueva contraseña se ha enviado por email y/o SMS")
            return
        #No existe el paciente en la base de datos -> añadirlo
        contraseña=get_nueva_contraseña(longitud=6) 
        crud.create_paciente(
            usuario=form_usuario,
            password=contraseña,
            nombre=form_nombre,
            apellidos=form_apellidos,
            email_paciente=str_to_opcionalstr(form_email),
            telefono_paciente=str_to_opcionalstr(form_telefono),
            activo=True,
            contacto_valido=False,
        )
        if ENVIAR_MENSAJES: 
            self.enviar_contraseña(email=form_email,
                                   telefono=form_telefono,
                                   contraseña=contraseña)
        else:
            print(contraseña)
        self.cerrar_modal_añadir_paciente()    
        await self.load_datos_gestion_pacientes()
        self.abrir_modal_info(titulo="Confirmación alta paciente", mensaje_1="El paciente ha sido dado de alta", mensaje_2="La contraseña se ha enviado por email y/o SMS")
        

    #MARK: FUNC MODAL EDICION PACIENTE
    
    def abrir_modal_edicion_paciente(self, paciente: Pacientes = None, origen: str = ""):
        if paciente: 
            self.set_paciente(paciente=paciente)
        else:
            self.reset_paciente()
        self.origen_modal_edicion_paciente = origen
        self.mensaje_error_edicion_paciente = ""
        self.modal_edicion_paciente_abierto = True
        
    def cerrar_modal_edicion_paciente(self):
        self.modal_edicion_paciente_abierto = False
        
    def modal_set_boton_on_submit(self, boton: str):
        self.boton_on_submit = boton
           
    async def on_submit_edicion_paciente(self, form_data: dict):
        #Comprobar las validaciones del formulario
        if not form_data: return
        form_id_paciente = "" if form_data.get("paciente_id") is None else form_data.get("paciente_id")    
        form_usuario = form_data.get("paciente_usuario", "")
        if not form_usuario or len(form_usuario) < 10:
            self.mensaje_error_añadir_paciente = "El usuario tiene que ser un AR válido" 
            return
        #Si ha cambiado el usuario comprobar que no exista el nuevo introducido
        paciente_existente = None
        if form_usuario != self.paciente_usuario:
            paciente_existente = crud.get_paciente_by_usuario(usuario=form_usuario)
            if paciente_existente and paciente_existente.eliminado == False:
                self.mensaje_error_edicion_paciente = "Ya hay un paciente con ese usuario dado de alta" 
                return 
        form_nombre = form_data.get("paciente_nombre")
        if not form_nombre or  len(form_nombre) < 3:
            self.mensaje_error_edicion_paciente = "El nombre tiene que tener al menos 3 caracteres" 
            return
        form_apellidos = form_data.get("paciente_apellidos")
        if not form_apellidos or  len(form_apellidos) < 3:
            self.mensaje_error_edicion_paciente = "Los apellidos tienen que tener al menos 3 caracteres" 
            return
        form_email = "" if form_data.get("paciente_email") is None else form_data.get("paciente_email") 
        if not is_valid_email(form_email, permitir_nulo=True):
            self.mensaje_error_edicion_paciente = "El email introducido no es correcto" 
            return
        form_telefono = "" if form_data.get("paciente_telefono") is None else form_data.get("paciente_telefono") 
        if not is_valid_telefono(form_telefono, permitir_nulo=True):
            self.mensaje_error_edicion_paciente = "El teléfono introducido no es correcto" 
            return
        #Si se ha llamado a on submit desde generar contraseña
        if self.boton_on_submit == "generar_contraseña":
            self.abrir_modal_confirmacion_si_no(titulo="Confirmación generar contraseña",
                                                mensaje_1=f"¿Desea generar una nueva contraseña para el paciente: {self.paciente_usuario}?",
                                                mensaje_2="La contraseña se enviará al email y/o al teléfono de contacto",
                                                origen="generar_contraseña_paciente",)
            return
        #Comprobar si el usuario esta en la papelera
        if paciente_existente and paciente_existente.eliminado == True:
            self.sacar_paciente_papelera(id_paciente=paciente_existente.id_paciente,
                                            usuario=form_usuario,
                                            nombre=form_nombre,
                                            apellidos=form_apellidos,
                                            email=form_email,
                                            telefono=form_telefono,                               
            )
            await self.load_datos_gestion_pacientes()
            self.cerrar_modal_edicion_paciente()
            self.abrir_modal_info(titulo="Confirmación alta paciente", mensaje_1="El paciente ya existía y ha sido recuperado de la papelera", mensaje_2="La nueva contraseña se ha enviado por email y/o SMS")
            return
        #Si no esta en la papelera actualizar datos
        crud.update_paciente_by_id(
                id_paciente=form_id_paciente,
                usuario=form_usuario,
                nombre=form_nombre,
                apellidos=form_apellidos,
                email_paciente=str_to_opcionalstr(form_email),
                telefono_paciente=str_to_opcionalstr(form_telefono),
                ) 
        await self.load_datos_gestion_pacientes()
        self.cerrar_modal_edicion_paciente()
        
                   
    #MARK: FUNC MODAL CONFIRMACION SI NO
    
    def abrir_modal_confirmacion_si_no(self, 
                                       titulo: str, 
                                       mensaje_1: str = "", 
                                       mensaje_2: str = "", 
                                       origen: str = "", 
                                       estado_paciente: EstadosPaciente = None,
                                       facultativo: Facultativos = None,
                                       paciente: Pacientes = None,
                                       ):
        self.origen_modal_confirmacion_si_no = origen
        self.titulo_confirmacion = titulo
        self.mensaje_confirmacion_1 = mensaje_1
        self.mensaje_confirmacion_2 = mensaje_2
        self.modal_confirmar_si_no_abierto = True
        if origen == "eliminar_estado_paciente" and estado_paciente:
            self.set_estado_paciente(estado_paciente=estado_paciente)
        if (origen == "reactivar_facultativo" or origen == "desactivar_facultativo" or origen == "eliminar_facultativo") and facultativo:
            self.set_facultativo(facultativo=facultativo)
        if (origen == "reactivar_paciente" or origen == "desactivar_paciente" or origen == "eliminar_paciente") and paciente:
            self.set_paciente(paciente=paciente)
            
    def cerrar_modal_confirmacion_si_no(self):
        self.modal_confirmar_si_no_abierto = False    

    async def on_click_si_confirmacion(self):
        self.cerrar_modal_confirmacion_si_no()
        match self.origen_modal_confirmacion_si_no:
            case "cambiar_contraseña":
                return self.do_logout()
            case "eliminar_estado_paciente":
                crud.delete_estado_pacientes_by_id(
                    id_estado=self.estado_paciente_id
                )
                await self.load_datos_estados_pacientes()
            case "reactivar_facultativo":
                crud.update_activo_facultativo_by_id(
                    id_facultativo=self.facultativo_id, 
                    activo=True,
                    fecha_alta=date.today(),
                    borrar_fecha_baja=True,
                )
                await self.load_datos_gestion_facultativos()
            case "desactivar_facultativo":
                crud.update_activo_facultativo_by_id(
                    id_facultativo=self.facultativo_id,
                    activo=False,
                    fecha_baja=date.today(),
                )
                await self.load_datos_gestion_facultativos()
            case "generar_contraseña_facultativo": 
                self.generar_nueva_contraseña_facultativo()
            case "eliminar_facultativo": 
                await self.eliminar_facultativo()    
            case "reactivar_paciente":
                crud.update_activo_paciente_by_id(
                    id_paciente=self.paciente_id, 
                    activo=True,
                    fecha_alta=date.today(),
                    borrar_fecha_baja=True,
                )
                await self.load_datos_gestion_pacientes()
            case "desactivar_paciente":
                crud.update_activo_paciente_by_id(
                    id_paciente=self.paciente_id,
                    activo=False,
                    fecha_baja=date.today(),
                )
                await self.load_datos_gestion_pacientes()        
            case "generar_contraseña_paciente": 
                self.generar_nueva_contraseña_paciente()
            case "eliminar_paciente": 
                await self.eliminar_paciente() 

    def on_click_no_confirmacion(self):
        self.cerrar_modal_confirmacion_si_no()

    #MARK: FUNC MODAL CAMBIO CONTRASEÑA INICIAL
        
    def abrir_modal_cambio_contraseña_inicial(self, origen: str = ""):
        self.origen_modal_cambio_contraseña_inicial = origen
        self.mensaje_informacion_cambio_contraseña_inicial_1 = "En el primier inicio de sesión, es necesásero cambiar la contraseña por seguridad."
        self.mensaje_informacion_cambio_contraseña_inicial_2 = "La contraseña debe contener por lo menos 6 carácteres o dígitos"
        self.mensaje_error_cambio_contraseña_inicial = ""
        self.modal_cambio_contraseña_inicial_abierto = True

    def cerrar_modal_cambio_contraseña_inicial(self):
        if (self.facultativo_logueado and self.facultativo_logueado.cambiar_contraseña == True) or (self.paciente_logueado and self.paciente_logueado.cambiar_contraseña == True):
            self.abrir_modal_confirmacion_si_no(titulo="Cancelación cambio contraseña", mensaje_1="Es necesáreo el cambio de contraseña, si cancela será redirigido a la ventana de login", mensaje_2="¿Seguro que desea cancelar?", origen="cambiar_contraseña"),
        else:
            self.modal_cambio_contraseña_inicial_abierto = False
        
        
    def on_submit_cambio_contraseña_inicial(self, form_data: dict):
        #Comprobar las validaciones del formulario
        if not form_data: return
        form_contraseña_nueva_1 = form_data.get("contraseña_nueva_1")
        if not form_contraseña_nueva_1 or len(form_contraseña_nueva_1) < 6:
            self.mensaje_informacion_cambio_contraseña_inicial_1 = ""
            self.mensaje_informacion_cambio_contraseña_inicial_2 = ""
            self.mensaje_error_cambio_contraseña_inicial = "La contraseña tiene que tener al menos 6 caracteres" 
            return        
        form_contraseña_nueva_2 = form_data.get("contraseña_nueva_2")
        if not form_contraseña_nueva_2 or len(form_contraseña_nueva_2) < 6:
            self.mensaje_informacion_cambio_contraseña_inicial_1 = ""
            self.mensaje_informacion_cambio_contraseña_inicial_2 = ""
            self.mensaje_error_cambio_contraseña_inicial = "La contraseña tiene que tener al menos 6 caracteres" 
            return  
        if form_contraseña_nueva_1 != form_contraseña_nueva_2:
            self.mensaje_informacion_cambio_contraseña_inicial_1 = ""
            self.mensaje_informacion_cambio_contraseña_inicial_2 = ""
            self.mensaje_error_cambio_contraseña_inicial = "Las contraseñas no coinicden" 
            return [
                rx.set_value("contraseña_nueva_1", ""),
                rx.set_value("contraseña_nueva_2", ""),
                rx.set_focus("contraseña_nueva_1")
            ]  
        #Todas validaciones son correctas -> guardar la nueva contraseña
        #En caso de ser un facultativo
        if self.facultativo_logueado:
            crud.update_contraseña_facultativo_by_id(
                    id_facultativo=self.facultativo_logueado.id_facultativo,
                    contraseña=form_contraseña_nueva_1,
                    cambiar_contraseña=False,
                    )
            self.facultativo_logueado.cambiar_contraseña = False
        #En caso de ser un paciente    
        elif self.paciente_logueado: 
            crud.update_contraseña_paciente_by_id(
                    id_paciente=self.paciente_logueado.id_paciente,
                    contraseña=form_contraseña_nueva_1,
                    cambiar_contraseña=False,
                    )
            self.paciente_logueado.cambiar_contraseña = False
        self.cerrar_modal_cambio_contraseña_inicial()
        self.abrir_modal_info(titulo="Cambio de contraseña", mensaje_1="La contraseña ha sido modificada correctamente")

    #MARK: FUNC MODAL CAMBIO CONTRASEÑA
        
    def abrir_modal_cambio_contraseña(self, origen: str = ""):
        self.origen_modal_cambio_contraseña = origen
        self.mensaje_informacion_cambio_contraseña = "La contraseña debe contener por lo menos 6 carácteres o dígitos"
        self.mensaje_error_cambio_contraseña = ""
        self.modal_cambio_contraseña_abierto = True

    def cerrar_modal_cambio_contraseña(self):
        self.modal_cambio_contraseña_abierto = False
        
    def on_submit_cambio_contraseña(self, form_data: dict):
        #Comprobar las validaciones del formulario
        if not form_data: return
        form_contraseña_actual = form_data.get("contraseña_actual")
        if not form_contraseña_actual or len(form_contraseña_actual) < 6:
            self.mensaje_informacion_cambio_contraseña = ""
            self.mensaje_error_cambio_contraseña = "La contraseña actual no es correcta"
            return
        if self.facultativo_logueado and self.facultativo_logueado.check_password(form_contraseña_actual) == False:
            self.mensaje_informacion_cambio_contraseña = ""
            self.mensaje_error_cambio_contraseña = "La contraseña actual no es correcta" 
            return [
                rx.set_value("contraseña_actual", ""),
                rx.set_focus("contraseña_actual")   
            ]
        if self.paciente_logueado and self.paciente_logueado.check_password(form_contraseña_actual) == False:
            self.mensaje_informacion_cambio_contraseña = ""
            self.mensaje_error_cambio_contraseña = "La contraseña actual no es correcta" 
            return [
                rx.set_value("contraseña_actual", ""),
                rx.set_focus("contraseña_actual")   
            ]     
        form_contraseña_nueva_1 = form_data.get("contraseña_nueva_1")
        if not form_contraseña_nueva_1 or len(form_contraseña_nueva_1) < 6:
            self.mensaje_informacion_cambio_contraseña = ""
            self.mensaje_error_cambio_contraseña = "La contraseña tiene que tener al menos 6 caracteres" 
            return        
        form_contraseña_nueva_2 = form_data.get("contraseña_nueva_2")
        if not form_contraseña_nueva_2 or len(form_contraseña_nueva_2) < 6:
            self.mensaje_informacion_cambio_contraseña = ""
            self.mensaje_error_cambio_contraseña = "La contraseña tiene que tener al menos 6 caracteres" 
            return  
        if form_contraseña_nueva_1 != form_contraseña_nueva_2:
            self.mensaje_informacion_cambio_contraseña = ""
            self.mensaje_error_cambio_contraseña = "Las contraseñas no coinicden" 
            return [
                rx.set_value("contraseña_nueva_1", ""),
                rx.set_value("contraseña_nueva_2", ""),
                rx.set_focus("contraseña_nueva_1")
            ]  
        #Todas validaciones son correctas -> guardar la nueva contraseña
        #En caso de ser un facultativo
        if self.facultativo_logueado:  
            crud.update_contraseña_facultativo_by_id(
                    id_facultativo=self.facultativo_logueado.id_facultativo,
                    contraseña=form_contraseña_nueva_1,
                    cambiar_contraseña=False,
                    )
            self.facultativo_logueado.cambiar_contraseña = False
        #En caso de ser un paciente    
        if self.paciente_logueado: 
            crud.update_contraseña_paciente_by_id(
                    id_paciente=self.paciente_logueado.id_paciente,
                    contraseña=form_contraseña_nueva_1,
                    cambiar_contraseña=False,
                    )
            self.paciente_logueado.cambiar_contraseña = False
        self.cerrar_modal_cambio_contraseña()
        self.abrir_modal_info(titulo="Cambio de contraseña", mensaje_1="La contraseña ha sido modificada correctamente")
        
        
    #MARK: FUNC MODAL ADD-EDICION ESTADOS PACIENTE
    
    def abrir_modal_add_edicion_estados_paciente(self, estado_paciente: EstadosPaciente = None, origen: str = ""):
        if estado_paciente: 
            self.set_estado_paciente(estado_paciente=estado_paciente)
        else:
            self.reset_estado_paciente()
        self.origen_modal_add_edicion_estados_paciente = origen
        if origen == "add_estado_paciente": self.titulo_add_edicion_estados_paciente = "Añadir estado"
        if origen == "edicion_estados_paciente": self.titulo_add_edicion_estados_paciente = "Editar estado"
        self.mensaje_error_add_edicion_estados_paciente = ""
        self.modal_add_edicion_estados_paciente_abierto = True
        
    def cerrar_modal_add_edicion_estados_paciente(self):
        self.modal_add_edicion_estados_paciente_abierto = False

    async def on_submit_add_edicion_estados_paciente(self, form_data: dict):
        if not form_data: return
        form_descripcion_estado_paciente = form_data.get("descripcion_estado_paciente", "")
        if len(form_descripcion_estado_paciente) < 3:
            self.mensaje_error_add_edicion_estados_paciente = "Introduzca un estado de al menos 3 caracteres"
            return
        if self.origen_modal_add_edicion_estados_paciente == "add_estado_paciente":
            crud.create_estado(descripcion=form_descripcion_estado_paciente)
        if self.origen_modal_add_edicion_estados_paciente == "edicion_estados_paciente":     
            crud.update_estado_paciente_by_id(
                id_estado=self.estado_paciente_id,
                descripcion=form_descripcion_estado_paciente,
                )           
        self.cerrar_modal_add_edicion_estados_paciente()
        from ..paginas_privadas.estados_paciente_page import EstadosPacienteState
        estado_paciente_state: EstadosPacienteState = await self.get_state(EstadosPacienteState)
        estado_paciente_state.load_datos()
        
    #MARK: FUNC MODAL CONFIRMAR ENVIO COMUNICACION
    
    def abrir_modal_confirmacion_envio_comunicacion(self, 
                                                    id_paciente: int,
                                                    usuario: str, 
                                                    nuevo_estado: str, 
                                                    observaciones: str = "", 
                                                    email_contacto: str = "",
                                                    telefono_contacto: str = "",
                                                    origen: str = "",
                                                    ):
        self.confirmar_envio_id_paciente = id_paciente
        self.confirmar_envio_usuario = usuario
        self.confirmar_envio_nuevo_estado = nuevo_estado
        self.confirmar_envio_observaciones = observaciones
        self.confirmar_envio_email_contacto = email_contacto
        self.confirmar_envio_telefono_contacto = telefono_contacto
        self.origen_modal_confirmacion_si_no = origen
        self.modal_confirmar_envio_comunicacion_abierto = True

    def cerrar_modal_confirmacion_envio_comunicacion(self):
        self.modal_confirmar_envio_comunicacion_abierto = False 

    async def on_click_enviar_comunicacion(self):
        nuevo_estado = crud.get_estado_paciente_by_descripcion(self.confirmar_envio_nuevo_estado)
        if nuevo_estado:
            crud.update_estado_actual_paciente_by_id(
                id_paciente=self.confirmar_envio_id_paciente,
                estado_actual=nuevo_estado.id_estado,
            )
        mensaje_a_enviar_email = get_mensaje_email_contacto_paciente(usuario=self.confirmar_envio_usuario, nuevo_estado=self.confirmar_envio_nuevo_estado, observaciones=self.confirmar_envio_observaciones)
        mensaje_a_enviar_sms = get_mensaje_sms_contacto_paciente(usuario=self.confirmar_envio_usuario, nuevo_estado=self.confirmar_envio_nuevo_estado, observaciones=self.confirmar_envio_observaciones)
        if ENVIAR_MENSAJES:
            if is_valid_email(self.confirmar_envio_email_contacto, permitir_nulo=False):
                enviar_email(
                    destinatario=self.confirmar_envio_email_contacto,
                    asunto="Behumanest: actualización estado",
                    mensaje_a_enviar=mensaje_a_enviar_email,
                    )
            if is_valid_telefono(self.confirmar_envio_telefono_contacto, permitir_nulo=False):
                enviar_sms(
                    destinatario=self.confirmar_envio_telefono_contacto,
                    mensaje_a_enviar=mensaje_a_enviar_sms,                
                )
        else:
            print(f"email: {mensaje_a_enviar_email}")
            print(f"sms: {mensaje_a_enviar_sms}")
        self.modal_confirmar_envio_comunicacion_abierto = False
        from ..paginas_privadas.facultativo_page import FacultativoState
        facultativo_state: FacultativoState = await self.get_state(FacultativoState)
        form_data = {
                "ar_paciente": self.confirmar_envio_usuario,
            }
        facultativo_state.buscar_paciente(form_data=form_data)
        self.abrir_modal_info(titulo="Confirmación de envío", mensaje_1="El nuevo estado ha sido comunicado a los contactos del paciente")
        

    def on_click_cancelar_comunicacion(self):
        self.modal_confirmar_envio_comunicacion_abierto = False
        self.abrir_modal_info(titulo="Comunicación cancelada", mensaje_1="La comunicación NO se ha enviado a los contactos del paciente")


    #MARK: FUNC MODAL GESTION FACUL QR
        
    def abrir_modal_gest_facul_qr(self, usuario: str = "", qr: str = ""):
        self.gest_facul_usuario = usuario
        self.qr_base64 = qr
        self.modal_gest_facul_QR_abierto = True

    def cerrar_modal_gest_facul_qr(self):
        self.modal_gest_facul_QR_abierto = False   

    #MARK: FUNC MODAL AÑADIR FACULTATIVO
    
    def abrir_modal_añadir_facultativo(self, facultativo: Facultativos = None, origen: str = ""):
        self.reset_facultativo()
        self.origen_modal_añadir_facultativo = origen
        self.mensaje_error_añadir_facultativo = ""
        self.modal_añadir_facultativo_abierto = True
        
    def cerrar_modal_añadir_facultativo(self):
        self.modal_añadir_facultativo_abierto = False
        
    async def on_submit_añadir_facultativo(self, form_data: dict):
        #Comprobar las validaciones del formulario
        if not form_data: return
        form_usuario = form_data.get("facultativo_usuario", "")
        if not form_usuario or not is_valid_email(form_usuario, permitir_nulo=False):
            self.mensaje_error_añadir_facultativo = "El usuario debe ser un email válido"
            return
        facultativo_existente = crud.get_facultativo_by_usuario(usuario=form_usuario)
        if facultativo_existente and facultativo_existente.eliminado == False:
            self.mensaje_error_añadir_facultativo = "Ya hay un facultativo con ese usuario dado de alta" 
            return 
        form_nombre = form_data.get("facultativo_nombre")
        if not form_nombre or  len(form_nombre) < 3:
            self.mensaje_error_añadir_facultativo = "El nombre tiene que tener al menos 3 caracteres" 
            return
        form_apellidos = form_data.get("facultativo_apellidos")
        if not form_apellidos or  len(form_apellidos) < 3:
            self.mensaje_error_añadir_facultativo = "Los apellidos tienen que tener al menos 3 caracteres" 
            return
        form_telefono = "" if form_data.get("facultativo_telefono") is None else form_data.get("facultativo_telefono") 
        if not is_valid_telefono(form_telefono, permitir_nulo=True):
            self.mensaje_error_añadir_facultativo = "El teléfono introducido no es correcto" 
            return
        #Comprobar si el usuario esta en la papelera
        if facultativo_existente and facultativo_existente.eliminado == True:
            self.sacar_facultativo_papelera(id_facultativo=facultativo_existente.id_facultativo,
                                            usuario=form_usuario,
                                            nombre=form_nombre,
                                            apellidos=form_apellidos,
                                            telefono=form_telefono,                               
            )
            await self.load_datos_gestion_facultativos()
            self.cerrar_modal_añadir_facultativo()
            self.abrir_modal_info(titulo="Confirmación alta facultativo", mensaje_1="El facultativo ya existía y ha sido recuperado de la papelera", mensaje_2="La nueva contraseña se ha enviado por email y/o SMS")
            return
        #No existe el facultativo en la base de datos -> añadirlo
        contraseña=get_nueva_contraseña(longitud=6) 
        crud.create_facultativo(
            usuario=form_usuario,
            password=contraseña,
            nombre=form_nombre,
            apellidos=form_apellidos,
            telefono=str_to_opcionalstr(form_telefono),
            admin=False,
            activo=True,
        )
        if ENVIAR_MENSAJES: 
            pass
            self.enviar_contraseña(email=form_usuario,
                                   telefono=form_telefono,
                                   contraseña=contraseña)
        else:
            print(contraseña)
        self.cerrar_modal_añadir_facultativo()    
        await self.load_datos_gestion_facultativos()
        self.abrir_modal_info(titulo="Confirmación alta facultativo", mensaje_1="El facultativo ha sido dado de alta", mensaje_2="La contraseña se ha enviado por email y/o SMS")

    
    
    #MARK: FUNC MODAL EDICION FACULTATIVO
        
    def abrir_modal_edicion_facultativo(self, facultativo: Facultativos = None, origen: str = ""):
        if facultativo: 
            self.set_facultativo(facultativo=facultativo)
        else:
            self.reset_facultativo()
        self.origen_modal_edicion_facultativo = origen
        self.mensaje_error_edicion_facultativo = ""
        self.modal_edicion_facultativo_abierto = True
        
    def cerrar_modal_edicion_facultativo(self):
        self.modal_edicion_facultativo_abierto = False
        
    async def on_submit_edicion_facultativo(self, form_data: dict):
        #Comprobar las validaciones del formulario
        if not form_data: return
        form_id_facultativo = "" if form_data.get("facultativo_id") is None else form_data.get("facultativo_id")    
        form_usuario = form_data.get("facultativo_usuario", "")
        if not form_usuario or not is_valid_email(form_usuario, permitir_nulo=False):
            self.mensaje_error_edicion_facultativo = "El usuario debe ser un email válido"
            return
        #Si ha cambiado el usuario comprobar que no exista el nuevo introducido
        facultativo_existente = None
        if form_usuario != self.facultativo_usuario:
            facultativo_existente = crud.get_facultativo_by_usuario(usuario=form_usuario)
            if facultativo_existente and facultativo_existente.eliminado == False:
                self.mensaje_error_edicion_facultativo = "Ya hay un facultativo con ese usuario dado de alta" 
                return 
        form_nombre = form_data.get("facultativo_nombre")
        if not form_nombre or  len(form_nombre) < 3:
            self.mensaje_error_edicion_facultativo = "El nombre tiene que tener al menos 3 caracteres" 
            return
        form_apellidos = form_data.get("facultativo_apellidos")
        if not form_apellidos or  len(form_apellidos) < 3:
            self.mensaje_error_edicion_facultativo = "Los apellidos tienen que tener al menos 3 caracteres" 
            return
        form_telefono = "" if form_data.get("facultativo_telefono") is None else form_data.get("facultativo_telefono") 
        if not is_valid_telefono(form_telefono, permitir_nulo=True):
            self.mensaje_error_edicion_facultativo = "El teléfono introducido no es correcto" 
            return
        #Si se ha llamado a on submit desde generar contraseña
        if self.boton_on_submit == "generar_contraseña":
            self.abrir_modal_confirmacion_si_no(titulo="Confirmación generar contraseña",
                                                mensaje_1=f"¿Desea generar una nueva contraseña para el facultativo: {self.facultativo_usuario}?",
                                                mensaje_2="La contraseña se enviará al email y/o al teléfono de contacto",
                                                origen="generar_contraseña_facultativo",)
            return
        #Comprobar si el usuario esta en la papelera
        if facultativo_existente and facultativo_existente.eliminado == True:
            self.sacar_facultativo_papelera(id_facultativo=facultativo_existente.id_facultativo,
                                            usuario=form_usuario,
                                            nombre=form_nombre,
                                            apellidos=form_apellidos,
                                            telefono=form_telefono,                               
            )
            await self.load_datos_gestion_facultativos()
            self.cerrar_modal_edicion_facultativo()
            self.abrir_modal_info(titulo="Confirmación alta facultativo", mensaje_1="El facultativo ya existía y ha sido recuperado de la papelera", mensaje_2="La nueva contraseña se ha enviado por email y/o SMS")
            return
        #Si no esta en la papelera actualizar datos
        crud.update_facultativo_by_id(
                id_facultativo=form_id_facultativo,
                usuario=form_usuario,
                nombre=form_nombre,
                apellidos=form_apellidos,
                telefono=str_to_opcionalstr(form_telefono),
                ) 
        await self.load_datos_gestion_facultativos()
        self.cerrar_modal_edicion_facultativo()


    #MARK: FUNC MODAL CONFIRMAR ENVIO PRUEBA
    
    def abrir_modal_confirmar_envio_prueba(self, email: str = "", telefono = "", origen: str = ""):
        self.origen_modal_confirmar_envio_prueba = origen
        self.confirmar_envio_prueba_email = email
        self.confirmar_envio_prueba_telefono = telefono
        self.modal_confirmar_envio_prueba_abierto = True
        
    def cerrar_modal_confirmar_envio_prueba(self):
        self.modal_confirmar_envio_prueba_abierto = False    
    
    async def on_click_enviar_mensaje_prueba(self):
        if not self.paciente_logueado: return
        envios_pruebas_restantes = crud.update_envios_pruebas_by_id(
            id_paciente=self.paciente_logueado.id_paciente, 
            variacion=-1)
        self.paciente_logueado.envios_pruebas = envios_pruebas_restantes
        mensaje_a_enviar_email = get_mensaje_email_envio_prueba_paciente()
        mensaje_a_enviar_sms = get_mensaje_sms_envio_prueba_paciente()
        if ENVIAR_MENSAJES:
            if is_valid_email(self.confirmar_envio_prueba_email, permitir_nulo=False):
                enviar_email(
                    destinatario=self.confirmar_envio_prueba_email,
                    asunto="Behumanest: prueba de comunicación",
                    mensaje_a_enviar=mensaje_a_enviar_email,
                    )
            if is_valid_telefono(self.confirmar_envio_prueba_telefono, permitir_nulo=False):
                enviar_sms(
                    destinatario=self.confirmar_envio_prueba_telefono,
                    mensaje_a_enviar=mensaje_a_enviar_sms,                
                )
        else:
            print(f"email: {mensaje_a_enviar_email}")
            print(f"sms: {mensaje_a_enviar_sms}")
        await self.oculta_boton_envio_comunicacon_prueba()
        self.cerrar_modal_confirmar_envio_prueba()
        self.abrir_modal_info(titulo="Comunicación de prueba", 
                              mensaje_1="La comunicación de prueba ha sido enviada.", 
                              mensaje_2="Compruebe en los dispositivos de los contactos, que ha recibido la comunicación correctamente. En caso contrario revise los datos de contacto introducidos")         
    
    

def modales_gestion_pacientes():
    return rx.fragment(
        modal_info_2_mensajes(), 
        modal_cambiar_contraseña(),
        modal_añadir_paciente(),      
        modal_edicion_paciente(),
        modal_confirmacion_si_no(),    
    )            
            
def modales_facultativo():
    return rx.fragment(
        modal_info_2_mensajes(),        
        modal_cambiar_contraseña_inicial(),
        modal_cambiar_contraseña(),
        modal_añadir_paciente(),
        modal_confirmacion_si_no(),
        modal_confirmar_envio_comunicacion(),
    )   

def modales_paciente():
    return rx.fragment(
        modal_info_2_mensajes(),        
        modal_cambiar_contraseña_inicial(),
        modal_cambiar_contraseña(),
        modal_confirmacion_si_no(),
        modal_confirmar_envio_prueba(),
        #modal_edicion_datos_paciente(),
    )      
      
def modales_recuperar_contraseña():
    return rx.fragment(
        modal_info_2_mensajes(),        
    )     

def modales_gestion_facultativos():
    return rx.fragment(
        modal_info_2_mensajes(), 
        modal_cambiar_contraseña(),  
        modal_gest_facultativo_QR(),   
        modal_confirmacion_si_no(),
        modal_añadir_facultativo(),
        modal_edicion_facultativo(),
    )          
     
def modales_estados_paciente():
    return rx.fragment(
        modal_info_2_mensajes(), 
        modal_cambiar_contraseña(),  
        modal_add_edicion_estados_paciente(), 
        modal_confirmacion_si_no(),
    )      

    
            
def modal_añadir_paciente():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Añadir paciente"),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_error_añadir_paciente != "",
                            rx.callout(
                                ModalState.mensaje_error_añadir_paciente,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.text(
                            "Usuario",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            name="paciente_usuario",
                            id="paciente_usuario",
                            placeholder="Introduzca el AR del paciente",
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Nombre",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_nombre",
                            id="paciente_nombre",
                            placeholder="Introduzca el nombre",
                            max_length=30,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Apellidos",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_apellidos",
                            id="paciente_apellidos",
                            placeholder="Introduzca los apellidos",
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Email",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_email",
                            id="paciente_email",
                            placeholder="Introduzca el email del paciente",
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Teléfono",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_telefono",
                            id="paciente_telefono",
                            placeholder="Introduzca el teléfono del paciente",
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.hstack(
                    rx.button(
                        "Añadir", 
                        type="submit", 
                        flex="1",
                    ),
                    rx.button(
                        "Cancelar", 
                        type="button", 
                        on_click=ModalState.cerrar_modal_añadir_paciente, 
                        flex="1",
                    ), 
                spacing="4",
                width="100%",
                padding_top = "30px"
                ),
            on_submit=ModalState.on_submit_añadir_paciente,
            ),
        width="100%",    
        max_width="550px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"],
        ),
    open=ModalState.modal_añadir_paciente_abierto
    )

def modal_edicion_paciente():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Editar paciente"),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_error_edicion_paciente != "",
                            rx.callout(
                                ModalState.mensaje_error_edicion_paciente,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.input(
                            name="paciente_id",
                            id="paciente_id",
                            default_value=ModalState.paciente_id,
                            display="none",
                        ),
                        rx.text(
                            "Usuario",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            name="paciente_usuario",
                            id="paciente_usuario",
                            placeholder="Introduzca el AR del paciente",
                            default_value=ModalState.paciente_usuario,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Nombre",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_nombre",
                            id="paciente_nombre",
                            placeholder="Introduzca el nombre",
                            default_value=ModalState.paciente_nombre,
                            max_length=30,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Apellidos",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_apellidos",
                            id="paciente_apellidos",
                            placeholder="Introduzca los apellidos",
                            default_value=ModalState.paciente_apellidos,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Email",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_email",
                            id="paciente_email",
                            placeholder="Introduzca el email del paciente",
                            default_value=ModalState.paciente_email,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Teléfono",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="paciente_telefono",
                            id="paciente_telefono",
                            placeholder="Introduzca el teléfono del paciente",
                            default_value=ModalState.paciente_telefono,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.vstack(
                    rx.button(
                        "Generar nueva contraseña", 
                        on_click=ModalState.modal_set_boton_on_submit("generar_contraseña"),
                        type="submit",
                        flex="1",
                    ),
                    rx.hstack(
                        rx.button(
                            "Guardar", 
                            on_click=ModalState.modal_set_boton_on_submit("guardar"),
                            type="submit", 
                            flex="1",
                        ),
                        rx.button(
                            "Cancelar", 
                            type="button", 
                            on_click=ModalState.cerrar_modal_edicion_paciente, 
                            flex="1",
                        ), 
                    spacing="4",
                    width="100%",
                    ),
                spacing="4",
                padding_top = "30px",
                ),
            on_submit=ModalState.on_submit_edicion_paciente,
            ),
        width="100%",    
        max_width="550px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"],
        ),
    open=ModalState.modal_edicion_paciente_abierto
    )
        

    
def modal_info_2_mensajes():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(ModalState.titulo_info),
            rx.dialog.description(
                rx.vstack(
                    rx.text(ModalState.mensaje_info_1, text_align="justify",),
                    rx.text(ModalState.mensaje_info_2, text_align="justify",),
                ),
            ),
            rx.button(
                "Cerrar", 
                on_click=ModalState.cerrar_modal_info, 
                width="100%",
                margin_top="20px",
            ),
        width="100%",    
        max_width="500px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"],
        ),
    open=ModalState.modal_info_abierto,
    )

def modal_confirmacion_si_no():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(ModalState.titulo_confirmacion),
            rx.dialog.description(
                rx.vstack(
                    rx.text(ModalState.mensaje_confirmacion_1, text_align="justify",),
                    rx.text(ModalState.mensaje_confirmacion_2, text_align="justify",),
                ),
            ),
            rx.hstack(
                rx.button(
                    "Si", 
                    on_click=ModalState.on_click_si_confirmacion, 
                    type="button",
                    flex="1",
                ),  
                rx.button(
                    "No", 
                    on_click=ModalState.on_click_no_confirmacion, 
                    type="button",
                    flex="1",
                ),
            spacing="4",
            width="100%",
            padding_top = "30px",
            ),
        width="100%",    
        max_width="500px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_confirmar_si_no_abierto,
    )
    
def modal_cambiar_contraseña_inicial():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Cambiar contraseña"),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_informacion_cambio_contraseña_inicial_1 != "",
                            rx.callout(
                                ModalState.mensaje_informacion_cambio_contraseña_inicial_1,
                                icon="info",
                                width="100%",
                                size="1",
                                #padding="10px", 
                                margin_top="10px",
                            ),
                        ),
                        rx.cond(
                            ModalState.mensaje_informacion_cambio_contraseña_inicial_2 != "",
                            rx.callout(
                                ModalState.mensaje_informacion_cambio_contraseña_inicial_2,
                                icon="info",
                                width="100%",
                                size="1",
                                #padding="10px", 
                                margin_top="10px",
                            ),
                        ),
                        rx.cond(
                            ModalState.mensaje_error_cambio_contraseña_inicial != "",
                            rx.callout(
                                ModalState.mensaje_error_cambio_contraseña_inicial,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.text(
                            "Nueva contraseña",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            name="contraseña_nueva_1",
                            id="contraseña_nueva_1",
                            placeholder="Introduzca la nueva contraseña",
                            max_length=20,
                            type="password",
                            size="3",
                            width="100%",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Confirmar nueva contraseña",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            name="contraseña_nueva_2",
                            id="contraseña_nueva_2",
                            placeholder="Introduzca la de nuevo la nueva contraseña",
                            max_length=20,
                            type="password",
                            size="3",
                            width="100%",
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.hstack(
                    rx.button(
                        "Guardar", 
                        type="submit",
                        flex="1",
                    ),  
                    rx.button(
                        "Cancelar", 
                        on_click=ModalState.cerrar_modal_cambio_contraseña_inicial, 
                        type="button",
                        flex="1",
                    ),
                spacing="4",
                width="100%",
                padding_top = "30px"
                ),
            on_submit=ModalState.on_submit_cambio_contraseña_inicial,
            ),
        width="100%",    
        max_width="500px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_cambio_contraseña_inicial_abierto,
    )    
    
def modal_cambiar_contraseña():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Cambiar contraseña"),
            rx.form( 
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_informacion_cambio_contraseña != "",
                            rx.callout(
                                ModalState.mensaje_informacion_cambio_contraseña,
                                icon="info",
                                width="100%",
                                size="1",
                                #padding="10px", 
                                margin_top="10px",
                            ),
                        ),
                        rx.cond(
                            ModalState.mensaje_error_cambio_contraseña != "",
                            rx.callout(
                                ModalState.mensaje_error_cambio_contraseña,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.vstack(
                            rx.text(
                                "Contraseña actual",
                                size="3",
                                weight="medium",
                                text_align="left",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("lock")),
                                name="contraseña_actual",
                                id="contraseña_actual",
                                placeholder="Introduzca la contraseña actual",
                                max_length=20,
                                type="password",
                                size="3",
                                width="100%",
                                autocomplete="new-password",
                            ),        
                        width="100%",
                        ),
                        rx.text(
                            "Nueva contraseña",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            name="contraseña_nueva_1",
                            id="contraseña_nueva_1",
                            placeholder="Introduzca la nueva contraseña",
                            max_length=20,
                            type="password",
                            size="3",
                            width="100%",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Confirmar nueva contraseña",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            name="contraseña_nueva_2",
                            id="contraseña_nueva_2",
                            placeholder="Introduzca la de nuevo la nueva contraseña",
                            max_length=20,
                            type="password",
                            size="3",
                            width="100%",
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.hstack(
                    rx.button(
                        "Guardar", 
                        type="submit",
                        flex="1",
                    ),  
                    rx.button(
                        "Cancelar", 
                        on_click=ModalState.cerrar_modal_cambio_contraseña, 
                        type="button",
                        flex="1",
                    ),
                spacing="4",
                width="100%",
                padding_top = "30px"
                ),
            on_submit=ModalState.on_submit_cambio_contraseña,
            ),
        width="100%",    
        max_width="500px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_cambio_contraseña_abierto,
    )    
  
def modal_add_edicion_estados_paciente():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(ModalState.titulo_add_edicion_estados_paciente),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_error_add_edicion_estados_paciente != "",
                            rx.callout(
                                ModalState.mensaje_error_add_edicion_estados_paciente,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.text(
                            "Descripción de estado",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            margin_top="-10px",
                            name="descripcion_estado_paciente",
                            id="descripcion_estado_paciente",
                            placeholder="Introduzca el estado",
                            max_length=50,
                            size="3",
                            width="100%",
                            default_value=ModalState.estado_paciente_descripcion,
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.hstack(
                    rx.button(
                        rx.cond(
                            ModalState.origen_modal_add_edicion_estados_paciente == "add_estado_paciente",
                            "Añadir",
                            "Guardar",
                        ),
                        type="submit",
                        flex="1",
                    ),  
                    rx.button(
                        "Cancelar", 
                        on_click=ModalState.cerrar_modal_add_edicion_estados_paciente, 
                        type="button",
                        flex="1",
                    ),
                spacing="4",
                padding_top = "30px",
                ),
            on_submit=ModalState.on_submit_add_edicion_estados_paciente,
            ),
        width="100%",    
        max_width="450px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_add_edicion_estados_paciente_abierto,
    )
    
def modal_confirmar_envio_comunicacion():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Confirmar comunicación a los contactos"),
            rx.dialog.description(
                rx.vstack(
                    rx.text(
                        rx.cond(
                            ModalState.confirmar_envio_observaciones == "",
                            f"El paciente {ModalState.confirmar_envio_usuario} tiene un nuevo estado: {ModalState.confirmar_envio_nuevo_estado}",
                            f"El paciente {ModalState.confirmar_envio_usuario} tiene un nuevo estado: {ModalState.confirmar_envio_nuevo_estado}  Observaciones: {ModalState.confirmar_envio_observaciones}",
                        ),
                        size="3",
                        weight="medium",
                        text_align="left",
                    ),
                )
            ),
            rx.hstack(
                rx.button(
                    "Enviar",  
                    on_click=ModalState.on_click_enviar_comunicacion, 
                    type="button",
                    flex="1"
                ),  
                rx.button(
                    "Cancelar", 
                    on_click=ModalState.on_click_cancelar_comunicacion, 
                    type="button",
                    flex="1"
                ),
            spacing="4",
            width="100%",
            padding_top = "30px"
            ),
        width="100%",    
        max_width="500px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_confirmar_envio_comunicacion_abierto,
    )
    
def modal_gest_facultativo_QR():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Código QR usuario"),
            rx.dialog.description(
                rx.vstack(
                    rx.cond(
                        ModalState.qr_base64 != "",
                        rx.box(
                            rx.vstack(
                                rx.image(src=ModalState.qr_base64, width="300px"),
                                rx.text(ModalState.gest_facul_usuario),
                                class_name="qrprint",
                            align="center",
                            width="100%",
                            ),
                        ),
                    ),
                )
            ),
            rx.hstack(
                rx.button(
                    "Imprimir", 
                    on_click=rx.call_script("window.print()"), 
                    type="button",
                    is_disabled=ModalState.qr_base64 == "", 
                    flex="1",
                ),  
                rx.button(
                    "Cancelar", 
                    on_click=ModalState.cerrar_modal_gest_facul_qr, 
                    type="button",
                    flex="1",
                ),
            spacing="4",
            width="100%",
            margin_top="30px",
            ),
        width="100%",    
        max_width="400px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_gest_facul_QR_abierto,
    )
    
def modal_añadir_facultativo():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Añadir facultativo"),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_error_añadir_facultativo != "",
                            rx.callout(
                                ModalState.mensaje_error_añadir_facultativo,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.text(
                            "Usuario",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            name="facultativo_usuario",
                            id="facultativo_usuario",
                            placeholder="Introduzca el email corporativo",
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            default_value=ModalState.facultativo_usuario,
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Nombre",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="facultativo_nombre",
                            id="facultativo_nombre",
                            placeholder="Introduzca el nombre",
                            max_length=30,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            default_value=ModalState.facultativo_nombre,
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Apellidos",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="facultativo_apellidos",
                            id="facultativo_apellidos",
                            placeholder="Introduzca los apellidos",
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            default_value=ModalState.facultativo_apellidos,
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Teléfono",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="facultativo_telefono",
                            id="facultativo_telefono",
                            placeholder="Introduzca el teléfono de contacto",
                            max_length=9,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            default_value=ModalState.facultativo_telefono,
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            "Añadir",
                            type="submit", 
                            flex="1",
                        ),  
                        rx.button(
                            "Cancelar", 
                            type="button",
                            on_click=ModalState.cerrar_modal_añadir_facultativo, 
                            flex="1",
                        ),
                    spacing="4",
                    width="100%",
                    ),
                spacing="4",
                padding_top = "30px",
                ),
        on_submit=ModalState.on_submit_añadir_facultativo,
        ),
        width="100%",    
        max_width="550px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_añadir_facultativo_abierto,
    )
    
def modal_edicion_facultativo():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Editar facultativo"),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_error_edicion_facultativo != "",
                            rx.callout(
                                ModalState.mensaje_error_edicion_facultativo,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.input(
                            name="facultativo_id",
                            id="facultativo_id",
                            default_value=ModalState.facultativo_id,
                            display="none",
                        ),
                        rx.text(
                            "Usuario",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            name="facultativo_usuario",
                            id="facultativo_usuario",
                            placeholder="Introduzca el email corporativo",
                            default_value=ModalState.facultativo_usuario,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Nombre",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="facultativo_nombre",
                            id="facultativo_nombre",
                            placeholder="Introduzca el nombre",
                            default_value=ModalState.facultativo_nombre,
                            max_length=30,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Apellidos",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="facultativo_apellidos",
                            id="facultativo_apellidos",
                            placeholder="Introduzca los apellidos",
                            default_value=ModalState.facultativo_apellidos,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Teléfono",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="facultativo_telefono",
                            id="facultativo_telefono",
                            placeholder="Introduzca el teléfono de contacto",
                            default_value=ModalState.facultativo_telefono,
                            max_length=9,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.vstack(
                    rx.button(
                        "Generar nueva contraseña", 
                        on_click=ModalState.modal_set_boton_on_submit("generar_contraseña"),
                        type="submit",
                        flex="1",
                    ),
                    rx.hstack(
                        rx.button(
                            "Guardar",
                            on_click=ModalState.modal_set_boton_on_submit("guardar"),
                            type="submit", 
                            flex="1",
                        ),  
                        rx.button(
                            "Cancelar", 
                            type="button",
                            on_click=ModalState.cerrar_modal_edicion_facultativo, 
                            flex="1",
                        ),
                    spacing="4",
                    width="100%",
                    ),
                spacing="4",
                padding_top = "30px",
                ),
        on_submit=ModalState.on_submit_edicion_facultativo,
        ),
        width="100%",    
        max_width="550px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_edicion_facultativo_abierto,
    )
    
def modal_confirmar_envio_prueba():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Confirmar comunicación de prueba"),
            rx.dialog.description(
                rx.vstack(
                    rx.text("¿Desea enviar una comunicación de prueba?"),
                    rx.cond(
                        ProtectedState.paciente_logueado != None,
                        rx.cond(
                            ProtectedState.paciente_logueado.envios_pruebas == 1,
                            rx.text(f"Dispone de 1 comunicación para enviar"),
                            rx.text(f"Dispone de {ProtectedState.paciente_logueado.envios_pruebas} comunicaciones para enviar", text_align="justify",),
                        ),
                        
                    ),
                ),
            ),
            rx.hstack(
                rx.button(
                    "Enviar", 
                    on_click=ModalState.on_click_enviar_mensaje_prueba, 
                    type="button",
                    flex="1",
                ),  
                rx.button(
                    "Cancelar", 
                    on_click=ModalState.cerrar_modal_confirmar_envio_prueba, 
                    type="button",
                    flex="1",
                ), 
            spacing="4",
            width="100%",
            padding_top = "30px"
            ),
        max_width="550px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"], 
        ),
    open=ModalState.modal_confirmar_envio_prueba_abierto,
    )
'''
def modal_edicion_datos_paciente():
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("Editar datos"),
            rx.form(
                rx.dialog.description(
                    rx.vstack(
                        rx.cond(
                            ModalState.mensaje_error_edicion_paciente != "",
                            rx.callout(
                                ModalState.mensaje_error_edicion_paciente,
                                icon="triangle_alert",
                                color_scheme="red",
                                role="alert",
                                width="100%",
                            ), 
                        ),
                        rx.input(
                            name="datos_paciente_id",
                            id="datos_paciente_id",
                            default_value=ModalState.paciente_id,
                            display="none",
                        ),
                        rx.text(
                            "Nombre",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="datos_paciente_nombre",
                            id="datos_paciente_nombre",
                            placeholder="Introduzca el nombre",
                            default_value=ModalState.paciente_nombre,
                            max_length=30,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Apellidos",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="datos_paciente_apellidos",
                            id="datos_paciente_apellidos",
                            placeholder="Introduzca los apellidos",
                            default_value=ModalState.paciente_apellidos,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Email",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="datos_paciente_email",
                            id="datos_paciente_email",
                            placeholder="Introduzca el email del paciente",
                            default_value=ModalState.paciente_email,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                        rx.text(
                            "Teléfono",
                            size="3",
                            weight="medium",
                            text_align="left",
                        ),
                        rx.input(
                            name="datos_paciente_telefono",
                            id="datos_paciente_telefono",
                            placeholder="Introduzca el teléfono del paciente",
                            default_value=ModalState.paciente_telefono,
                            max_length=50,
                            size="3",
                            width="100%",
                            margin_top="-10px",
                            autocomplete="new-password",
                        ),
                    width="100%",
                    ),
                ),
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            "Guardar", 
                            type="submit", 
                            flex="1",
                        ),
                        rx.button(
                            "Cancelar", 
                            type="button", 
                            on_click=ModalState.cerrar_modal_edicion_datos_paciente, 
                            flex="1",
                        ), 
                    spacing="4",
                    width="100%",
                    ),
                spacing="4",
                padding_top = "30px",
                ),
            on_submit=ModalState.on_submit_edicion_datos_paciente,
            ),
        width="100%",    
        max_width="550px",
        left=["auto", "auto", "auto", "calc(0% + 170px)"],
        ),
    open=ModalState.modal_edicion_datos_paciente_abierto,
    )
'''