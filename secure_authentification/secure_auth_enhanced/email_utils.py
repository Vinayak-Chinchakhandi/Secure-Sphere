import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_code(receiver_email, code):
    sender = '23u0036@students.git.edu'
    password = 'qrsr hewz dbty yzvy'  # App password

    message = MIMEMultipart("alternative")
    message["Subject"] = "🔐 Your Verification Code"
    message["From"] = sender
    message["To"] = receiver_email

    # Plain text (fallback)
    text = f"Your verification code is: {code}"

    # HTML version with bold and large font
    html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; padding: 20px;">
        <p style="font-size: 20px; font-weight: bold; color: #333;">
          Dear User,<br><br>
          You have initiated a secure login process.<br><br>
          Please use the following verification code to continue:
        </p>
        <p style="font-size: 28px; font-weight: bold; color: #2a7ae2;">
          {code}
        </p>
        <p style="font-size: 18px; font-weight: bold; color: #333;">
          If you did not request this, please ignore this message.<br><br>
          Thank you,<br>
          The Security Team
        </p>
      </body>
    </html>
    """

    # Attach both plain text and HTML
    message.attach(MIMEText(text, "plain"))
    message.attach(MIMEText(html, "html"))

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver_email, message.as_string())