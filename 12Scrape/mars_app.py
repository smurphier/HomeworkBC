from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_Mars

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"

# ## create / Use database
db = client.mars_db
## create/use collection. 
collection = db.mars_data_coll


@app.route("/")
def index():
    # Get the data from mongodb.
    mars_mission_mongo = mars_data_coll.find_all()
    # Return the template with data content
    return render_template("index.html", mars_data = mars_mission_mongo)


@app.route("/scrape")
def scrape():
    mars_data_coll = mongo.mars_db.\
    mars_data = mission.scrape_Mars()
    mars_data_coll.update({}, mars_data, upsert=True)
    return redirect("/")
    # , code=302)

if __name__ == "__main__":
    app.run(debug=True)