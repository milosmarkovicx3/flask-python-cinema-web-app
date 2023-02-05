#from WTForms import *

from flask import Flask

from service.utility.logger import project_path
app = Flask(__name__, template_folder=f'{project_path}templates')
# csrf = CSRFProtect()
# csrf.init_app(app)
app.config["SECRET_KEY"] = 'development key'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['RECAPTCHA_USE_SSL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcMkHshAAAAAOsgybf6CkOi9R0vXugojWzTMqTl'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcMkHshAAAAACIX71ZTnSDZ-6XuobY8i0micU5W'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'dark'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cinema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#
# @app.errorhandler(413)
# def fileSizeError(e):
#     print("[error: 413] Veličina datoteke prelazi dozvoljenu granicu!")
#
#

# @app.route('/EditDatabase', methods=['GET','POST'])
# def EditDatabase():
#     return render_template('EditDatabase.html', formMovie=WTFInsertMovie(), formActor=WTFInsertActor(), formGenre=WTFInsertGenre())


# def registerUser(req):
#     first_name = req.form['first-name']
#     last_name = req.form['last-name']
#     email = req.form['email']
#     password = req.form['password']
#
#     sqlList = []
#     sql = "insert into users(first_name,last_name,email,password) values('%s','%s','%s','%s') " % (first_name,last_name,email,password)
#     sqlExecute(sql)

# #---------------------------------------------------------------------------------------------------
#
# @app.route('/insertMovie', methods=['POST'])
# def insertMovie():
#     form =  WTFInsertMovie()
#     if not form.validate():
#         return "Loša validacija forme!"
#
#     title = request.form['title']
#     year = request.form['year']
#     duration = request.form['year']
#     rating = request.form['rating']
#     votes = request.form['votes']
#     posterFile = request.files['posterFile']
#     genresId = request.form['genresId'].split(':')
#     actorsId = request.form['actorsId'].split(':')
#     actorsRoles = request.form['actorsRoles'].split(':')
#
#     filename = secure_filename(posterFile.filename)
#     app.config['UPLOAD_FOLDER'] = 'static/resources/movies-poster/'
#
#     returnMessage = "Uspešan unos u bazu!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute(f"insert into movies(title,year,duration,rating,votes,poster) values('{title}','{year}','{duration}','{rating}','{votes}','{filename}')")
#         cursor.execute("select last_insert_id()")
#         movieId = cursor.fetchone()
#         for x in range(0, len(genresId)):
#             cursor.execute(f"insert into movie_genre(id_movie,id_genre) values('{movieId}','{genresId[x]}')")
#         for x in range(0, len(actorsId)):
#             cursor.execute(f"insert into movie_actor(id_movie,id_actor,role) values('{movieId}','{actorsId[x]}','{actorsRoles[x]}')")
#
#         posterFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita ili otpremanju postera! \n" + str(e)
#     db.close()
#
#     return returnMessage
#
# @app.route('/deleteMovie', methods=['POST'])
# def deleteMovie():
#     id_movie = request.form['uuid']
#
#     returnMessage = "Uspešano izvršena operacija!!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute(f"delete from movies where id_movie={id_movie}")
#         cursor.execute(f"delete from movie_actor where id_movie={id_movie}")
#         cursor.execute(f"delete from movie_genre where id_movie={id_movie}")
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita! \n" + str(e)
#     db.close()
#
#     return returnMessage
# #---------------------------------------------------------------------------------------------------
#
#
# @app.route('/insertActor', methods=['POST'])
# def insertActor():
#     form =  WTFInsertActor()
#     if not form.validate():
#         return "Loša validacija forme!"
#
#     name = request.form['name']
#     actorFile = request.files['actorFile']
#
#     filename = secure_filename(actorFile.filename)
#     app.config['UPLOAD_FOLDER'] = 'static/resources/actors-images/'
#
#     returnMessage = "Uspešan unos u bazu!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute( f"insert into actors(name,image) values('{name}','{filename}')")
#         actorFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita ili otpremanju slike! \n" + str(e)
#     db.close()
#
#     return returnMessage
#
# @app.route('/deleteActor', methods=['POST'])
# def deleteActor():
#     id_actor = request.form['uuid']
#
#     returnMessage = "Uspešano izvršena operacija!!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute(f"select * from movie_actor where id_actor={id_actor}")
#         data = cursor.fetchone()
#         if data:
#             returnMessage = "Brisanje otkazano! Postoji film sa datim glumcom!"
#             return returnMessage
#         cursor.execute(f"delete from actors where id_actor={id_actor}")
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita! \n" + str(e)
#     db.close()
#     return returnMessage
# #---------------------------------------------------------------------------------------------------
# @app.route('/insertGenre', methods=['POST'])
# def insertGenre():
#     form =  WTFInsertGenre()
#     if not form.validate():
#         return "Loša validacija forme!"
#
#     genre = request.form['genre']
#     genreFile = request.files['genreFile']
#
#     filename = secure_filename(genreFile.filename)
#     app.config['UPLOAD_FOLDER'] = 'static/resources/genres-images/'
#
#     returnMessage = "Uspešan unos u bazu!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute(f"insert into genres(genre,image) values('{genre}','{filename}')")
#         genreFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita ili otpremanju slike! \n" + str(e)
#     db.close()
#
#     return returnMessage
#
# @app.route('/deleteGenre', methods=['POST'])
# def deleteGenre():
#     id_genre = request.form['uuid']
#
#     returnMessage = "Uspešano izvršena operacija!!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute(f"select * from movie_genre where id_genre={id_genre}")
#         data = cursor.fetchone()
#         if data:
#             returnMessage = "Brisanje otkazano! Postoji film sa datim žanrom!"
#             return returnMessage
#         cursor.execute(f"delete from genre where id_genre={id_genre}")
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita! \n" + str(e)
#     db.close()
#     return returnMessage
# #---------------------------------------------------------------------------------------------------
# def sqlSelect(sql):
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     data = []
#     try:
#         cursor.execute(sql)
#         db.commit()
#         data = cursor.fetchall()
#     except Exception as e:
#         print(e)
#         db.rollback()
#     db.close()
#     return jsonify(data)
#
# def sqlExecute(sql):
#     returnMessage = "Uspešano izvršena operacija!!"
#
#     db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#     cursor = db.cursor()
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except Exception as e:
#         print(e)
#         db.rollback()
#         returnMessage = "Greška pri izvršavanju sql upita! \n" + str(e)
#     db.close()
#     return returnMessage
# #---------------------------------------------------------------------------------------------------
# @app.route('/registerUser', methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         if request.form['request'] == 'registerUser':
#             registerUser(request)
#






from entities.core.base import db
from web.rest_api.genres_api import genres_api
from web.rest_api.actors_api import actors_api
from web.rest_api.movies_api import movies_api


app.register_blueprint(actors_api, url_prefix='/actors')
app.register_blueprint(genres_api, url_prefix='/genres')
app.register_blueprint(movies_api, url_prefix='/movies')






db.init_app(app)
app.app_context().push()
db.create_all()



    #show_all()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
