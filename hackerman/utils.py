import os, base64, hashlib, sqlite3, socket
from subprocess import Popen, PIPE

sh = lambda cmd: Popen(cmd,stdout=PIPE,shell=True).communicate()[0]
sha256 = lambda raw: hashlib.sha256(raw).hexdigest()

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
		return True
	except FileNotFoundError:
		return False


def interactive_sh(cmd, out_func):
	process = Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
	for ln in iter(process.stdout.readline, b''):
		out_func(force_decode(ln))

def sqlexec(cmd,db_file):
	with sqlite3.connect(db_file) as db:
		try:
			res = db.cursor().execute(cmd).fetchall()
		except Exception as e:
			res = str(e)
		db.commit()
	return res
