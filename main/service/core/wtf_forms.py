from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileAllowed
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, HiddenField, FileField
from wtforms.validators import DataRequired, Email, Length, ValidationError

def length(min=-1, max=-1):
    message = f"Unos mora biti dužine od {min} do {max} karaktera!"
    def _length(form, field):
        l = field.data and len(field.data.strip(" ")) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length

# def size(max=-1):
#     message = f"Veličina mora biti manja od {max}MB!"
#     max_bytes = max*1024*1024
#     def _size(form, field):
#         if len(field.data.read()) > max_bytes:
#             raise ValidationError(message)
#         field.data.seek(0)
#     return _size

# def end_with():
#     message = "Pogrešna ekstenzija slike"
#     def _end_with(form, field):
#         l = field.data
#         if not l.endswith('png') and not l.endswith('jpg') and not l.endswith('jpeg') :
#             raise ValidationError(message)
#     return _end_with


class wtf_create_movie(FlaskForm):
    title = StringField("Naslov: ", validators=[length(min=2,max=100)], render_kw={"placeholder": "npr. Star Wars: Episode IV - A New Hope"})
    year = StringField("Godina: ", validators=[length(min=4,max=4)], render_kw={"placeholder": "npr. 1977"})
    duration = StringField("Trajanje: ", validators=[length(min=2,max=6)], render_kw={"placeholder": "npr. 2h 1m"})
    rating = StringField("Rejting: : ", validators=[length(min=2,max=6)], render_kw={"placeholder": "npr. 8.6"})
    votes = StringField("Glasovi: ", validators=[length(min=2,max=6)], render_kw={"placeholder": "npr. 1.3M"})
    poster = StringField("Poster (2:3): ", validators=[], render_kw={"placeholder": "npr. C:\\fakepath\\star_wars_iv.png", "readonly": "true"})
    posterFile = FileField("Izaberi", validators=[FileAllowed(['png','jpg','jpeg'])], render_kw={"accept": ".png, .jpg, .jpeg"})
    submit = SubmitField("Pošalji zahtev")
    # recaptcha = RecaptchaField()
    genresSearch = StringField("Žanrovi: ", render_kw={"placeholder": "npr. Fantasy"})
    actorsSearch = StringField("Glumci: ", render_kw={"placeholder": "npr. Mark Hamill"})




    # Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    # Insertress = TextAreaField("Insertress")
    # email = StringField("Email",validators=[DataRequired("Enter your emailaddress."),Email("Enter your email address11.")])
    # Age = IntegerField("age")
    # language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    # submit = SubmitField("Send")

class wtf_create_actor(FlaskForm):
    name = StringField("Ime i prezime: ", validators=[length(min=6, max=100)], render_kw={"placeholder": "npr. Robert De Niro"})
    actorImage = StringField("Slika (1:1): ", validators=[FileAllowed(['png','jpg','jpeg'])], render_kw={"placeholder": "npr. C:\\fakepath\\robert_de_niro.png", "readonly": "true"})
    actorFile = FileField("Izaberi", validators=[], render_kw={"accept": ".png, .jpg, .jpeg"})
    submit = SubmitField("Pošalji zahtev")
    # recaptcha = RecaptchaField()

class wtf_create_genre(FlaskForm):
    genre = StringField("Naziv: ", validators=[length(min=3, max=100)], render_kw={"placeholder": "npr. Action"})
    genreImage = StringField("Slika (1:1): ", validators=[FileAllowed(['png','jpg','jpeg'])], render_kw={"placeholder": "npr. C:\\fakepath\\action.png", "readonly": "true"})
    genreFile = FileField("Izaberi", validators=[], render_kw={"accept": ".png, .jpg, .jpeg"})
    submit = SubmitField("Pošalji zahtev")
    # recaptcha = RecaptchaField()


