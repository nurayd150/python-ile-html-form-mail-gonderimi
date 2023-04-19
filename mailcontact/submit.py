from email.mime.multipart import MIMEMultipart
import os
from smtplib import SMTP
from email.message import EmailMessage
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit_form1', methods=['POST'])
def submit_form():
    print(os.getcwd())
    print(os.path.isfile('submit.py'))
    name = request.form['namecontact']
    email = request.form['mailcontact']
    message = request.form['commentcontact']

    mail = SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login("mailadresim@gmail.com", "password")
    mesaj = MIMEMultipart()
    mesaj["From"] = email       # Gönderen kişi
    mesaj["To"] = " mailadresim@gmail.com"          # Alıcı

    mesaj["Subject"] = mail +"'dan gelen mesaj"  # Konu

    body = "name:%s"%name+ "\n "+"mail:%s"%email+"\n"+"comment:%s"%message

    body_text = MIMEText(body, "plain")  
    mesaj.attach(body_text)
    mail.sendmail(mesaj["From"] ,mesaj["To"],mesaj.as_string()) 
    print("Mail başarılı bir şekilde gönderildi.")
    mail.close()
    # with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
    #     smtp.starttls()
    #     smtp.login("nurayd150@gmail.com", "eruimousqsiculno")
    #     smtp.send_message(msg)

    return redirect(url_for('index'))

@app.route('/thank-you')
def thank_you():
    return 'Thank you for your message!'

if __name__ == '__main__':
    app.run(debug=True)
