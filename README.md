# Email Sender

A simple Python project demonstrating two different approaches to sending emails: using Flask-Mail and using the built-in `smtplib` library.

## Features

- Send emails using Flask-Mail extension
- Send emails using Python's built-in `smtplib` library
- Support for Gmail SMTP server
- TLS encryption for secure email transmission

## Prerequisites

- Python 3.x
- Gmail account
- Gmail App Password (2FA must be enabled)

## Installation

1. Clone the repository or download the source code
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, you need to configure your Gmail credentials:

1. Enable 2-Factor Authentication in your Gmail account
2. Generate an App Password:
   - Go to your Google Account settings
   - Navigate to Security
   - Under "Signing in to Google," select App Passwords
   - Generate a new App Password for the application

3. Update the credentials in both files:

In `main.py`:
```python
app.config['MAIL_USERNAME'] = 'your.email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'
```

In `app.py`:
```python
s.login("your.email@gmail.com", "your-app-password")
```

## Usage

### Using Flask-Mail (main.py)

1. Run the Flask application:
```bash
python main.py
```
2. Visit `http://localhost:5000` in your browser to send a test email

### Using smtplib (app.py)

1. Run the script:
```bash
python app.py
```

## Security Notes

- Never commit your email credentials to version control
- Consider using environment variables for sensitive information
- Always use App Passwords instead of your main Gmail password

## File Structure

```
email-sender/
├── main.py          # Flask-Mail implementation
├── app.py           # smtplib implementation
├── requirements.txt # Project dependencies
└── README.md
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.