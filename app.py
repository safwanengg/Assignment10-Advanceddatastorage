from flask import Flask, jsonify


app = Flask(__name__)

stations_dict = {'station1':'USC00519281','station2':'USC00516128','station3':'USC00514830','station4':'USC00519523','station5':'USC00519397','station6':'USC00513117','station7':'USC00517948'}

holidayprcp_dict = {'2017-03-01': 0.59,
  '2017-03-02': 0.44,
  '2017-02-28': 0,
  '2017-03-03': 0,
  '2017-03-06': 0,
  '2017-03-05': 0.1,
  '2017-02-22': 0.06,
  '2017-02-25': 0.0,
  '2017-02-21': 0,
  '2017-02-23': 0.0,
  '2017-02-24': 0.0,
  '2017-03-04': 0.0,
  '2017-03-08': 0,
  '2017-02-27': 0,
  '2017-03-07': 0,
  '2017-02-20': 0,
  '2017-02-26': 0}

tobs_dict = {'2017-03-01': 73.0,
  '2017-03-02': 73.0,
  '2017-02-28': 72.0,
  '2017-03-03': 73.0,
  '2017-03-06': 67.0,
  '2017-03-05': 70.0,
  '2017-02-22': 72.0,
  '2017-02-25': 61.0,
  '2017-02-21': 71.0,
  '2017-02-23': 73.0,
  '2017-02-24': 70.0,
  '2017-03-04': 77.0,
  '2017-03-08': 67.0,
  '2017-02-27': 69.0,
  '2017-03-07': 67.0,
  '2017-02-20': 71.0,
  '2017-02-26': 67.0}

start_dict = {'tmin': 58.0, 'tavg': 75.39594843462247, 'tmax': 87.0}

end_dict = {'tmin': 61.0, 'tavg': 70.28571428571429, 'tmax': 78.0}

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def jsonified():
    return jsonify(holidayprcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    return jsonify(stations_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(tobs_dict)

@app.route("/api/v1.0/start")
def start():
    return jsonify(start_dict)

@app.route("/api/v1.0/start/end")
def end():
    return jsonify(end_dict)

if __name__ == "__main__":
    app.run(debug=True)