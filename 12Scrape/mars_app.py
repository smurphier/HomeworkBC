from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_Mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    return render_template("index.html", mars_data = Mars)


@app.route("/scrape")
def scrape():
    mars_data = mission.scrape_Mars()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)