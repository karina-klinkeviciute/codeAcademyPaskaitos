import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from string import Template
import mimetypes

# elementarios email žinutės sukūrimas:
email = EmailMessage()
# email = MIMEMultipart('alternative')

email['from'] = 'Vardas Pavardė'
email['to'] = 'karina.klinkeviciute@gmail.com'
email['subject'] = 'email from python'

files = ['jude-mitchellhedges.jpg', 'ache-surya.jpg', "laiskas.html"]

for file in files:
    mimetype = mimetypes.guess_type(file)[0]
    subtype = mimetype.split('/')[1]
    with open(file, 'rb') as img:
        content = img.read()
        email.add_attachment(
            content,
            maintype=mimetype,
            subtype=subtype,
            filename=file)



with open('laiskas_su_vardu.html', 'r') as f:
    laisko_html = f.read()

sablonas = Template(laisko_html)


# email.set_content("labas rytas, bandau siusti laiskus", "html")
# email.set_content(sablonas.substitute({'vardas': 'Karina'}), "html")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
    smtp.starttls() # inicijuojame šifruotą kanalą
    smtp.login('aaha87151@gmail.com', "twksjlvsrfiidogi") # nurodome prisijungimo duomenis
    smtp.send_message(email) # išsiunčiame žinutę

print("Done")
#

#

