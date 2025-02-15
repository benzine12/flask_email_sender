# app.py
import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("gmail account email", "app password")
# message to be sent
message = "Hey bogogaga just send this email from flask app!"
# sending the mail
s.sendmail("sender email", "receiver email", message)
# terminating the session
s.quit()