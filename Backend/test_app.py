import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from .config import *
from .models import *
from .app import *

# Unitest class


class TriviaTestCase(unittest.TestCase):

    def setUp(self):
        # Define test variables and initialize app
        # Using second db other than the main db for Unitests
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_unitest"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)

    def tearDown(self):
        # Executed after each test
        pass

    def test_200_get_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["Movies"])
        self.assertTrue(len(data["Movies"]) > 0)

    def test_404_get_movies_fail(self):
        # Delete all movies from the database
        Movie.query.delete()
        db.session.commit()

        # Send a GET request to the /movies route
        res = self.client().get("/movies")
        data = json.loads(res.data)

        # Check if the response status code is 404
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_200_create_movie(self):
        new_movie = {
            "title": "Test Movie",
            "release_date": "2023-07-18"
        }
        res = self.client().post("/movies/create", json=new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["created movie:"])

    def test_422_create_movie_fail(self):
        # Create an invalid new movie, null title name
        new_movie = {
            "release_date": "2023-07-19"
        }

        # Send a POST request to the /movies/create route with the invalid movie data
        res = self.client().post("/movies/create", json=new_movie)
        data = json.loads(res.data)

        # Check if the response status code is 422
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])

    def test_200_update_movie(self):
        movie_id = 3
        update_data = {
            "title": "batman23",
            "release_date": "2023-07-19"
        }
        res = self.client().patch(f"/movies/{movie_id}", json=update_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])
        self.assertTrue(data["updated movie:"])

    def test_404_update_movie_fail(self):
        # Set the movie_id to a non-existent movie
        movie_id = 100000
        update_data = {
            "title": "Updated Test Movie",
            "release_date": "2023-07-19"
        }

        # Send a PATCH request to the /movies/{movie_id} route with the update data
        res = self.client().patch(f"/movies/{movie_id}", json=update_data)
        data = json.loads(res.data)

        # Check if the response status code is 404
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_404_delete_movie_fail(self):
        # Set the movie_id to a non-existent movie
        movie_id = 99999

        # Send a DELETE request to the /movies/{movie_id} route
        res = self.client().delete(f"/movies/{movie_id}")
        data = json.loads(res.data)

        # Check if the response status code is 404
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_404_get_actors_fail(self):
        # Delete all actors from the database
        Actor.query.delete()
        db.session.commit()

        # Send a GET request to the /actors route
        res = self.client().get("/actors")
        data = json.loads(res.data)

        # Check if the response status code is 404
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_422_create_actor_fail(self):
        # Create an invalid new actor
        new_actor = {
            "age": 30,
            "gender": "male"
        }

        # Send a POST request to the /actor/create route with the invalid actor data
        res = self.client().post("/actor/create", json=new_actor)
        data = json.loads(res.data)

        # Check if the response status code is 422
        self.assertEqual(res.status_code, 422)
        self.assertFalse(data["success"])

    def test_404_update_actor_fail(self):
        # Set the actor_id to a non-existent actor
        actor_id = 99999
        update_data = {
            "name": "abdulaziz",
            "age": 31,
            "gender": "Male"
        }

        # Send a PATCH request to the /actor/{actor_id} route with the update data
        res = self.client().patch(f"/actor/{actor_id}", json=update_data)
        data = json.loads(res.data)

        # Check if the response status code is 404
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_404_delete_actor_fail(self):
        # Set the actor_id to a non-existent actor
        actor_id = 99999

        # Send a DELETE request to the /actor/{actor_id} route
        res = self.client().delete(f"/actor/{actor_id}")
        data = json.loads(res.data)

        # Check if the response status code is 404
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
