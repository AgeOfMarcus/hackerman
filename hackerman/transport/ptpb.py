from hackerman import utils
import requests

def create_link():
	dat = utils.rand_bytes().decode()
	req = requests.post("https://ptpb.pw/",data={'c':dat})
	res = req.content.decode().strip()
	url = res.split("\n")[7].split(": ")[1]
	uid = res.split("\n")[-1].split(": ")[1]
	return url, uid

class Client(object):
	def __init__(self, url, uid):
		self.url = url
		self.uid = uid
	def send(self, raw):
		data = utils.b64e(raw)
		r = requests.post(url, data={'c':data})
	def recv(self):
		res = utils.b64d(requests.get(url).decode())
		r = requests.delete("https://ptpb.pw/"+uid)
		return res
