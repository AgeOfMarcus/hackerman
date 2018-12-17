from flask import Flask, request
from flask_cors import CORS

def shutdown_server():
	func = request.environ.get("werkzeug.server.shutdown")
	if func is None:
		raise RuntimeError("Not running with the Werkzeug Server")
	func()

def serve_once(text, port):
	app = Flask(__name__)
	CORS(app)
	@app.route("/")
	def app_main():
		shutdown_server()
		return text
	app.run(host="0.0.0.0",port=port)

def serve(text, port):
	while True:
		try:
			serve_once(text, port)
		except KeyboardInterrupt:
			break