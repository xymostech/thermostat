try:
    from RPi import GPIO
    real_gpio = True
except ImportError:
    real_gpio = False


RELAY_OUTPUT = 11


if real_gpio:
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(RELAY_OUTPUT, GPIO.OUT)


def heat_on():
    if real_gpio:
        GPIO.output(RELAY_OUTPUT, GPIO.HIGH)
    else:
        print "(fake) Turning heat on"

def heat_off():
    if real_gpio:
        GPIO.output(RELAY_OUTPUT, GPIO.LOW)
    else:
        print "(fake) Turning heat off"
