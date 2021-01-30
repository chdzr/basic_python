import os
import smtplib, ssl, mimetypes
from getpass import getpass
from subject import Subject
from receiver import Receiver
from content import Content
from attachment import Attachment
from email.message import EmailMessage

# https://realpython.com/python-send-email/
# https://docs.python.org/3/library/email.examples.html

def main():
    s = Subject()
    subject = s.get_subject()
    if not(subject == ""):
        send_email_proccess(subject)
    else:
        print('You should entry the subject of email')


def send_email_proccess(subject):
    try:
        context = ssl.create_default_context()
        email_address = input("Input Your Email Address : ")
        password = getpass()
        emailClient = smtplib.SMTP('smtp.gmail.com', 587)
        emailClient.ehlo()
        emailClient.starttls(context=context)
        emailClient.ehlo()
        emailClient.login(email_address, password)
        msg = prepare_email_content(email_address, subject)
        emailClient.send_message(msg)
        emailClient.quit()
    except Exception as err:
        print(err)

def prepare_email_content(email_address, subject):
    #construct Receiver, Content and Attachment Class
    r = Receiver()
    c = Content()
    a = Attachment()
    
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['To'] = ', '.join(r.get_receiver())
    msg['From'] = email_address
    msg.set_content(c.get_content())
    set_attachment(msg, a.get_attachments())
    return msg


def set_attachment(msg, list_attachment):
    for attachment in range(len(list_attachment)):
        filename = os.path.basename(list_attachment[attachment])
        ctype, encoding = mimetypes.guess_type(list_attachment[attachment])
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        with open(list_attachment[attachment], 'rb') as fp:
            msg.add_attachment(fp.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=filename)

if __name__ == "__main__":
    main()