from app import flask_app
from flask import render_template, send_from_directory, request, abort
import app.libraries.raspi_capture.capture as raspi
import app.constants as constants


@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'dummy'}
    return render_template('index.html', title='Home', user=user)


@flask_app.route('/capture', methods=['GET'])
def send_capture():
    # 7 and 11 are the GPIO ports for leds.
    # We should give them as req args.
    rot = request.args.get('rot', default=0)
    raspi_handler = raspi.CaptCamera(gpio_list=[7, 11])
    raspi_handler.capture_to_file('app/temp/images/' + constants.CAPTURE_IMG, rot=rot)
    return send_from_directory('./temp/images', constants.CAPTURE_IMG)


@flask_app.route('/capture/dummy', methods=['GET'])
def send_dummy_photo():
    return send_from_directory('./static/images', constants.DUMMY_IMG)


@flask_app.route('/teapot', methods=['GET'])
def imateapot():
    abort(418)


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0')
