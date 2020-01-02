import RPi.GPIO as GPIO


class GPIOHandler:

    def __init__(self, gpio_list):
        self.gpio_list = gpio_list
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        for gpio in self.gpio_list:
            GPIO.setup(gpio, GPIO.OUT)

    def _set_vals(self, value):
        for gpio in self.gpio_list:
            GPIO.output(gpio, value)

    def setON(self):
        self._set_vals(True)

    def setOFF(self):
        self._set_vals(False)

    def __del__(self):
        if self.gpio_list:
            GPIO.cleanup()
