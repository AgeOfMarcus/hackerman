import os, base64, hashlib, sqlite3, socket, uuid
import random, qrcode, dis, ctypes, sys, code
import ast
from subprocess import Popen, PIPE
from hackerman.ui import betterexec
from hackerman.hashing import sha256
from typing import Union

blank_px = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGP6zwAAAgcBApocMXEAAAAASUVORK5CYII="

def inline_with(ctx, fn):
    """
    Run a function with the given context.

    :param ctx: The context to run the function with.
    :param fn: The function to run.
    :return: The return value of the function.

    Example:
    >>> inline_with(tryExceptHandler(), lambda: 1/0)
    """
    with ctx:
        return fn()

class tryExceptHandler(object):
    """
    Provides a context manager that will catch any exceptions.
    Usage:
        with tryExceptHandler():
            print('This code will run')
            print(This 'code will' not run but will not crash either)
            print('This code will not run since it is after the bad code')
    """
    def __enter__(self): pass
    def __exit__(self, *args): return True
tryExcept = tryExceptHandler()

def bin2int(x: Union[str, int]):
    '''
    Convert binary to integer.

    :param x: The binary to convert. Can be a string or an integer.
    :return: The integer representation of the binary.
    '''
    if type(x) == int:
        b = "0b"+str(x)
    else:
        if not x.startswith("0b"):
            b = "0b"+x
        else:
            b = x
    return ast.literal_eval(b)

def pythonShell(local=None, banner="entering InteractiveConsole (Ctrl+D to exit)..."):
    local = local or globals()
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


def sqlexec(cmd: str, db_file: str, values: tuple=()):
    with sqlite3.connect(db_file) as db:
        try:
            res = db.cursor().execute(cmd).fetchall() if values == () else db.cursor().execute(cmd,values).fetchall()
        except Exception as e:
            res = str(e)
        db.commit()
    return res

def rand_bytes(num: int=16) -> bytes:
    res = b''
    while len(res) < num:
        res += chr(random.randint(0,0x110000)).encode()
    return res

def getfilesize(fn: str) -> int:
    """
    Depends on the program `du` being installed.
    """
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
    """
    Gets an object from its id in memory.

    :param id: The id of the object.
    :return: status code (int, 0 for success), the object from memory or error
    """
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
