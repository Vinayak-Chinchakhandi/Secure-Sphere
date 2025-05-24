from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
from email_utils import send_verification_code

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/send-code', methods=['POST'])
def send_code():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        flash("❌ Passwords do not match.")
        return redirect(url_for('index'))

    code = str(random.randint(100000, 999999))
    session['username'] = username
    session['email'] = email
    session['password'] = password
    session['code'] = code

    send_verification_code(email, code)
    flash("✅ Verification code sent to your email.")
    return redirect(url_for('verify'))

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/check-code', methods=['POST'])
def check_code():
    entered_code = request.form['code']
    if entered_code == session.get('code'):
        username = session.get('username')
        return render_template('success.html', username=username)
    else:
        flash("❌ Invalid verification code.")
        return redirect(url_for('verify'))

if __name__ == '__main__':
    app.run(debug=True,port=2000)