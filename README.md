# hackerman
The hackerman library is one I made for two reasons.

	1. Because I want to make, package, and publish my own library
	2. So I can use it in my penetration testing programs

So yeah

# Docs

Key:
	$name - needed argument
	£name - optional argument
	name - function name()
	Name - class Name
	%type - returns type

## hackerman
	There's nothing here lol
## hackerman.crypto
### blowfish (Crypto.Cipher.Blowfish)
	encrypt
	$raw = raw bytes to encrypt
	$password = plain text password
	%bytes = encrypted bytes

	decrypt
	$raw = raw encrypted bytes to decrypt
	$password = plain text password
	%bytes = decrypted bytes
### hmc (my own cipher method)
	encrypt
	$raw = raw bytes to encrypt
	$password = plain text password
	%bytes = encrypted bytes

	decrypt
	$raw = raw encrypted bytes to decrypt
	$password = plain text password
	%bytes = decrypted bytes
### xor (Crypto.Cipher.XOR)
	encrypt
	$raw = raw bytes to encrypt
	$password = plain text password
	%bytes = encrypted bytes

	decrypt
	$raw = raw encrypted bytes to decrypt
	$password = plain text password
	%bytes = decrypted bytes
### rsa (Crypto.PublicKey.RSA)
	Key = RSA key class
	£imp = default=False, if specified, needs to be an RSA key object
		encrypt = encrypt function
		$raw = raw bytes to encrypt with key
		%bytes = encrypted bytes

		decrypt = decrypt function
		$raw = raw encrypted bytes to decrypt with key
		%bytes = decrypted bytes

		export
		$fn = filename to save key to

	importKey
	$fn = filename to read key data from
### onion (onion domains)
	generate = generate onion domain and key
	%onion, %priv = onion domain, private key for said domain

## handlers
### reverse_dns (handler for payloads.reverse.dns)
	NoCrypt = class needed if you don't want encryption
	XORCrypt = class wrapper for xor en/de cryption
	Handler = payload handler
		$crypt = method of encryption (NoCrypt, XORCrypt, or your own as long as it has the encrypt and decrypt methods)
		£send = default="send.com" domain for sending data (read transport.covert.dns.SpeedyClient)
		£listen = default="listen.com" (see above)



# License
It is licensed under the GNU GPL (more info in the "LICENSE" file). It is my first time adding a license so I don't really know if I did it right.
Basically, don't distribute closed-source versions, but feel free to do whatever else you want with it, it would be cool if you credited me, though.

