from hackerman.transport import ptpb

def upload(text):
	cli = ptpb.ptpb("https://ptpb.pw")
	url, uid = cli.upload(text)
	if url == "already exists":
		return uid # actually url
	else:
		return url