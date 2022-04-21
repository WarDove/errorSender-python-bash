import smtplib

#subject generator
with open('/home/terminal/atm/bin/errorSender/pointId', 'r') as file:
    pointname = file.read()

with open('error_list', 'r') as file2:
    message = file2.read()

#e-mail sender function
def gmailsender(toaddr, subject, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    from os.path import basename
    fromaddr = "nakh.sc.errors@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, "plain"))
    attach_file_name = 'paylog.zip'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    #payload.add_header('Content-Decomposition', 'attachment',  filename="asd.asd")
    payload['Content-Disposition'] = 'attachment; filename="%s"' % basename(attach_file_name)
    msg.attach(payload)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.connect("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, "smartpay")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

#e-mail variables
toaddr = "tarlan@huseynov.net"
subject = pointname
gmailsender(toaddr, subject, message)


