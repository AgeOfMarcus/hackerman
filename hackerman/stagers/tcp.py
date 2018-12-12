from hackerman.transport import tcp

def serve_once(raw, port):
	srv = tcp.RawServer(port)
	srv.send(raw)
	srv.conn.close()

def serve(raw, port):
	while True:
		try:
			serve_once(raw, port)
		except KeyboardInterrupt:
			break