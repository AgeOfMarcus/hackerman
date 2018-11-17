import base64

def to_num(raw):
	res = []
	for i in string: res.append(i)
	return res
def from_num(nums):
	res = ''
	for i in nums: res += chr(i)
	return res

def n_encrypt(nums,pwnums):
	res = []
	this = 0
	for i in nums:
		if this == len(pwnums) -1:
			this = 0
		res.append(i+pwnums[this])
		this += 1
	return res
def n_decrypt(nums,pwnums):
	res = []
	this = 0
	for i in nums:
		if this == len(pwnums) -1:
			this = 0
		res.append(i-pwnums[this])
		this += 1
	return res

def encrypt(raw, password):
	safe = base64.b64encode(raw).decode()
	n_ec = n_encrypt(to_num(safe),to_num(password))
	enc = from_num(n_ec)
	return enc.encode()
def decrypt(enc, password):
	n_ec = to_num(enc)
	safe = n_decrypt(n_ec,to_num(password))
	dec = base64.b64decode(from_num(safe))
	return dec
