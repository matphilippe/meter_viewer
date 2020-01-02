from flask import Flask
import app.libraries.raspi_capture as raspi

flask_app = Flask(__name__)

from app import routes

