import re  #funciones regulares
import boto3
from sms_api.altiria_client import *
import string
import secrets
import os

EMAIL_ID = os.getenv("EMAIL_ID", "xxx")
EMAIL_KEY = os.getenv("EMAIL_KEY", "xxx")
SMS_ID = os.getenv("SMS_ID", "xxx")
SMS_KEY = os.getenv("SMS_KEY", "xxx")

debug = False

def enviar_email(destinatario: str, asunto: str, mensaje_a_enviar: str):
    if debug: print("Enviando email")
    ses_client = boto3.client(
        'ses', 
        region_name='eu-west-3',
        aws_access_key_id=EMAIL_ID,
        aws_secret_access_key=EMAIL_KEY
    )
    response = ses_client.send_email(
        Source="noreply@behumanest.com",
        Destination={'ToAddresses': [f"{destinatario}"]},
        Message={
            'Subject': {'Data': f'{asunto}'},
            'Body': {'Text': {'Data': f'{mensaje_a_enviar}'}}
        }
    )
    if debug: print("Email enviado:", response)



def is_valid_email(email: str, permitir_nulo: bool = True):
    # Regular expression for validating an Email
    #regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    #regex = r"[^@]+@[^@]+.[^@]+"
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._%+-]+\.[A-Z|a-z]{2,7}\b'
    # If the string matches the regex, it is a valid email
    #if not email: return False
    if permitir_nulo and email == "": return True
    if email and len(email) > 0:
        if re.match(regex, email):
            return True
        else:
            return False
    return False
    
    

def is_valid_telefono(telefono: str, permitir_nulo: bool = True):
    if permitir_nulo and telefono == "": return True
    if (len(telefono) == 9 and telefono.isdigit()):
        return True
    else:
        return False
    

def enviar_sms(destinatario: str, mensaje_a_enviar: str):
    try:
        client = AltiriaClient(SMS_ID, SMS_KEY)
        textMessage = AltiriaModelTextMessage(f"34{destinatario}", mensaje_a_enviar, senderId='Behumanest')
        jsonText = client.sendSms(textMessage)
        #print('¡Mensaje enviado!')
    except AltiriaGwException as ae: 
        print('Mensaje no aceptado:'+ae.message)
        print('Código de error:'+ae.status)
    except JsonException as je:
        print('Error en la petición:'+je.message)
    except ConnectionException as ce:
        if "RESPONSE_TIMEOUT" in ce.message: 
            print('Tiempo de respuesta agotado:'+ce.message)
        else:
            print('Tiempo de conexión agotado:'+ce.message)


def opcionalstr_to_str(variable: str):
    if variable: 
        return variable
    else:
        return ""
    
def str_to_opcionalstr(variable: str):
    if variable == "": 
        return None
    else:
        return variable
    
def get_nueva_contraseña(longitud=10):
    caracteres = string.ascii_uppercase + string.digits #+ string.punctuation   # ascii_letters 
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))