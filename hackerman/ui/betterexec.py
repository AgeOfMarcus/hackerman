import sys

class FakeIO(object):
	def __init__(self):
		self.mem = ""
	def write(self, a):
		self.mem += a
	def read(self):
		return self.mem
	def flush(self):
		self.mem = ""

class BetterExec(object):
	def __init__(self):
		self.fd = FakeIO()
	def exec(self, code):
		old = sys.stdout
		sys.stdout = self.fd
		exec(code)
		sys.stdout = old
		res = self.fd.read()
		self.fd.flush()
		return res