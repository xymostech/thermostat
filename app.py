from flask import Flask, redirect, url_for
app = Flask(__name__)

import gpio


@app.route('/')
def main():
    return 'Hello, thermostat!'


@app.route('/heaton')
def heat_on():
    gpio.heat_on()
    return redirect(url_for('main'))


@app.route('/heatoff')
def heat_off():
    gpio.heat_off()
    return redirect(url_for('main'))


if __name__ == "__main__":
    app.run(debug=True)
