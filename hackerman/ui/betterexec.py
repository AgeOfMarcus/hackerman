import sys

class FakeIO(object):
	def __init__(self):
		self.mem = []
	def write(self, *args):
		if type(args) == list or type(args) == tuple:
			[self.mem.append(i) for i in args]
		else:
			self.mem.append(args)
	def flush(self):
		pass
	def read(self):
		return ''.join(self.mem)
	def clear(self):
		self.mem = []

class BetterExec(object):
	def __init__(self):
		self.stdout = FakeIO()
	def exec(self, code):
		stdout = sys.stdout
		sys.stdout = self.stdout

		try:
			exec(code)
			res = self.stdout.read(), 0
		except Exception as e:
			res = e, 1

		sys.stdout = stdout
		self.stdout.clear()
		
		return res