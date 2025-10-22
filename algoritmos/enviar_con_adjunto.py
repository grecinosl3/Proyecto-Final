import os
import mimetypes
import smtplib
import ssl
from email.message import EmailMessage

# Configuración del servidor SMTP de Gmail
SERVIDOR = "smtp.gmail.com"
PUERTO = 587
CONTRASENA = os.getenv('GOOGLE_APP_PASS')  # Tu contraseña de aplicación de Google
USUARIO = os.getenv("GOOGLE_APP_EMAIL")        # Tu email

def enviar_mensaje(asunto, cuerpo, destinatario, titulo, nombre_archivo, ruta_de_adjunto):
    mensaje = EmailMessage()
    mensaje["Subject"] = asunto
    mensaje["From"] = USUARIO
    mensaje["To"] = destinatario

    # Cuerpo del mensaje
    mensaje.set_content(cuerpo)

    # Versión HTML (opcional)
    mensaje.add_alternative(f"""
    <html>
      <body>
        <h1>{titulo}</h1>
        <p>{cuerpo}</p>
      </body>
    </html>
    """, subtype="html")

    # Obtener tipo MIME del archivo
    ctype, encoding = mimetypes.guess_type(nombre_archivo)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    tipo_principal, sub_tipo = ctype.split("/", 1)

    ruta_completa = os.path.join(ruta_de_adjunto, nombre_archivo)
    with open(ruta_completa, "rb") as archivo:
        mensaje.add_attachment(archivo.read(),
                               maintype=tipo_principal,
                               subtype=sub_tipo,
                               filename=nombre_archivo)

    # Conexión segura y envío
    context = ssl.create_default_context()
    with smtplib.SMTP(SERVIDOR, PUERTO) as smtp:
        smtp.starttls(context=context)
        smtp.login(USUARIO, CONTRASENA)
        smtp.send_message(mensaje)
