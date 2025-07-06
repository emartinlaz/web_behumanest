

def get_mensaje_email_envio_contraseña(contraseña: str):
    return f"Bienvenido a Behumanest.\n\nLa contraseña inicial de acceso es: {contraseña}\n\nEn el primer acceso al área privada, se pedirá cambiar la contraseña por seguridad.\n\n\nEste es un email automático, no contestes a este email.\nSi ha recibido este mensaje por error, por favor elimínelo."

def get_mensaje_sms_envio_contraseña(contraseña: str):
    return f"Bienvenido a Behumanest\nLa contraseña inicial de acceso es: {contraseña}\nEn el primer acceso al area privada, se pedirá cambiar la contraseña"


def get_mensaje_email_reenvio_contraseña(contraseña: str):
    return f"Recuperación de contraseña.\n\nLa contraseña inicial de acceso es: {contraseña}\n\nEn el primer acceso al área privada, se pedirá cambiar la contraseña por seguridad.\n\n\nEste es un email automático, no contestes a este email.\nSi ha recibido este mensaje por error, por favor elimínelo."

def get_mensaje_sms_reenvio_contraseña(contraseña: str):
    return f"Recuperación de contraseña\nLa contraseña inicial de acceso es: {contraseña}\nEn el primer acceso al area privada, se pedirá cambiar la contraseña"

def get_mensaje_email_contacto_paciente(usuario: str, nuevo_estado: str, observaciones: str = ""):
    if observaciones == "":
        return f"Comunicación de Behumanest.\n\nEl paciente {usuario} tiene un nuevo estado: {nuevo_estado}.\n\n\nEste es un email automático, no contestes a este email.\nSi ha recibido este mensaje por error, por favor elimínelo."
    else:
        return f"Comunicación de Behumanest.\n\nEl paciente {usuario} tiene un nuevo estado: {nuevo_estado}.\n\nObservaciones: {observaciones}.\n\n\nEste es un email automático, no contestes a este email.\nSi ha recibido este mensaje por error, por favor elimínelo."

def get_mensaje_sms_contacto_paciente(usuario: str, nuevo_estado: str, observaciones: str = ""):
    if observaciones == "":
        return f"Comunicacion de Behumanest\n\nEl paciente {usuario} tiene un nuevo estado: {nuevo_estado}"
    else:
        return f"El paciente {usuario} tiene un nuevo estado: {nuevo_estado}\n\nObservaciones: {observaciones}"
    
def get_mensaje_email_envio_prueba_paciente():
    return "Comunicación de Behumanest.\n\nEsto es una prueba de comunicación.\n\nSi ha recibido este mensaje, ha configurado correctamente los datos de contacto.\n\n\nEste es un email automático, no contestes a este email.\nSi ha recibido este mensaje por error, por favor elimínelo."

def get_mensaje_sms_envio_prueba_paciente():
    return "Comunicacion de Behumanest\nEsto es una prueba de comunicacion\nSi ha recibido este mensaje, ha configurado correctamente los datos de contacto"

