import os
import smtplib, ssl
from subject import Subject
from receiver import Receiver
from content import Content
from attachment import Attachment
from email.message import EmailMessage

s = Subject()
#print(s.get_subject())
r = Receiver()
#print(r.get_receiver())
c = Content()
#print(c.get_content())
a = Attachment()
#print(a.get_attachments())


# https://realpython.com/python-send-email/
# https://docs.python.org/3/library/email.examples.html
def main():
    FROM = 'chidzirw@gmail.com'
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg['Subject'] = s.get_subject()
    msg['To'] = ', '.join(r.get_receiver())
    msg['From'] = FROM  # Enter your address
    msg.set_content(c.get_content())

    try:
        password = input("Type of Your Password and press Enter: ")
        emailClient = smtplib.SMTP('smtp.gmail.com', 587)
        emailClient.ehlo()
        emailClient.starttls(context=context)
        emailClient.ehlo()
        emailClient.login("chidzirw@gmail.com", password)
        emailClient.send_message(msg)
        emailClient.quit()
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()