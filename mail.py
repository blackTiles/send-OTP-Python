from flask import Flask
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/")
def index():
    sender_email = "sender_email@gmail.com"
    password = "password"
    receiver_email = "receiver_email@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "OTP verification"
    otp = "727872"
    message["From"] = sender_email
    message["To"] = receiver_email
    html = """\
            <html>
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                <div style="align-items:center;">
                    <div style="margin:0px auto;text-align:center;"><img src="https://scontent.fpat2-1.fna.fbcdn.net/v/t1.0-0/p526x296/149769738_232347528522986_2842490704685962839_o.jpg?_nc_cat=104&ccb=3&_nc_sid=730e14&_nc_ohc=ehEWDBits3AAX-u6VhH&_nc_ht=scontent.fpat2-1.fna&tp=6&oh=fc8c17661e83077ade1ac030f14e973b&oe=604D9EC8" width="100" height="100" /></div>
                    <br />
                    <h1 style="font-family:sans-serif; color:grey;text-align:center;">Email Confirmation OTP</h1>
                    <br />
                    <h1 style="font-family:sans-serif; padding:10px; border: 2px dashed black;text-align:center;">{}</h1>
                    <br />
                    <p style="text-align:center">Thank you for being a member of black tiles</p>
                    <hr />
                </div>
            </body>
            </html>
            """.format(otp)
    part1 = MIMEText(html, "html")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    return "Email sent"

if __name__ == '__main__':
   app.run(debug = True)