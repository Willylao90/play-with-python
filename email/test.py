"""The first step is to create an SMTP object, each object is used for
connection 
with one server."""

import smtplib
server = smtplib.SMTP()
server.set_debuglevel(True)
server.connect('smtp.live.com', 25)
server.ehlo()
server.starttls()
server.ehlo()
#Next, log in to the server
server.login("test79058350@hotmail.com", "seCurity7905")

#Send the mail
msg = "\nThis is a Test!" # The /n separates the message from the headers
server.sendmail("test79058350@hotmail.com", "duncan.kennaugh@renishaw.com", msg)
