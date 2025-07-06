from sqlmodel import create_engine
import os

ENVIRONMENT = os.getenv("ENVIRONMENT", "servidor").lower()
BASE_DATOS = os.getenv("BASE_DATOS", "produccion").lower()
MYSQL_KEY = os.getenv("MYSQL_KEY", "xxx")

if ENVIRONMENT == "local":
    #local
    if BASE_DATOS == "pruebas":
        URL_DATABASE = f'mysql+pymysql://admin:{MYSQL_KEY}@behumanest.com:3306/behumanest_pre'
    else:
        URL_DATABASE = f'mysql+pymysql://admin:{MYSQL_KEY}@behumanest.com:3306/behumanest' 
else:
    #servidor
    if BASE_DATOS == "pruebas":
        URL_DATABASE = f'mysql+pymysql://admin:{MYSQL_KEY}@localhost:3306/behumanest_pre'
    else:
        URL_DATABASE = f'mysql+pymysql://admin:{MYSQL_KEY}@localhost:3306/behumanest'
    
ssl_args = {'ssl_ca':'../certificado_mysql_behumanest/ca.pem',
            'ssl_cert':'../certificado_mysql_behumanest/client-cert.pem',
            'ssl_key':'../certificado_mysql_behumanest/client-key.pem'}

engine = create_engine(URL_DATABASE, connect_args=ssl_args, echo=False)

def connect():
    return engine



