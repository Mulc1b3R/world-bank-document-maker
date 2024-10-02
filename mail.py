import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass
import os
import zipfile

def zip_folder(folder_path, zip_filename):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            file_path = os.path.join(folder_path, file)
            zipf.write(file_path, os.path.basename(file_path))

    print(f"All files in '{folder_path}' zipped to '{zip_filename}' successfully.")

def send_email(sender_email, recipient_email, subject, body, attachment_filename):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(attachment_filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {attachment_filename}")
    msg.attach(part)

    password = getpass("Enter your email password: ")

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()

    print(f"Email with attachment '{attachment_filename}' sent successfully!")

# Folder path containing files to be zipped and sent
folder_path = "path/to/folder"
zip_filename = "output.zip"

# Zip the folder
zip_folder(folder_path, zip_filename)

# Email details
sender_email = "your_email@gmail.com"
recipient_email = "recipient_email@example.com"
subject = "Email with zipped folder attachment"
body = "Please find the zipped folder attached."

# Send email with zipped file as attachment
send_email(sender_email, recipient_email, subject, body, zip_filename)