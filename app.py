import web_app
import monitor
import signal
import sys

def signal_handler(sig, stack):
    monitor.stop_monitoring()
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

monitor.start_monitoring()
web_app.app.run(port=18260, host='0.0.0.0')
