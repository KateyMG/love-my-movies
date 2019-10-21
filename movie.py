#FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import yaml 
import requests
import redis
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Discover

enviroment = os.getenv("API_KEY","NULL")
tmdb = TMDb()
tmdb.api_key = 'fe280a95fb920174dd75e3066c7cc1b8'
tmdb.language = 'en'
tmdb.debug= True

#Redis
r = redis.Redis()
r.ping
True

movie = Movie()
recommendations = movie.recommendations(movie_id=111)

for recommendation in recommendations:
    print(recommendation.title)
    print(recommendation.overview)

#DISCOVER MOVIES
discover = Discover()
movie = discover.discover_movies({
    'primary_release_date.gte': '2019-01-20',
    'primary_release_date.lte': '2019-01-25'
})

#MOVIE DETAILS 

search = movie.search("Joker")

for res in search:
    print(res.id)
    print(res.title)
    print(res.overview)
    print(res.poster_path)
    print(res.vote_average)

m = movie.details(343611)

print(m.title)
print(m.overview)
print(m.popularity)

#TRENDING MOVIES-POPULAR
popular = movie.popular()

for p in popular:
    print(p.id)
    print(p.title)
    print(p.overview)
    print(p.poster_path)


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

