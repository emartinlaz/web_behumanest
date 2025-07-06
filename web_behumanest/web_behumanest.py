import reflex as rx
from .paginas_publicas import index_page, login_page, recuperar_contrasena_page, construccion_page
from .paginas_publicas import consentimientos_page, que_vamos_a_hacer_page
from .paginas_publicas import proyecto_behumanest_page, indicaciones_generales_page, comunicacion_fecha_ingreso_page, ubicacion_espera_familias_page
from .paginas_publicas import en_planta_page, telefonos_interes_page, traslado_quirofano_page, comunicacion_behumanest_page, preparacion_previa_intervencion_page
from .paginas_publicas import aviso_legal_page, politica_privacidad_page, que_llevar_ingreso_page, ubicacion_acceso_ingreso_page, ubicacion_consulta_page
from .paginas_privadas import facultativo_page, gestion_facultativos_page, paciente_page, gestion_pacientes_page, estados_paciente_page
from .styles import styles
from dotenv import load_dotenv


load_dotenv()   #Carga las variables de entorno designadas en .env

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    html_lang="es",
    theme=rx.theme(
        panel_background="translucent",
        appearance="light",
       )
    ) 
