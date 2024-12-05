import os

class Config:
    GMAIL_ADDRESS = "mejorsaludmental@gmail.com"
    GMAIL_APP_PASSWORD = os.getenv('APP_MAIL_PASS')  # Set via environment variable
    RECAPTCHA_SECRET_KEY = os.getenv("CAPTCHA_SECRET_KEY")  # Set via environment variable
