from pynput.keyboard import Key, Controller, Listener

class Keyboard(object):
	def __init__(self):
		self.keyboard = Controller()
	def press(self, key):
		self.keyboard.press(key)
	def release(self, key):
		self.keyboard.release(key)

	def win_r(self):
		self.press(Key.cmd)
		self.press("r")
		self.release(Key.cmd)
		self.release("r")
	def enter(self):
		self.press(Key.enter)
		self.release(Key.enter)
	def alt_f4(self):
		self.press(Key.alt)
		self.press(Key.f4)
		self.release(Key.alt)
		self.release(Key.f4)

	def type(self, string):
		self.keyboard.type(string)

def keylogger(on_press, on_release):
	with Listener(
		on_press=on_press,
		on_release=on_release) as listener:
		listener.join()
