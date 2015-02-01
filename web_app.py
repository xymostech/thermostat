from flask import Flask, render_template, jsonify, request, make_response
import gpio
import monitor
import db
import time


app = Flask(__name__)


def crossdomain(func):
    def wrapper(*args, **kwargs):
        resp = make_response(func(*args, **kwargs))

        resp.headers['Access-Control-Allow-Origin'] = '*'

        return resp

    return wrapper


@app.route('/')
def main():
    if app.config['DEBUG']:
        # Serve from beefy server
        bundle_url = 'http://localhost:9876/bundle.js'
    else:
        # Serve statically
        bundle_url = '/static/build/bundle.js'

    return render_template('index.html', bundle_url=bundle_url)


@app.route('/api/heater_on')
def heater_on():
    return jsonify(heat=monitor.heat_on())


@app.route('/api/current_temp')
def current_temp():
    return jsonify(temp=gpio.get_temp())


@app.route('/api/temp_data')
@crossdomain
def temp_data():
    now = int(time.time())
    start_time = request.args.get('start', now - 24 * 60 * 60)
    end_time = request.args.get('end', now)

    temp_data = []
    with db.get_db() as cursor:
        for row in cursor.execute("""
                SELECT * FROM temp_data WHERE
                time >= ? and time <= ?""",
                (start_time, end_time)):
            temp_data.append({
                "time": row["time"],
                "temp": row["temperature"]
            })

    return jsonify(data=temp_data)



app.teardown_appcontext(db.cleanup_db)
