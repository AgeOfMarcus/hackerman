from __future__ import print_function
import sys, readline
from os import environ

class Autocomplete(object):
	def __init__(self, options):
		self.options = sorted(options)
	def complete(self, text, state):
		if state == 0:
			if not text:
				self.matches = self.options[:]
			else:
				self.matches = [s for s in self.options if s and s.startswith(text)]
		try:
			return self.matches[state]
		except IndexError:
			return None
	def display_matches(self, subsitution, matches, longest_match_length):
		line_buffer = readline.get_line_buffer()
		columns = environ.get("COLUMNS", 80)
		print()
		tpl = "{:<" + str(int(max(map(len, matches)) * 1.2)) + "}"
		buffer = ""
		for match in matches:
			match = tpl.format(match[len(subsitution):])
			if len(buffer + match) > columns:
				print(buffer)
				buffer = ""
			buffer += match
		if buffer:
			print(buffer)
		print("> ",end="")
		sys.stdout.flush()

class ExampleHandler(object):
	def __init__(self):
		self.commands = ['help','exit']
	def handle(self,cmd):
		if cmd == 'help':
			print("HELP_MENU_GOES_HERE")
			return None
		elif cmd == "exit":
			return "exit"

def start_shell(cmd_handler):
	commands = cmd_handler.commands
	completer = Autocomplete(list(set(commands)))
	readline.set_completer_delims('\t')
	readline.set_completer(completer.complete)
	readline.parse_and_bind('tab: complete')
	readline.set_completion_display_matches_hook(completer.display_matches)
	while True:
		cmd = input("> ")
		try:
			res = cmd_handler.handle(cmd)
		except Exception as e:
			print("Error: "+str(e))
			res = None
		if res == "exit":
			break
