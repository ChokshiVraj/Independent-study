from PyPDF2 import PdfFileWriter, PdfFileReader
import smtplib
import ssl
from email.message import EmailMessage
import random
import time
import smtplib
import listusers
from listusers import my_dict,dict2
import sys

#import pdf-encryptor



def generate_otp(length=6):
    """Generate a random OTP of the given length."""
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += digits[random.randint(0, 9)]
    return otp

otp = generate_otp()
filename = input('Enter filename:')
if filename not in dict2:
  print('No such file exist')
  sys.exit()
email = input('Enter your email: ')
if email not in my_dict:
  print("You donot have access")
  sys.exit()

email_sender = 'brochacha420@gmail.com'
email_password = 'pdahqhecdlfvuymo'
email_receiver = email

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

pdfWriter = PdfFileWriter()

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

# Read the pdf file which will be encrypted
#email = input('Enter your email: ')

 
password = input('Enter your otp: ')

while(password!=otp):
  print("Wrong otp")
  password = input('Enter your otp: ')
static_password = input('Enter admin set password')
psd = static_password

print(dict2[filename])
while(dict2[filename]!=int(static_password)):
  print("Try again")
  static_password = input('Enter admin set password')
fil = filename + ".pdf"  
decrypt_pdf(fil, 'new.pdf',psd)
pdf = PdfFileReader('new.pdf')

print('Excellent! You have securely download your PDF file!')