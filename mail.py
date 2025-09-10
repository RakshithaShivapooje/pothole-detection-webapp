from email.message import EmailMessage
import ssl
import smtplib
import os

def send_email(cont_dic, mail_receiver):
    # Set up email sender and password (use environment variables or secure storage for better security)
    mail_sender = 'potholedetection06@gmail.com'  # Replace with your Gmail address
    mail_password = 'lkexnwcfdzwrcrll' # Use environment variable' for password or set an App Password

    # Subject and body for the email
    subject = 'Complaint Register'
    body = f"Potholes are identified at location: {cont_dic['location']}. It's a {cont_dic['highway_type']} that contains {cont_dic['size']}. Take necessary actions."

    # Create the email
    em = EmailMessage()
    em['From'] = mail_sender
    em['To'] = mail_receiver
    em['Subject'] = subject  # Make sure the header is capitalized correctly

    em.set_content(body)

    # Establish a secure SSL connection and send the email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(mail_sender, mail_password)
            smtp.sendmail(mail_sender, mail_receiver, em.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

