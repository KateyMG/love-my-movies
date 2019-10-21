#FLASK
from flask import Flask, jsonify, render_template, request
import os, optparse
import yaml 
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
r=redis.Redis(host="localhost",port=6379) 

r.set("dani",11)
r.get("dani")



movie = Movie()
#DISCOVER MOVIES
discover = Discover()
discovermovie = discover.discover_movies({
    'primary_release_date.gte': '2019-09-20',
    'primary_release_date.lte': '2019-09-25'
 })
print("---------")
print(discovermovie)

#MOVIE DETAILS 


#TRENDING MOVIES-POPULAR
movie = Movie()
popular = movie.popular()
for p in popular:
    print(p.id)
    print(p.title)
    print(p.overview)
    print(p.poster_path)

for eachMovie in popular:
        r.hset(eachMovie.title, "poster_path" ,eachMovie.poster_path)
        r.hset(eachMovie.title, "id" ,eachMovie.id)
        r.hset(eachMovie.title, "overview" ,eachMovie.overview)
        r.hset(eachMovie.title, "vote_count", eachMovie.vote_count)
        

#json
my_details = {
    'name': 'John Doe',
    'age': 29
}

with open('popular_movies.json', 'w') as json_file:
    json.dump(my_details, json_file)


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
    return render_template("index.html",popular=popular, discovermovie=discovermovie)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)

