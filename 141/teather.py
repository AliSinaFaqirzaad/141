from flask import Flask, jsonify , request
import csv

allMovies=[]
with open("main.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

app = Flask(__name__)


likedMovies=[]
notLikedMovies=[]
didNotWatched=[]

@app.route("/Movies")
def get_movie():
    return jsonify({
        "data":allMovies[0],
        "status":"success"
    })

@app.route("/likedMovies",methods=['POST'])
def liked_movies():
  movie = allMovies[0]
  allMovies = allMovies[1:]
  likedMovies.append(movie)
  return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run(debug=True)