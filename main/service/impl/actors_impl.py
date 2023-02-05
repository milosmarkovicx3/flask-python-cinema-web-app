from service.utility.logger import log
from service.utility.utility import toJSON
from entities.core.result import Result
from entities.facade import actors_facade as af
from entities.models.actors import actors

def get_by_id(id):
    try:
        result = Result(item = af.get_by_id(id))
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'

def get_by_name(name):
    try:
        result = Result(item = af.get_by_name(name))
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'

def get_all():
    try:
        result = Result(item = af.get_all())
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'

# def create(data):
#     try:
#         form =  WTFInsertActor()
#         if not form.validate():
#             return "Loša validacija forme!"
#
#         name = request.form['name']
#         actorFile = request.files['actorFile']
#
#         filename = secure_filename(actorFile.filename)
#         app.config['UPLOAD_FOLDER'] = 'static/resources/actors-images/'
#
#         returnMessage = "Uspešan unos u bazu!"
#
#         db = pymysql.connect(host="localhost", port=3306, user="root", passwd="", db="cinema")
#         cursor = db.cursor()
#         try:
#             cursor.execute( f"insert into actors(name,image) values('{name}','{filename}')")
#             actorFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             db.commit()
#         except Exception as e:
#             print(e)
#             db.rollback()
#             returnMessage = "Greška pri izvršavanju sql upita ili otpremanju slike! \n" + str(e)
#         db.close()
#
#         return returnMessage
#
#
#         actor = actors(data['name'], data['image'])
#         result = Result(item = af.create(actor))
#         if result.get_item() is None:
#             result.set_status(Result.NOT_FOUND)
#         return toJSON(result)
#     except Exception as e:
#         log.error(e)
#         return f'Dogodila se greška! [ {str(e)} ]'

def delete_by_id(id):
    try:
        result = Result(item = af.delete_by_id(id))
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'