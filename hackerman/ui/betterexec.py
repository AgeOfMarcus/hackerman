import sys

class FakeIO(object):
	def __init__(self):
		self.mem = ""
	def write(self, a):
		self.mem += a
	def flush(self):
		pass

class BetterExec(object):
	def __init__(self):
		self.stdout = FakeIO()
		self.stderr = FakeIO()
	def exec(self, code):
		stdout = sys.stdout
		stderr = sys.stderr
		sys.stdout = self.stdout
		sys.stderr = self.stderr

		exec(code)

		sys.stdout = stdout
		sys.stderr = stderr
		res = self.stdout.mem, self.stderr.mem
		self.stdout.mem = ""
		self.stderr.mem = ""
		
		return res