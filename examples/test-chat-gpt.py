# Function to send an email

def send_email(recipient, subject, body):
    import smtplib

    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    # start TLS for security 
    s.starttls() 

    # Authentication 
    s.login("sender_email_id", "sender_email_id_password") 

    # message to be sent 
    message = "Subject: {}\n\n{}".format(subject, body)

    # sending the mail 
    s.sendmail("sender_email_id", recipient, message) 

    # terminating the session 
    s.quit()
