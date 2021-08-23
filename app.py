# 9.4.3 Import the Flask dependency
# from flask import Flask

# Create a new Flask App Instance
# app = Flask(__name__)

# Create a Flask route
# @app.route('/')
# def hello_world():
    # return 'Hello world'


# 9.5.1 Import dependencies
import datetime as dt
from flask.signals import request_tearing_down
import numpy as np
import pandas as pd

# Import SQLAlchemy and its dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependencies
from flask import Flask, jsonify

# Setup database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the data
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variables to reference each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)

# Create a Flask application called app
app = Flask(__name__)

# 9.5.2 Define the welcome route
@app.route("/")

# Create a function that adds routing information for each of the other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# 9.5.3 Create the precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# 9.5.4 Create the stations route
@app.route("/api/v1.0/stations")

# Create the stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# 9.5.5 Create the monthly temperature route
@app.route("/api/v1.0/tobs")

# Create the monthly temperature function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create the statistics route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create the statistics function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
