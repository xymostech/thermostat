from flask import Flask, render_template, jsonify
import gpio
import monitor
import db


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/heater_on')
def heater_on():
    return jsonify(heat=monitor.heat_on())


@app.route('/api/current_temp')
def current_temp():
    return jsonify(temp=gpio.get_temp())


app.teardown_appcontext(db.cleanup_db)
