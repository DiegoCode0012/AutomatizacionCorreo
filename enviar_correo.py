import os
import requests

# Configuración del remitente y destinatario
REMITENTE = "diegoburneo@gmail.com"
DESTINATARIO = "diegoburneoh@gmail.com"

# Lee la API Key de Brevo desde los secretos de GitHub
API_KEY = os.environ.get("MAIL_PASS")

url = "https://api.brevo.com/v3/smtp/email"

headers = {
    "accept": "application/json",
    "api-key": API_KEY,
    "content-type": "application/json"
}

payload = {
    "sender": {"name": "Automatizacion GitHub", "email": REMITENTE},
    "to": [{"email": DESTINATARIO}],
    "subject": "Correo automatizado desde GitHub Actions con Brevo",
    "textContent": "¡Hola! Este correo se envió desde la nube de GitHub usando la API de Brevo y llegó sin problemas."
}

try:
    print("Enviando correo a través de la API de Brevo...")
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print("¡Correo enviado con éxito!")
    else:
        print(f"Error al enviar el correo. Código: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")