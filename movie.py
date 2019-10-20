#FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import yaml 
import requests
from tmdbv3api import TMDb
from tmdbv3api import Movie

enviroment = os.getenv("API_KEY","NULL")
tmdb = TMDb()
tmdb.api_key = 'fe280a95fb920174dd75e3066c7cc1b8'
tmdb.language = 'en'
tmdb.debug= True

movie = Movie()
recommendations = movie.recommendations(movie_id=111)

for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)

#requests.get(f"https://api.themoviedb.org/3/movie/550?api_key={api_key}")

app = Flask(__name__)

environment=os.getenv("KEY","development")


@app.route("/")
def api_students():
    return render_template("index.html")

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)

