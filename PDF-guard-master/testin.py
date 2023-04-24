import smtplib
import ssl
from email.message import EmailMessage
import random
import time
import smtplib

def generate_otp(length=6):
    """Generate a random OTP of the given length."""
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += digits[random.randint(0, 9)]
    return otp

otp = generate_otp()
print(f"Generated OTP: {otp}")
email_sender = 'brochacha420@gmail.com'
email_password = 'pdahqhecdlfvuymo'
email_receiver = 'hello42031398@gmail.com'

subject = 'Your OTP'
body = """
{}
""".format(otp)
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())