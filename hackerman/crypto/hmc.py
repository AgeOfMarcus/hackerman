import base64

def to_num(raw):
	res = []
	for i in raw: res.append(i)
	return res
def from_num(nums):
	res = b''
	for i in nums: res += (i).to_bytes(1,"little")
	return res

def n_encrypt(nums,pwnums):
	res = []
	this = 0
	for i in nums:
		if this == len(pwnums):
			this = 0
		res.append(i+pwnums[this])
		this += 1
	return res
def n_decrypt(nums,pwnums):
	res = []
	this = 0
	for i in nums:
		if this == len(pwnums):
			this = 0
		res.append(i-pwnums[this])
		this += 1
	return res

def encrypt(raw, password):
	n_ec = n_encrypt(to_num(raw),to_num(password.encode()))
	enc = from_num(n_ec)
	return enc
def decrypt(raw, password):
	n_ec = to_num(raw)
	dec = from_num(n_decrypt(n_ec,to_num(password.encode())))
	return dec
