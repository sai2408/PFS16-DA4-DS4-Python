import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
otp = random.randint(1111,9999)
months = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"Decemeber"}
name = input("Enter Your name: ")
date = int(input("Enter Your Date of Birth: "))
month = int(input("Enter your Month of birth: "))

tomail = input("Enter Mail id: ")
subject = "OTP For Verification"
body = f"Hello {name} !\nDate of Birth : {date} - {months[month]}\nYour Secret OTP is {otp}"

msg = MIMEMultipart()
msg['From'] = "saivardhan@codegnan.com"
msg['To'] = tomail
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("saivardhan@codegnan.com","yyzz guyc uejz rbod")
server.send_message(msg)
server.quit()

userinput = input("Enter OTP recieved to your mail: ")
if userinput == str(otp):
    print("OTP Validation Successfull !")
else:
    print("Wrong OTP Entered !")
