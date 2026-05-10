from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Email configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SENDER_EMAIL = os.getenv('SENDER_EMAIL', 'your-email@gmail.com')
SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', 'your-app-password')
RECIPIENT_EMAIL = 'rachaittalwar@gmail.com'

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        
        # Validate input
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', 'Portfolio Contact Form').strip()
        message = data.get('message', '').strip()
        
        print(f"[FORM] Received: name={name}, email={email}, subject={subject}")
        
        if not all([name, email, message]):
            print("[ERROR] Missing required fields")
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        # Validate email format
        if '@' not in email or '.' not in email:
            print("[ERROR] Invalid email format")
            return jsonify({'success': False, 'error': 'Invalid email format'}), 400
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"Portfolio: {subject}"
        
        # Email body
        body = f"""
New message from portfolio contact form:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        print(f"[MAIL] Attempting to send from {SENDER_EMAIL} to {RECIPIENT_EMAIL}")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            print(f"[MAIL] TLS enabled")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print(f"[MAIL] Login successful")
            server.send_message(msg)
            print(f"[MAIL] Message sent successfully")
        
        return jsonify({'success': True, 'message': 'Email sent successfully'}), 200
    
    except Exception as e:
        error_msg = str(e)
        print(f"[ERROR] Exception: {error_msg}")
        return jsonify({'success': False, 'error': f'Failed to send email: {error_msg}'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
