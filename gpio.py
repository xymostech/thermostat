import random
try:
    from RPi import GPIO
    real_gpio = True
except ImportError:
    real_gpio = False


# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adc_num, spi_pins):
    if ((adc_num > 7) or (adcnum < 0)):
        return -1

    clock_pin, mosi_pin, miso_pin, ss_pin = spi_pins

    GPIO.output(ss_pin, True)

    GPIO.output(clock_pin, False)  # start clock low
    GPIO.output(ss_pin, False)     # bring SS low

    commandout = adc_num
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosi_pin, True)
        else:
            GPIO.output(mosi_pin, False)
        commandout <<= 1
        GPIO.output(clock_pin, True)
        GPIO.output(clock_pin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clock_pin, True)
        GPIO.output(clock_pin, False)
        adcout <<= 1
        if (GPIO.input(miso_pin)):
            adcout |= 0x1

    GPIO.output(ss_pin, True)

    adcout >>= 1       # first bit is 'null' so drop it
    return adcout

def spi_setup(spi_pins):
    clock_pin, mosi_pin, miso_pin, ss_pin = spi_pins

    GPIO.setup(clock_pin, GPIO.OUT)
    GPIO.setup(mosi_pin, GPIO.IN)
    GPIO.setup(miso_pin, GPIO.OUT)
    GPIO.setup(ss_pin, GPIO.OUT)


# GPIO pin corresponding to the relay
RELAY_OUTPUT = 17


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


# GPIO pins corresponding to clock, mosi, miso, and ss pins
SPI_PINS = (22, 23, 24, 25)

# ADC input for the temperature sensor
TEMP_SENSOR = 0


def get_temp():
    if real_gpio:
        return readadc(TEMP_SENSOR, SPI_PINS)
    else:
        return random.randint(18 * 2, 23 * 2) / 2.0


if real_gpio:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RELAY_OUTPUT, GPIO.OUT)

    spi_setup(SPI_PINS)
