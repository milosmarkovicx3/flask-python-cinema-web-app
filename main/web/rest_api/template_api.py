from flask import render_template, Blueprint, request
from flask_login import login_required
from service.core.wtf_forms import wtf_create_movie, wtf_create_actor, wtf_create_genre
from service.impl.movie_impl import MovieImpl


template_api = Blueprint('template_api', __name__)
mi = MovieImpl()

@template_api.route('/EditDatabase', methods=['GET'])
@login_required
def dashboard():
    return render_template('EditDatabase.html', form_movie=wtf_create_movie(), form_actor=wtf_create_actor(), form_genre=wtf_create_genre())

# @template_api.route('/logo')
# def get_image():
#     image_path = os.path.join(project_path, 'static\\resources\\images', 'arhiva_logo.jpg')
#     return send_file(image_path, mimetype='image/jpg')

@template_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@template_api.route('/repertoire', methods=['GET'])
def repertoire_search():
    search_input = request.args.get('search_input')
    imdb_rating = request.args.get('imdb_rating')
    timeline = request.args.get('timeline')
    genre_name = request.args.get('genre_name')
    sort_method = request.args.get('sort_method')
    page = request.args.get('page')
    per_page = request.args.get('per_page')

    search_parameters = {
        'search_input': search_input,
        'imdb_rating': imdb_rating,
        'timeline': timeline,
        'genre_name': genre_name,
        'sort_method': sort_method
    }

    paginate_object = mi.repertoire_search(search_input=search_input,
                                           imdb_rating=imdb_rating,
                                           timeline=timeline,
                                           genre_name=genre_name,
                                           sort_method=sort_method,
                                           page=page,
                                           per_page=per_page)

    return render_template("repertoire.html",
                           pagination=paginate_object,
                           endpoint='template_api.repertoire_search',
                           form=search_parameters)