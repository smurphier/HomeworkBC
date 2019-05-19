from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo 
import mission

app = Flask(__name__)

# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"

## create / Use database
db = client.mars_db
## create/use collection. 
collection = db.mars_data_coll

# A route to query the mongoDB to fill the html template, "index.html":
@app.route("/")
def index():
    # Get the data from mongodb.
    mars_mission_data = mars_data_coll.find_one()
    # Return the template with data content
    return render_template("index.html", mars_mission_data = mars_mission_data)


# A route to trigger the scrape function:
@app.route("/scrape")
def scrape():
    # import the scrape function from the scrape file
    from mission import scrape_Mars
    mars_mission_data = scrape_Mars()

    # mars_data_coll.update({}, mars_data, upsert=True)
    mars_data_coll.update({"id": 1}, {"$set": mars_mission_data}, upsert = True)

    # return redirect("/", code=300)
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)