
from flask_mail import Message, Mail


mail = Mail()


def send_mail(msg_to, msg_subject, msg_body="", msg_html=""):
    msg = Message(msg_subject, recipients=[msg_to])
    msg.body = msg_body
    msg.html = msg_html
    # with app.open_resource("image.jpg") as fp:
    #     msg.attach("mage.jpg", "image/jpg", fp.read())
    mail.send(msg)

def send_mail_confirm_email(msg_to, token):
    send_mail(msg_to=msg_to,
              msg_subject='Molimo vas verifikujte vašu email adresu',
              msg_html=f'''
                    <html>
                    <head>
                        <title>Email Verification</title>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link href="https://fonts.googleapis.com/css?family=Helvetica" rel="stylesheet">
                    </head>
                    <body style="margin: 0; padding: 0; font-family: Tahoma; font-size: 16px; text-align: left;">
                        <table cellpadding="0" cellspacing="0" width="100%" style="background-color: #f8f8f8;">
                            <tr>
                                <td align="">
                                    <table cellpadding="0" cellspacing="0" width="520" style="background-color: #ffffff;">
                                        <tr>
                                            <td style="padding: 20px;">
                                                <h1 style="margin-top: 0;">Verifikujte vašu email adresu</h1>
                                                <p style="margin-bottom: 20px;">Hvala što ste se registrovali kod nas. Molimo vas kliknite dugme ispod kako bi ste se verifikovali vašu email adresu.</p>
                                                <a href="127.0.0.1:5000/auth/{msg_to}/{token}" style="background-color: #4CAF50; color: #ffffff; display: inline-block; padding: 10px 20px; text-decoration: none; font-size: 14px; border-radius: 5px;">VERIFIKUJ EMAIL</a>
                                                <p style="margin-top: 20px;">Ako se niste registrovali kod nas, molimo vas ignorišite ovaj mail.</p>
                                                <p style="font-size: 12px; text-decoration: none; color: black; ">
                                                    *U slučaju da dugme ne radi, kliknite na link ispod:
                                                    <br>
                                                    127.0.0.1:5000/auth/{msg_to}/{token}
                                                </p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </body>
                    </html>
                       ''')

