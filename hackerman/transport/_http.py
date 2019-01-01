from flask import Flask, request
from flask_cors import CORS
from hackerman import utils
import _thread, logging, requests

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

class Server(object):
	def __init__(self, port):
		self.tosend = []
		self.torecv = []

		app = Flask(__name__)
		CORS(app)

		@app.route("/send", methods=['POST'])