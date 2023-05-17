from flask_mail import Message, Mail
from config import STATIC_DIR_PATH

mail = Mail()
app_url = 'https://arhiv.pythonanywhere.com'


def send_mail(msg_to, msg_subject, msg_html=''):
    msg = Message(msg_subject, sender=('Arhiv', 'arhiv.bioskop@gmail.com'), recipients=[msg_to])
    msg.html = msg_html
    with open(f'{STATIC_DIR_PATH}/resources/images/arhiv_logo.jpg', 'rb') as fp:
        image_data = fp.read()
    msg.attach('arhiv_logo.jpg', 'image/jpeg', image_data, 'inline', headers=[('Content-ID', '<arhiv_logo>')])
    # <img src="cid:arhiv_logo">
    # <img src="{app_url}/resource/images/arhiv_logo.jpg"
    mail.send(msg)


def send_mail_confirm_email(msg_to, username, token):
    send_mail(msg_to=msg_to,
              msg_subject='Arhiv: molimo vas verifikujte vašu email adresu',
              msg_html=f'''
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body style="margin: 0; padding: 0; font-family: 'Trebuchet MS', 'Sans Serif'; font-size: 16px; ">
                        <div style="padding: 40px; background-color: #efefef; border-radius: 40px; width: 350px; margin: auto; border: 1px solid black;">
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
                              <div style="display: flex;">
                                    <p>Srdačan pozdrav,<br>Arhiv</p>
                                    <img src="cid:arhiv_logo" width="50" height="50" title="logo" alt="logo" style="display:block; width: 50px; height: 50px; margin: auto 0 auto auto;">
                              </div>
                              <hr>
                              <p style="margin: 0;">Ukoliko se niste registrovali kod nas, molimo vas ignorišite ovaj mail.</p>
                        </div>
                    </body>
                    </html>
                       ''')

def send_mail_create_reservation(msg_to, reservation_id, movie, date, time, seat):
    send_mail(msg_to=msg_to,
              msg_subject=f'Arhiv: kreirana nova rezervacija',
              msg_html=f'''
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body style="margin: 0; padding: 0; font-family: 'Trebuchet MS', 'Sans Serif'; font-size: 16px; ">
                        <div style="padding: 40px; background-color: #efefef; border-radius: 40px; width: 350px; margin: auto; border: 1px solid black;">
                              <div style="border: 2px solid gray; background-color: #fafafa;padding: 0 15px; display: flex">
                                  <div>
                                    <h2>Poštovani,</h2>
                                    <p>
                                      Rezervacija kreirana pod brojem #{reservation_id}.
                                      <br><br>
                                      Naziv filma: {movie} <br>
                                      Datum projekcije: {date} <br>
                                      Vreme projekcije: {time} <br>
                                      Sedište: {seat}
                                    </p>
                                  </div>
                              </div>
                              <br>
                              <div style="display: flex;">
                                    <p>Srdačan pozdrav,<br>Arhiv</p>
                                    <img src="cid:arhiv_logo" width="50" height="50" title="logo" alt="logo" style="display:block; width: 50px; height: 50px; margin: auto 0 auto auto;">
                              </div>
                        </div>
                    </body>
                    </html>
                       ''')

def send_mail_login_new_ip(msg_to, ip_adress):
    send_mail(msg_to=msg_to,
              msg_subject=f'Arhiv: prijavljivanje sa nove lokacije',
              msg_html=f'''
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body style="margin: 0; padding: 0; font-family: 'Trebuchet MS', 'Sans Serif'; font-size: 16px; ">
                        <div style="padding: 40px; background-color: #efefef; border-radius: 40px; width: 350px; margin: auto; border: 1px solid black;">
                              <div style="border: 2px solid gray; background-color: #fafafa;padding: 0 15px; display: flex">
                                  <div>
                                    <h2>Poštovani,</h2>
                                    <p>
                                        Primetili smo novu prijavu na vašem nalogu sa ip adrese: {ip_adress}. 
                                        Ukoliko ste to vi, onda nema potrebe da preduzimate bilo kakve mere. 
                                        U suprotnom, sigurnosne kredencijale možete promeniti u okviru podešavanja vašeg naloga.
                                    </p>
                                  </div>
                              </div>
                              <br>
                              <div style="display: flex;">
                                    <p>Srdačan pozdrav,<br>Arhiv</p>
                                    <img src="cid:arhiv_logo" width="50" height="50" title="logo" alt="logo" style="display:block; width: 50px; height: 50px; margin: auto 0 auto auto;">
                              </div>
                        </div>
                    </body>
                    </html>
                       ''')

def send_mail_forgotten_password(msg_to, token):
    send_mail(msg_to=msg_to,
              msg_subject='Arhiv: pokrenuta je procedura promene lozinke',
              msg_html=f'''
                    <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body style="margin: 0; padding: 0; font-family: 'Trebuchet MS', 'Sans Serif'; font-size: 16px; ">
                        <div style="padding: 40px; background-color: #efefef; border-radius: 40px; width: 350px; margin: auto; border: 1px solid black;">
                              <div style="border: 2px solid gray; background-color: #fafafa;padding: 0 15px; display: flex">
                                  <div>
                                    <h2>Poštovani, </h2>
                                    <p>
                                      Na vašem nalogu pokrenuta je procedura promene lozinke.
                                      <br><br>
                                      Molimo vas kliknite dugme ispod kako bi nastavili.
                                    </p>
                                  </div>
                              </div>
                              <br>
                              <a href="{app_url}/nova-lozinka?email={msg_to}&token={token}" style="border: 1px solid black; text-align: center; width: calc(100% - 40px); background-color: #7630f3; color: #ffffff; display: inline-block; padding: 10px 20px; text-decoration: none;  border-radius: 20px;">Verifikuj email</a>
                              <div style="display: flex;">
                                    <p>Srdačan pozdrav,<br>Arhiv</p>
                                    <img src="cid:arhiv_logo" width="50" height="50" title="logo" alt="logo" style="display:block; width: 50px; height: 50px; margin: auto 0 auto auto;">
                              </div>
                              <hr>
                              <p style="margin: 0;">Ukoliko vi niste pokrenuli proceduru zamene lozinke, molimo vas ignorišite ovaj mail.</p>
                        </div>
                    </body>
                    </html>
                       ''')