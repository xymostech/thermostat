import web_app
import monitor
import signal
import sys
import argparse

parser = argparse.ArgumentParser(description='Run the web server')
parser.add_argument('--debug', dest='debug', action='store_true')

args = parser.parse_args()

def signal_handler(sig, stack):
    monitor.stop_monitoring()
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

monitor.start_monitoring()
web_app.app.run(port=18260, host='0.0.0.0', debug=args.debug)
