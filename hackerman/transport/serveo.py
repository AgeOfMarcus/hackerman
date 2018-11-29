import os

def tcp(lport,rport):
	os.system("ssh -R %s:localhost:%s serveo.net" % (
		str(lport),
		str(rport)
	))
def http(lport,subdomain=None):
	if subdomain is None:
		cmd = "ssh -R 80:localhost:%s serveo.net"
	else:
		cmd = "ssh -R {}.serveo.net:80:localhost:%s serveo.net".format(
			subdomain
		)
	os.system(cmd % str(lport))
