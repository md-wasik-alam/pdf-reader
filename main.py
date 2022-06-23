from gtts import gTTS
from playsound import playsound

import os

import PyPDF2
# open("file name","rb")
pdf_file = open("exam.pdf","rb")

pdf_reader = PyPDF2.PdfFileReader(pdf_file)

count = pdf_reader.numPages

textList = []

for i in range(count):
    try:
        page = pdf_reader.getPage(i)

        textList.append(page.extractText())
    except :
        pass    

textString = " ".join(textList)



lang = "en"
myFile = gTTS(text=textString,lang=lang,slow=False)
myFile.save("data.mp3")
file = os.path.dirname("") + "data.mp3"
playsound(file)