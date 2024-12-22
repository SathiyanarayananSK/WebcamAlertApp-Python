import smtplib
import mimetypes
from email.message import EmailMessage
import os

MAIL_ID = "ssk98.automations@gmail.com"
PASSWORD = os.getenv("WebcamMotionDetector")

def send_email(image_path):
    # Create email message
    email_message = EmailMessage()
    email_message["Subject"] = "Webcam Alert"
    email_message.set_content("New object detected!")

    # Determine MIME type
    mime_type, _ = mimetypes.guess_type(image_path)
    maintype, subtype = mime_type.split('/') if mime_type else ('application', 'octet-stream')

    # Attach the image
    with open(image_path, "rb") as file:
        content = file.read()
        email_message.add_attachment(content, maintype=maintype, subtype=subtype)

    # Send the email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()

    # Replace MAIL_ID and PASSWORD with your credentials
    gmail.login(MAIL_ID, PASSWORD)

    # Ensure MAIL_ID and PASSWORD are defined
    gmail.sendmail(MAIL_ID, MAIL_ID, email_message.as_string())
    # Close the connection
    gmail.quit()



    
