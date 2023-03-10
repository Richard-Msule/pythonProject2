# importing the modules
import PyPDF2
import pyttsx3

# path of the PDF file
path = open('TENDER DOC. MINI PAINTING MJIMWEMA ADD.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.pages[1]

# extracting the text from the PDF
text = from_page.extract_text()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

