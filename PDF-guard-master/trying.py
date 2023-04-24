import random
import time
import smtplib

def send_email(recipient, subject, body):
    """Send an email to the given recipient with the given subject and body."""
    sender = "hello42031398@gmail.com"
    password = "Akash@7781"
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message)
# Example usage:
recipient = "hello42031398@gmail.com"
subject = "Hello from Python"
body = "This is a test email sent from Python!"
send_email(recipient, subject, body)
print(f"Sent email to {recipient}")
def generate_otp(length=6):
    """Generate a random OTP of the given length."""
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += digits[random.randint(0, 9)]
    return otp

def verify_otp(otp, max_age=60):
    """Verify the OTP is correct and not expired."""
    current_time = int(time.time())
    try:
        otp_time, otp_value = otp.split(":")
        otp_time = int(otp_time)
    except ValueError:
        return False
    if current_time - otp_time > max_age:
        return False
    return otp == f"{otp_time}:{otp_value}"

# Example usage:
otp = generate_otp()
print(f"Generated OTP: {otp}")

# Simulate a delay between generating and verifying the OTP
time.sleep(1)

if verify_otp(otp, max_age=15):
    print("OTP is valid!")
else:
    print("OTP is invalid or expired.")
