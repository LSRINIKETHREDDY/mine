from flask import Flask, render_template, request
import smtplib
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=TEMPLATES_DIR)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('mainpage.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    mail_sent = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        subject = f"Contact Form Submission from {name}"
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login('ghanisriniketh@gmail.com', 'dcmg pqxk xlwl kocj')  # Use your Gmail and app password
                msg = f"Subject: {subject}\n"
                msg += f"From: EduHub <ghanisriniketh@gmail.com>\n"
                msg += f"Reply-To: {email}\n"
                msg += f"\nName: {name}\nEmail: {email}\nMessage: {message}"
                server.sendmail('ghanisriniketh@gmail.com', 'ghanisriniketh@gmail.com', msg)
            mail_sent = True
        except Exception as e:
            print("Mail send error:", e)
            mail_sent = False
        return render_template('thanks.html', mail_sent=mail_sent)
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html')

@app.route('/cse')
def cse():
    return render_template('cse.html')

@app.route('/ece')
def ece():
    return render_template('ece.html')

@app.route('/eee')
def eee():
    return render_template('eee.html')

@app.route('/mech')
def mech():
    return render_template('mech.html')

if __name__ == '__main__':
    app.run(debug=True)
