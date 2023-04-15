import os
import hashlib
import subprocess
import time
import smtplib
from subprocess import Popen, PIPE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


dir_path = "C:\\Users\\mhpc\\Desktop\\private"

#input your password recieved by google after enabling use of less secure apps
#email addresses to be modifies according to need
sender_email = "ruchirrfor9@gmail.com"
sender_password = 'xxxxxxxxx'
recipient_email = "lranjitaa@gmail.com"


current_files = {}

def hash_file(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

# Function to send an email message
def send_email(subject, body, attachment_path=None):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient_email

    body_text = MIMEText(body)
    message.attach(body_text)


    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(message)

    print("Email sent successfully!")

for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)
    if os.path.isfile(file_path):
        current_files[filename] = hash_file(file_path)

while True:
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            current_hash = hash_file(file_path)

            if current_files.get(filename) != current_hash:
               
                print(f"File {filename} has changed!")
                current_files[filename] = current_hash
                
                subject = f"Change detected"
                body = f"File {filename} has changed in directory {dir_path}."
                attachment_path = file_path
                send_email(subject, body, attachment_path)
                subprocess.run(["python", "step3.py"])

    time.sleep(1)
