from app.libraries.raspi_capture.gpio import GPIOHandler
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import os


class CaptCamera:

    def __init__(self, gpio_list):
        self.gpio_handler = GPIOHandler(gpio_list)

    def capture_to_array(self, warmup=1):
        with PiCamera() as camera:
            self.gpio_handler.setON()
            camera.start_preview()
            raw_capture = PiRGBArray(camera)
            camera.capture(raw_capture)
            camera.stop_preview()
            self.gpio_handler.setOFF()
            time.sleep(warmup / 2)

        image = raw_capture.array
        return image

    def capture_to_file(self, file, warmup=1):
        my_file = open('file', 'wb')
        with PiCamera() as camera:
            self.gpio_handler.setON()
            camera.start_preview()
            time.sleep(warmup)
            camera.capture(my_file)
            camera.stop_preview()
            self.gpio_handler.setOFF()
            time.sleep(warmup / 2)
        my_file.close()

        return None
