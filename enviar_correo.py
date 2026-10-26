import os
import smtplib
from email.message import EmailMessage

REMITENTE = "diegoburneo@gmail.com"
DESTINATARIO = "diegoburneoh@gmail.com"

# Lee la contraseña de aplicación desde los secretos de GitHub
PASSWORD_APP = os.environ.get("MAIL_PASS")

# Impresión corregida en Python (usando f-string)
print(f"Valor enmascarado de la contraseña: {PASSWORD_APP}")

# Comprobación útil de longitud para saber si llegó vacía o no
if PASSWORD_APP:
    print(f" Longitud recibida: {len(PASSWORD_APP)} caracteres")
else:
    print("❌ LA VARIABLE MAIL_PASS ESTÁ VACÍA (None)")

mensaje = EmailMessage()
mensaje["From"] = REMITENTE
mensaje["To"] = DESTINATARIO
mensaje["Subject"] = "Correo automatizado desde GitHub Actions"
mensaje.set_content("¡Hola! Este correo se envió automáticamente desde la nube de GitHub.")

try:
    print("Conectando al servidor con TLS (Puerto 587)...")
    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(REMITENTE, PASSWORD_APP)
        servidor.send_message(mensaje)

    print("¡Correo enviado con éxito!")

except Exception as e:
    print(f"Error al enviar el correo: {e}")