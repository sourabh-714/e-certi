
from PIL import Image, ImageDraw, ImageFont
import os
os.system("python -m pip install Pillow")
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import csv 



fromaddr = "sourabh18csu241@ncuindia.edu"
password = "pass"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sourabh18csu241@ncuindia.edu","pass"
)

csvfile = r"certi.csv"

def process(word,toaddr):
    #image = Image.open('71.jpg')
    #draw = ImageDraw.Draw(image)
    #font = ImageFont.truetype("mtc.ttf",150)
   # try:
      #  os.mkdir('certificates')
   # except:pass
    #(x, y) = (2212, 1695)
    #color = 'rgb(0, 0, 0)'
    #draw.text((x, y), word.title(), fill=color, size=45, font=font)
    #filename = os.path.join('certificates',f"{word}_certificate.jpg")
    #image.save(os.path.join(filename))
    msg = MIMEMultipart() 
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = "Certificate of webinar on Domestic violence amid Covid-19 lockdown"
    body = """{word}Type the message here"""
    msg.attach(MIMEText(body, 'plain')) 
   # attachment = open(filename, "rb")  
    p = MIMEBase('application', 'octet-stream') 
    #p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    #p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)

with open(csvfile,'r') as file:
    print('processing pls wait')
    for word,email in [x for x in csv.reader(file)][1:]:
        process(word,email)
    print('certificates sent')
s.quit()
