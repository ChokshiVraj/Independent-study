from PyPDF2 import PdfFileWriter, PdfFileReader
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  
import listusers

from listusers import dict2
import importlib
def up(frames):
 upload_file_list = []
 upload_file_list.append(frames)
 for upload_file in upload_file_list:
	 gfile = drive.CreateFile({'parents': [{'id': '1waodpEZGHOF_U7iFLWzX9bws45vHxqyk'}]})
	 gfile.SetContentFile(upload_file)
	 gfile.Upload() # Upload the file.
	 # Read file and set it as the content of this instance.
	#gfile.SetContentFile(upload_file)
    


pdfWriter = PdfFileWriter()
#my_dict = {"hello42031398@gmail.com":1}

# Read the pdf file which will be encrypted
pdf = PdfFileReader("original.pdf")

for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))

# Encryption process goes here
passw = input('Enter your password: ')
pdfWriter.encrypt(passw)
print('Password was set successfully !')

setNewName = input('What will you name your encrypted pdf? (without ".pdf") : ')
newPdfName = str(setNewName) + '.pdf'
dict2.update({setNewName:passw})
#importlib.reload(listusers.dict2)
#print(dict2)
# Create a new encrypted PDF
with open(newPdfName, 'wb') as f:
    pdfWriter.write(f)
    f.close()

up(newPdfName)
print('Excellent! You have secured your PDF file!')



