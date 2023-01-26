import PyPDF2
from gtts import gTTS

# Open the PDF file
pdf_file = open('Richard Philemon Msule Software Devloper.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Iterate through each page of the PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()

    # Convert the text to speech
    tts = gTTS(text=text, lang='en', tld='co.za')

    # Save the audio file
    tts.save('audio{}.mp3'.format(page_num + 1))

pdf_file.close()
