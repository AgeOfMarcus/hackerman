import bitcoin

def generate_private_key():
	return bitcoin.random_key()
def private_key_to_public_key(priv):
	return bitcoin.privtopub(priv)
def public_key_to_address(pub):
	return bitcoin.pubtoaddr(pub)

