from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission

# create instance of Flask app
app = Flask(__name__)
# Create connection variable, Pass connection to the pymongo instance.
# # Use flask_pymongo to set up mongo connection
mongo_conn = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route that renders index.html template using content from Mongo
@app.route("/")
def home():
    # Find & Store the entire collection of data from the mongo database
    mars_collect = mongo.db.collection.find()
    # Return the template index.html with the retrieved collection of data passed in
    return render_template("index.html", mars_data = mars_collect)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = mission.scrape_Mars()

    # # Connect to a database, then a collection; create one if not already available.
    # mars_db = mongo_conn.mars_db
    # mars_coll = mongo_conn.mars_db.mars_coll
    # mars_db.mars_coll.insert_one({key1:val1})
    
    # Add one entry to the Mongo database using update and upsert=True
    # update allows new fields, keys/values to be added for that record.
    # mongo_conn.mars_db.mars_coll.update_one({}, mars_data, upsert: true)

    # Redirect back to home page
    return redirect("/")     # , code=302)

if __name__ == "__main__":
    app.run(debug=True)