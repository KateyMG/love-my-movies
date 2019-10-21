#FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import requests
import redis
import json
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
#r = redis.Redis(host='redis', port=6379, db=0, charset="utf-8", decode_responses=True)
r=redis.Redis(host="localhost",port=6379, db=0)  
#r = redis.Redis(host='my_redis_service', port=6379, decode_responses=True)
#redis_server= redis.Redis(host="localhost", port=6379, db=0)



movie = Movie()
#DISCOVER MOVIES
discover = Discover()
discovermovie = discover.discover_movies({
    'primary_release_date.gte': '2019-09-20',
    'primary_release_date.lte': '2019-09-25'
 })

# for movied in discovermovie:
#          redis_server.hset(movied.title, "title" ,movied.title)
#          redis_server.hset(movied.title, "poster_path" ,movied.poster_path)
#          redis_server.hset(movied.title, "id" ,movied.id)
#          redis_server.hset(movied.title, "overview" ,movied.overview)
#          redis_server.hset(movied.title, "vote_count", movied.vote_count)

#se mezclan las trending con las discover
#print(redis_server.hget("Fractured","id").decode('utf-8'))

#MOVIE DETAILS 

#TRENDING MOVIES-POPULAR
movie = Movie()
popular = movie.popular()

for eachMovie in popular:
        r.hset(eachMovie.title, "title" ,eachMovie.title)
        r.hset(eachMovie.title, "poster_path" ,eachMovie.poster_path)
        r.hset(eachMovie.title, "id" ,eachMovie.id)
        r.hset(eachMovie.title, "overview" ,eachMovie.overview)
        r.hset(eachMovie.title, "vote_count", eachMovie.vote_count)

#Infomarcion en redis
#Inforedis= r
#print(Inforedis)


#Recomendations
# recommendations = movie.recommendations(movie_id=111)

# for recommendation in recommendations:
#     print(recommendation.title)
#     print(recommendation.overview)

#requests.get(f"https://api.themoviedb.org/3/movie/550?api_key={api_key}")

app = Flask(__name__)
environment=os.getenv("KEY","development")

@app.route("/")
def api_students():
    return render_template("index.html", discovermovie=discovermovie, r = r)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)

