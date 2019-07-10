import _thread, time, sys

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

class msg:
	alert = lambda msg: color.RED + color.BOLD + "[!] " + color.END + color.UNDERLINE + msg + color.END
	info = lambda msg: color.YELLOW + color.BOLD + "[*] " + color.END + color.UNDERLINE + msg + color.END
	plus = lambda msg: color.GREEN + color.BOLD + "[+] " + color.END + color.UNDERLINE + msg + color.END
	minus = lambda msg: color.DARKCYAN + color.BOLD + "[-] " + color.END + color.UNDERLINE + msg + color.END
	loot = lambda msg: color.GREEN + color.BOLD + "[$] " + color.END + color.UNDERLINE + msg + color.END
	info2 = lambda msg: color.YELLOW + color.BOLD + "[~] " + color.END + color.UNDERLINE + msg + color.END

class Notifier(object):
	def __init__(self, prompt):
		self.messages = []
		self.prompt = prompt
		self.check = True
	def _start(self, check, delay):
		time.sleep(delay)
		while check():
			try:
				for msg in self.messages:
					sys.stdout.flush()
					sys.stdout.write("\r%s\n%s" % (msg, self.prompt))
					self.messages.remove(msg)
			except Exception as e:
				self.messages.append(color.RED + color.BOLD + "[!] " + color.END + color.RED + color.UNDERLINE + "Error printing message. Err: " + color.END + str(e))
	def start(self, check=None, delay=0.2):
		check = check if not check is None else lambda: self.check
		_thread.start_new_thread(self._start, (check,delay))
	def stop(self, stop=None):
		if stop is None:
			self.check = False
		else:
			stop()
