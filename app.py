from flask import Flask, request, abort, jsonify, render_template, redirect, url_for, flash, Blueprint
from db_config import setup_db
from models import Movie, Actor
from datetime import datetime
from auth import AuthError, requires_auth, check_permissions
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_login import login_user, login_required, current_user
from auth import login_manager, client_id, domain
import auth0
from auth.views import auth_bp
# inheritence of Flask-WTF validating the form data,
# generating CSRF tokens, and rendering form fields.


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


def create_app(test_config=None):
    app = Flask(
        __name__, template_folder='templates')
    setup_db(app)
    app.secret_key = 'bafddb088a222c78b54f96f9eab7aaff'

    app.register_blueprint(auth_bp, url_prefix='/')

    # Login Page

    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template("login.html")

        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

            # Use the Auth0 login endpoint to authenticate the user using username and password
            user = auth0.login_with_credentials(username, password)

            # Redirect the user to the home page if the login is successful
            if user is not None:
                return redirect(url_for('homepage.html'))

            # Otherwise, display an error message
            else:
                flash('Invalid username or password')
                return render_template('login.html')
        return render_template('login.html')
    # HomePage

    @app.route('/homepage')
    @login_required
    def main():
        if current_user is None:
            return redirect(url_for('login.html'))
        return render_template('homepage.html')

    # GET MOVIES

    @app.route('/movies', methods=['GET'])
    def get_movies():
        response = Movie.query.order_by(Movie.id).all()
        if not response:
            abort(404)
        else:
            return render_template('movies.html',
                                   movies=response)
            # return jsonify({
            #     "Movies": [i.format()for i in response]
            # })

    # CREATE MOVIE

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(payload):
        response = request.get_json()
        if response is None:
            abort(404)
        else:
            # Check if the "title" key is present in the response
            if "title" not in response:
                abort(422)
            new_movie = Movie(
                title=response.get("title"),
                release_date=response.get("release_date")
            )
            new_movie.insert()
            return jsonify({
                "success": True,
                "created movie:": new_movie.format()
            }), 200

    # UPDATE MOVIE

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(payload, movie_id):
        response = request.get_json()
        if response is None:
            abort(404)
        else:
            movie = Movie.query.filter(Movie.id == movie_id).first()
            if movie is None:
                abort(404)
            else:
                movie.title = response.get('title')
                movie.release_date = datetime.strptime(
                    response.get('release_date'), '%Y-%m-%d').date()
                movie.update()
                return jsonify({
                    "success": True,
                    "updated movie:": [movie.format()]
                }), 200

    # DELETE MOVIE

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        response = Movie.query.filter(Movie.id == movie_id).first()
        if response is None:
            abort(404)
        else:
            deleted_movie = response.format()
            response.delete()
            return jsonify({
                "success": True,
                "deleted movie:": deleted_movie
            }), 200

    # GET ACTORS

    @app.route('/actors', methods=['GET'])
    def get_actors():
        response = Actor.query.order_by(Actor.id).all()
        if not response:
            abort(404)
        else:
            return render_template('actors.html',
                                   actors=response)
            # return jsonify({
            #     "Actors:": [i.format() for i in response]
            # }), 200

    # POST ACTORS

    @app.route('/actor/create', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(payload):
        response = request.get_json()
        if not response:
            abort(404)
        else:
            # Check if all required keys are present in the response
            if "name" not in response or "age" not in response or "gender" not in response:
                abort(422)
            new_actor = Actor(
                name=response.get('name'),
                age=response.get('age'),
                gender=response.get('gender')
            )
            print(f"New actor: {new_actor.format()}")
        new_actor.insert()
        return jsonify({
            "added actor:": new_actor.format()
        }), 200

    # UPDATE ACTOR DATA

    @app.route('/actor/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(payload, actor_id):
        response = request.get_json()
        if response is None:
            abort(404)
        else:
            actor = Actor.query.filter(Actor.id == actor_id).first()
            if actor is None:
                abort(404)
            else:
                actor.name = response.get('name')
                actor.age = response.get('age')
                actor.gender = response.get('gender')
                actor.update()
                return jsonify({
                    "success": True,
                    "actors": [actor.format()]
                }), 200

    # DELETE ACTOR

    @app.route('/actor/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        check_permissions('delete:actor', payload)
        actor = Actor.query.filter(Actor.id == actor_id).first()
        if actor is None:
            abort(404)
        else:
            actor.delete()
            return jsonify({
                "success": True,
                "deleted": actor_id
            }), 200

    @app.route('/googlemap')
    def googlemap():
        return render_template('googlemap.html')

    @app.route('/spotify')
    def spotify():
        return render_template('spotify.html')

    # _______ERROR HANDLING _________#

    @app.errorhandler(404)
    def resource_not_found(error):
        return (
            jsonify({"success": False, "error": 404,
                    "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422,
                    "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({"message": "An error occurred while processing your request"})

    @app.errorhandler(AuthError)
    def handle_auth_error(exception):
        return jsonify({
            "success": False,
            "error": exception.status_code,
            "message": exception.error
        }), exception.status_code
    return app


# Initialize app and run with debug mode
app = create_app()
if __name__ == '__main__':
    app.debug = True
    app.run()
