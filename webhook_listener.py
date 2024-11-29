from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_listener():
    # Parse the webhook payload
    data = request.json  # Ensure the webhook sends JSON
    
    # Extract necessary data
    event = data.get('event', 'Unknown event')
    details = data.get('details', 'No details provided')
    
    # Send an email
    send_email(f"Event: {event}", f"Details: {details}")
    return "Webhook received and email sent", 200

def send_email(subject, body):
    # Email configuration
    sender_email = "no-reply@unicamp.br"
    receiver_email = "massakiwillian@gmail.com"
    smtp_server = "mailing.extecamp.unicamp.br"
    smtp_port = 587
    smtp_password = "*Pro@SQ"
    
    # Create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    app.run(port=5000)
