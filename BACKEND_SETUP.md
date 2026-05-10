# Portfolio Backend Setup

This backend receives contact form submissions and sends them to your email via SMTP.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings

**For Gmail:**
1. Go to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Generate an app-specific password (16 characters)
3. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
4. Edit `.env` and fill in:
   ```
   SENDER_EMAIL=your-email@gmail.com
   SENDER_PASSWORD=your-16-char-app-password
   ```

### 3. Run the Backend
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 4. Test the Form
Open `rachait_talwar_portfolio.html` and submit the contact form. Messages should now arrive in your inbox.

## Deployment

For production, deploy to:
- **Heroku** (Free tier available)
- **Replit** (Free Python hosting)
- **PythonAnywhere** (Free tier)
- **DigitalOcean** (Affordable VPS)

Make sure to set environment variables on your hosting platform instead of using `.env`.

## Environment Variables

- `SMTP_SERVER`: SMTP server (default: smtp.gmail.com)
- `SMTP_PORT`: SMTP port (default: 587)
- `SENDER_EMAIL`: Your email address
- `SENDER_PASSWORD`: App-specific password or regular password
- `RECIPIENT_EMAIL`: Where to send messages (default: rachaittalwar@gmail.com)

## Troubleshooting

### "Connection refused" error
- Make sure backend is running: `python app.py`
- Check that port 5000 is not blocked

### "Authentication failed" error
- Verify SENDER_EMAIL and SENDER_PASSWORD in `.env`
- For Gmail, use an app-specific password, not your regular password

### Messages not arriving
- Check spam/promotions folder
- Verify email credentials are correct
- Check Flask console for error messages
