# main.py
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'gmail account email'  # Use your actual Gmail address
app.config['MAIL_PASSWORD'] = 'app password'     # Use your generated App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index():
    msg = Message(
        subject='Hello from the other side!', 
        sender='gmail account email', 
        recipients=['receiver email'] 
    )
    msg.body = "Hey bogogaga just send this email from flask app!"
    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)