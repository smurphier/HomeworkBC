# Surfs Up!: Design a Flask API based on the queries you developed.
# Use FLASK to create your routes.
 
import numpy as np
import sqlalchemy
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
            f"`/api/precipitation`<br/>"
            f"`/api/stations`<br/>"
            f"`/api/temperature`<br/>"
            f"and `/api/<start>` & `/api/<start>/<end>`")

@app.route("/api/precipitation")
def precip():
    # Convert query results to Dictionary, `date` as key, `prcp` as value.
    last_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first() 
    yr_ago = dt.date(2017,8,23) - dt.timedelta(days=366) 
    # Perform a query to retrieve the data and precipitation scores
    YrAgo = session.query(Measurement.station, Measurement.date,                       Measurement.prcp).                filter(Measurement.date > yr_ago).                order_by(Measurement.date).all()
    yrago_df = pd.DataFrame(YrAgo, columns=['station', 'date', 'precip'])
    yrago_df.set_index('date', inplace=True)
    yrago_df.head()
    # Sort the dataframe by date --- AND GET RID OF NULL (NaN) VALUES ---
    yrago_df.sort_values('date', na_position='first')
    yrago_df['precip'].isnull().sum().sum()    ## 208 NaNv alues; ALL in precip column
    yrago_df.dropna(inplace=True)
    
    # precip_date = session.query(Measurement.date, Measurement.prcp).\
    #         filter(Measurement.date == start_date).\
    #         filter(Measurement.date <= end_date).\
    #         order_by(func.sum(Measurement.prcp).desc()).all()
    precip_dict = list(np.ravel(precip_date))
    print(precip_dict)
    return precip_dict

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

# * "/api/<start>" and "/api/<start>/<end>"
@app.route("/api/<start>")
def sttemp():
    print(f"Start date will be {start}")
    start_date = start
    return start_date

@app.route("/api/<start>/<end>")
def endtemp():
    print(f"END date will be {end}")
    end_date = end
    return end_date

def calc_temps(start_date, end_date):
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), \
                         func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start_date).\
                    filter(Measurement.date <= end_date).all()
    templist = calc_temps(start_date, end_date)
    return jsonify(templist)


#   * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
#   * Hint: You may want to look into how to create a defualt value for your route variable.
#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
# ## Hints
# * Must join station + measurement tables for some of the analysis queries.
# * Use Flask `jsonify` to convert your API data to a valid JSON response object.
# @app.route("/jsonified")
# def jsonified():
#     return jsonify(hello_dict)

if __name__ == "__main__":
    app.run(debug=True)
