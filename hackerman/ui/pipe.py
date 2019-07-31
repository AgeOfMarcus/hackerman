import sys

def reader():
	if not sys.stdin.isatty():
		return lambda: sys.stdin.buffer.read()
	else:
		return lambda: input().encode()

write = lambda raw: sys.stdout.buffer.write(raw)
