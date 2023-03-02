import smtplib
import datetime
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'prasidh2904agg@gmail.com'  # Replace with your email address
SMTP_PASSWORD =  os.environ.get('SMTP_PASSWORD') # Replace with your email password
EMAIL_TO = 'aprasidh@gmail.com'  # Replace with the recipient's email address
EMAIL_SUBJECT = 'Stopped EC2 instance'  # Replace with the subject of the email
current_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
EMAIL_BODY = f'There were issues with stopping the instance.'  # Updated body

# Send email
smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp_server.starttls()
smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
email_message = f'To: {EMAIL_TO}\nSubject: {EMAIL_SUBJECT}\n\n{EMAIL_BODY}'
smtp_server.sendmail(SMTP_USERNAME, EMAIL_TO, email_message)
smtp_server.quit()
