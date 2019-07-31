import os, base64, hashlib, sqlite3, socket, uuid
import random, qrcode, dis, ctypes, sys, code
import ast
from subprocess import Popen, PIPE
from hackerman.ui import betterexec
from hackerman.hashing import sha256

blank_px = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGP6zwAAAgcBApocMXEAAAAASUVORK5CYII="

class tryExceptHandler(object):
	def __enter__(self): pass
	def __exit__(self, *args): return True
tryExcept = tryExceptHandler()

def bin2int(x):
	if type(x) == int:
		b = "0b"+str(x)
	else:
		if not x.startswith("0b"):
			b = "0b"+x
		else:
			b = x
	return ast.literal_eval(b)

def pythonShell(local=None, banner="entering InteractiveConsole (Ctrl+D to exit)..."):
	local = dict(globals(), **local) if local else globals()
	code.interact(banner, local=local)

uid = lambda: str(uuid.uuid4())
safe_uid = lambda: ''.join(str(uuid.uuid4()).split("-"))

sh = lambda cmd: Popen(cmd,stdout=PIPE,shell=True).communicate()[0]

b64e = lambda raw: base64.b64encode(raw).decode()
b64d = lambda b64: base64.b64decode(b64)

addr2ip = lambda addr: socket.gethostbyname(addr)
hostname = socket.gethostname

def force_decode(raw):
	try:
		return raw.decode()
	except:
		return str(raw)[2:][:-1]

def cd(newdir):
	try:
		os.chdir(newdir)
	except:
		return False


def interactive_sh(cmd, out_func):
	process = Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
	try:
		for ln in iter(process.stdout.readline, b''):
			out_func(ln)
	except KeyboardInterrupt:
		os.system("pkill -f \"%s\"" % cmd)
		out_func(ln)


def sqlexec(cmd,db_file):
	with sqlite3.connect(db_file) as db:
		try:
			res = db.cursor().execute(cmd).fetchall()
		except Exception as e:
			res = str(e)
		db.commit()
	return res

def rand_bytes(num=16):
	res = b''
	while len(res) < num:
		res += chr(random.randint(0,0x110000)).encode()
	return res

def getfilesize(fn):
	r = sh("du "+fn).decode().strip().split("\n")[-1]
	bt = r.split("\t")[0]
	return int(bt)

def qr(text):
	be = betterexec.BetterExec()
	q = be.exec("import qrcode; code=qrcode.QRCode(); code.add_data('%s'); code.print_ascii()" % str(text.encode())[2:-1])
	return False if (q[1] == 1) else q[0]

def disassemble(bytecode):
	dis.dis(bytecode)

def from_id(id):
	try:
		return 0, ctypes.cast(id, ctypes.py_object).value
	except Exception as e:
		return 1, e

def zerostr(string):
	if not isinstance(string, str):
		raise TypeError("Expected a string, got: "+str(type(string)).split("'")[1])
	location = id(string) + 20
	size = sys.getsizeof(string) - 20
	try:
		memset = ctypes.cdll.msvcrt.memset # windows only
	except:
		memset = ctypes.memset
	memset(location, 0, size)
