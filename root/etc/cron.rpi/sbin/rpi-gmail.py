#!/usr/bin/python
 
# Import smtplib for the actual sending function
import smtplib
 
# For guessing MIME type
import mimetypes
 
# Import the email modules we'll need
import email
import email.mime.application
 
#Import sys to deal with command line arguments
import sys
 

def test():
    print ("Test")
    send_gmailEx("mySubject","rpi.fongming@gmail.com","rpi.fongming@gmail.com","my Body", "my att")

def send_gmailEx(_subject,_from,_to,_body,_att):
    print (_subject,_from,_to,_body,_att)

def send_gmail(iMsg):
    # send via Gmail server
    # NOTE: my ISP, Centurylink, seems to be automatically rewriting
    # port 25 packets to be port 587 and it is trashing port 587 packets.
    # So, I use the default port 25, but I authenticate.
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login('rpi.fongming@gmail.com','Fongshek702')
    s.sendmail('rpi.fongming@gmail.com',['rpi.fongming@gmail.com'], iMsg.as_string())
    s.quit()

def run():
    # Create a text/plain message
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = '#IFTTT #TWITTER'
    msg['From'] = 'rpi.fongming@gmail.com'
    msg['To'] = 'rpi.fongming@gmail.com'
     
    # The main body is just another attachment
    body = email.mime.Text.MIMEText("""Here you can write as many things as you want!""")
    msg.attach(body)
     
    # PDF attachment block code
     
    directory=sys.argv[1]
     
    # Split de directory into fields separated by / to substract filename
     
    spl_dir=directory.split('/')
     
    # We attach the name of the file to filename by taking the last
    # position of the fragmented string, which is, indeed, the name
    # of the file we've selected
     
    filename=spl_dir[len(spl_dir)-1]
     
    # We'll do the same but this time to extract the file format (pdf, epub, docx...)
     
    spl_type=directory.split('.')
     
    type=spl_type[len(spl_type)-1]
     
    fp=open(directory,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype=type)
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)
     
    send_gmail(msg)

if (len(sys.argv) == 1):
    run()
    sys.exit(0)

if 	(sys.argv[1]=="test"):
	test()
	sys.exit(0)
