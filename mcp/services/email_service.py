import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(recipient_email, subject, body):

    sender_email = "yumcand.m@gmail.com"
    sender_password = "hcgo iuws hdul sfhj"

    msg = MIMEMultipart()

    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    server.send_message(msg)

    server.quit()

    return "Email sent successfully!"