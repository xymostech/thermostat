from flask import Flask, render_template
app = Flask(__name__)

import gpio
import monitor


@app.route('/')
def main():
    context = {
        "heat": monitor.heat_on()
    }

    return render_template('index.html', **context)


if __name__ == "__main__":
    app.run(debug=True, port=18260)
