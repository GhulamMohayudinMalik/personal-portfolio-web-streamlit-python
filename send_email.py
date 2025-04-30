import smtplib
import ssl

MY_EMAIL = 'ghulammohayudinmalik@gmail.com'
MY_PASSWORD = 'skbv jjko yumj orwo'


def send_email(mail, msg):
    host = "smtp.gmail.com"
    port = 465
    receiver = mail
    context = ssl.create_default_context()
    message = msg
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(MY_EMAIL, MY_PASSWORD)
        server.sendmail(MY_EMAIL, receiver, message)
