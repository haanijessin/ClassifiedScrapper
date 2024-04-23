import re, requests, time, sys
from datetime import date
from bs4 import BeautifulSoup
from wand.image import Image as wandImage
from PIL import Image
import pytesseract


def randomLoading():
    dots = " . .\n"
    for i in dots:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


sys.stdout.write("Starting Classfied Scraping .")
randomLoading()

# Getting link for latest PDF file
today = date.today().strftime("%Y%m%d")
mainPage = requests.get("https://www.gulf-times.com/Classified")
content = mainPage.content
soup = BeautifulSoup(content, "html.parser")
link = soup.find(href=re.compile(today))["href"]

# Downloading the PDF file from link
sys.stdout.write("Downloading PDF .")
randomLoading()

myFile = requests.get(link)
filePath = "./PDFDownloads/classified.pdf"
with open(filePath, "wb") as PDF:
    PDF.write(myFile.content)

# OCR and checking for required data
sys.stdout.write("Checking Data.")
randomLoading()

# For wand to work, install ImageMagik, GhostScript for windows.
# For OCR to work, install Tesseract OCR and add to path.

# def dataCollect(filePath):
#    imgPath = "C:/Users/haani/source/repos/Classified Scraper/PDFDownloads/image.jpg"
#    dataPath = "C:/Users/haani/source/repos/Classified Scraper/PDFDownloads/data.txt"

#    with wandImage(filename=filePath, resolution=300) as PDFimage:
#        for i in PDFimage.sequence:
#            img = wandImage(image=i)
#            img.save(filename=imgPath)

#            with open(dataPath,"r+") as dataFile:
#                dataFile.write(image_to_string(Image.open(imgPath)))
#                for line in dataFile:
#                     if not 'situation wanted' in line.lower():
#                         data+=line
#    return data


def datacollect(filepath):
    with wandImage(filename=filepath, resolution=300) as pdfimage:
        for i in pdfimage.sequence:
            img = wandImage(image=i)
            imgpath = "./PDFDownloads/image.jpg"
            img.save(filename=imgpath)
            initData = pytesseract.image_to_string(Image.open(imgpath))

            data = """"""
            for line in initData:
                if not "situation wanted" in line.lower():
                    data += line
                else:
                    return data


datacollect(filePath)
