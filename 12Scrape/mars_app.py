from flask import Flask, render_template, redirect
import pymongo 
import mission
from mission import scrape_Mars
from pprint import pprint
app = Flask(__name__)


# Create connection variable -- 03/07
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)

# from flask_pymongo import PyMongo
# # # Use PyMongo to establish Mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)
# # # or...
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


## create / Use database
db = client.mars_db
## create/use collection. 
collection = db.mars_data_coll

# A route to query the mongoDB to fill the html template, "index.html":
@app.route("/")
def index():
    # Get the data from mongodb.
    mars_mission_data = collection.find_one()
    # Return the template with data content
    return render_template("index.html", mars_mission_data=mars_mission_data)


# A route to trigger the scrape function:
@app.route("/scrape")
def scrape():
    # import the scrape function from the scrape file
    # mars_mission_data = mission.scrape_Mars()
    mars_mission_data = scrape_Mars()
    # print("Completed scraping in app.py")
    pprint(mars_mission_data)

    # collection.update_one({}, mars_mission_data, upsert=True)
    collection.update_one({"id": 1},{"$set": mars_mission_data},upsert=True)

    return redirect("/", code=302)
    # return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)