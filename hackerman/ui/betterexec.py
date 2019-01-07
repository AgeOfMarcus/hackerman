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
	def exec(self, code):
		stdout = sys.stdout
		sys.stdout = self.stdout

		try:
			exec(code)
			res = self.stdout.mem, 0
		except Exception as e:
			res = e, 1

		sys.stdout = stdout
		self.stdout.mem = ""
		
		return res