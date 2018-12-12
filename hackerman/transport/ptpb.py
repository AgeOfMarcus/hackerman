import requests

class ptpb(object):
	def __init__(self, url):
		self.url = url
	def upload(self, text, uri="/"):
		r = requests.post(self.url+uri, data={'c':text})
		ln = r.content.decode().strip().split("\n")
		url, uid = ln[-2].split(": ")[1], ln[-1].split(": ")[1]
		return url, uid
	def delete(self, uuid):
		r = requests.delete(self.url+"/"+uuid)
		return r.status_code
