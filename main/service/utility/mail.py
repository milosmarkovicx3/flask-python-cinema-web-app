from flask_mail import Message, Mail


mail = Mail()
app_url = 'https://arhiv.pythonanywhere.com'

def send_mail(msg_to, msg_subject, msg_html=''):
    msg = Message(msg_subject, recipients=[msg_to])
    msg.html = msg_html
    with open('static/resources/images/arhiv_logo.jpg', 'rb') as fp:
        image_data = fp.read()
    msg.attach('image.jpg', 'image/jpeg', image_data, 'inline', headers=[('Content-ID', '<arhiv_logo>')])
    mail.send(msg)

def send_mail_confirm_email(username, msg_to, token):
    send_mail(msg_to=msg_to,
              msg_subject='Arhiv: molimo vas verifikujte vašu email adresu',
              msg_html=f'''
                    <html>
                    <head>
                        <title>Email Verification</title>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body style="margin: 0; padding: 0; font-family: 'Trebuchet MS', 'Sans Serif'; font-size: 16px; ">
                        <div style="padding: 40px; background-color: #efefef; border-radius: 40px; width: 350px; margin: auto; border: 1px solid black;">
                              <div style="width: 350px; display: flex; justify-content<img src="cid:arhiv_logo">
                              <div style="border: 2px solid gray; background-color: #fafafa;padding: 0 15px; display: flex">
                                  <div>
                                    <h2>Dobrodošao, {username}</h2>
                                    <p>
                                      Hvala što ste se registrovali kod nas.
                                      <br><br>
                                      Molimo vas kliknite dugme ispod kako bi ste se verifikovali vašu email adresu.
                                    </p>
                                  </div>
                                </div>
                              <br>
                              <a href="{app_url}/confirm-email?email={msg_to}&token={token}" style="border: 1px solid black; text-align: center; width: calc(100% - 40px); background-color: #7630f3; color: #ffffff; display: inline-block; padding: 10px 20px; text-decoration: none;  border-radius: 20px;">Verifikuj email</a>
                              <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <p>Srdačan pozdrav,<br>Arhiv</p>
                                    <img src="cid:arhiv_logo" style="width: 50px; height: 50px;">
                              </div>
                              <hr>
                              <p style="margin: 0;">Ako se niste registrovali kod nas, molimo vas ignorišite ovaj mail.</p>
                        </div>
                    </body>
                    </html>
                       ''')

