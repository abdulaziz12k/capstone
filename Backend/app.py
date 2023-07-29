import os
from flask import Flask, request, abort, jsonify
from .config import setup_db
from .models import Movie, Actor
from datetime import datetime
from .auth import AuthError, requires_auth
from flask import render_template


def create_app(test_config=None):
    app = Flask(
        __name__, template_folder='../templates')
    setup_db(app)

    # main page for render web service
    @app.route('/')
    def index():
        return ' To The MOON ! change the URL on top, add this in the end  "/movies" for starters'

    # GET MOVIES

    @app.route('/movies', methods=['GET'])
    def get_movies():
        response = Movie.query.order_by(Movie.id).all()
        if not response:
            abort(404)
        else:
            return render_template('../templates/movies.html',
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
    def update_movie(movie_id):
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
    def delete_movie(movie_id):
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
            return jsonify({
                "Actors:": [i.format() for i in response]
            }), 200

    # POST ACTORS

    @app.route('/actor/create', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor():
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
    def update_actor(actor_id):
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
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).first()
        if actor is None:
            abort(404)
        else:
            actor.delete()
            return jsonify({
                "success": True,
                "deleted": actor_id
            }), 200

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
