import smtplib

def gmail(username, password):
	srv = SMTP("smtp.gmail.com", 587)
	srv.login(username, password)
	return srv

class SMTP(object):
	def __init__(self, addr, port, tls=True):
		try:
			self.server = smtplib.SMTP(addr, port)
			self.server.ehlo()
			if tls:
				self.server.starttls()
		except:
			raise BaseException("Connection error")

	def login(self, username, password):
		try:
			self.server.login(username, password)
		except:
			raise BaseException("Login failed")

	def send(self, sent_from, to, subject, body):
		msg = "\r\n".join([
				"To: %s" % ', '.join(to),
				"From: %s" % sent_from,
				"Subject: %s" % subject,
				'',body
			])
		try:
			self.server.sendmail(sent_from, to, msg)
		except:
			raise BaseException("Error sending email")

	def close(self):
		self.server.close()
