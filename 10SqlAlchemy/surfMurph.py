# Surfs Up!: Design a Flask API based on the queries you developed.
# Use FLASK to create your routes.
 
import numpy as np
import datetime as dt
# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite", \
    connect_args={'check_same_thread':False})
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Flask Setup
app = Flask(__name__)

@app.route("/")
def home():
    return (f"Welcome to the homepage: available routes are:<br/>"
            f"`/api/precipitation`  (precipitation for most recent 12months observed)<br/>"
            f"`/api/stations`    (list of observation stations in Hawaii)<br/>"
            f"`/api/temperature`    (temperatures for most recent 12months observed)<br/>"
            f"`/api/<start>`     (recent temperature statistics, since a specific date)<br/>"
            f"and `/api/<start>/<end>`  (temperature statistics for a specific RANGE of dates)")


@app.route("/api/precipitation")
def precip():
    """Query/retrieve the data and precipitation scores:
    Convert query results to a Dictionary, date=key, prcp=value.
	Return the JSON representation of your dictionary.

    Retrieve start & end dates for last 12months of 2010-01-01 to 2017-08-23:
    Capture last date, convert dtype for timedelta fcn to derive start date:"""
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first() 
    last_day = str(last_day)
    last_day_s= (last_day[2:12]) 
    last_date = dt.datetime.strptime(end_date_s, '%Y-%m-%d').date()
    yr_ago = last_date - dt.timedelta(days=365) 

    precip_trip = session.query(Measurement.date, func.sum(Measurement.prcp).\
        filter(Measurement.date >= yr_ago).\
        filter(Measurement.date <= last_date).\
            order_by(Measurement.date).all()
  
    # start_day = '2016-09-14'
    # start_date = dt.datetime.strptime(start_day, '%Y-%m-%d').date()
    # end_day = '2016-09-29'
    # end_date = dt.datetime.strptime(end_day, '%Y-%m-%d').date()
    # print(type(start_date))   
    # print(start_date, end_date)
    # num_days = (end_date - start_date).days
    # print(num_days)

    # print(type(precip_trip))  ## list
    # precip_trip
    precip_dict = dict(precip_trip)
    # precip_dict
    precip = list(np.ravel(precip_dict, order='F'))
    precip.json()


@app.route("/api/stations")
def stations():
#   * Return a JSON list of stations from the dataset.
    stations = session.query(Station.name).count()
    return jsonify(stations)

@app.route("/api/temperature")
def temperatures():
#   * query dates and temps from a year from the last data point.
#   * Return a JSON list of tobs for previous year.
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first() 
    yr_ago = dt.date(2017,8,23) - dt.timedelta(days=366) 
    YrAgo = session.query(Measurement.date, Measurement.tempobs).\
                filter(Measurement.date > yr_ago).\
                order_by(Measurement.date).all()
    return jsonify(YrAgo)

#   * Return a JSON list of min, avg, max temp for a given start or start-end range.
@app.route("/api/<start>")
def strtemp():
    start = input(f("Select a START date for your trip to Hawaii: yyyy-mm-dd"))
    print(f"Start date will be {start}")
    start_date = start
    return calc_temps(start_date)

@app.route("/api/<start>/<end>")
def endtemp():
    end = input(f("Select an END date for your trip to Hawaii: yyyy-mm-dd"))
    print(f"End date will be {end}")
    end_date = end
    return calc_temps(start_date, end_date)

def calc_temps(start_date, end_date):
    # start_day = '2016-09-14'
    # start_date = dt.datetime.strptime(start_day, '%Y-%m-%d').date()
    # end_day = '2016-09-29'
    # end_date = dt.datetime.strptime(end_day, '%Y-%m-%d').date()
    # print(type(start_date))   
    # print(start_date, end_date)

    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), \
                         func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start_date).\
                    filter(Measurement.date <= end_date).all()
    templist = calc_temps(start_date, end_date)
    # start_date = dt.datetime.strptime(start_date, '%Y-%m-%d').date()
    # end_date = dt.datetime.strptime(end_date, '%Y-%m-%d').date()
    # num_days = (end_date - start_date).days
    # print(num_days)
    return(f"Your trip {start_date} to {end_date} can expect to see temperatures like this:")
        # over the {num_days} days:")
    return jsonify(templist)

def calc_temps(start_date):
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), \
                         func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start_date).all()
    templist = calc_temps(start_date)
    return(f"Your trip on {start_date} can expect to see these temperatures like this:")
    return jsonify(templist)


# * Use Flask `jsonify` to convert your API data to a valid JSON response object.
@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)

if __name__ == "__main__":
    app.run(debug=True)
