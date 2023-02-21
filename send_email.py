import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "curtkellum@gmail.com"
    password = os.getenv("PASSWORD")
    print(password)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        print(message)
        server.sendmail(username, username, message)
