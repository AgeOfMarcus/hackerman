# 0.10.1
	- Bugfixes in reverse_ptpb

# 0.10.0
	- Deleted hackerman.transport.covert.ptpb
	- Improved hackerman.transport.ptpb to be actual transport
	- Added hackerman.payloads.reverse.ptpb
	- And hackerman.handlers.reverse_ptpb to go with it

# 0.9.9
	- Renamed libs named "http.py" to "_http.py"

# 0.9.8
	- Added hackerman.transport.covert.ptpb

# 0.9.7
	- changed RuntimeErrors to BaseExceptions

# 0.9.6
	- Added hackerman.transport.smtp

# 0.9.5
	- Added hackerman.rat (Remote Access Tools)
		- gui
			- screenshot
				- box (function)
				- all (function)
			- keyboard
				- Keyboard (class)
					- win_r, enter, alt_f4
					- type
				- keylogger

# 0.9.4
	- Quick changes to hackerman.stagers.examples.tcp

# 0.9.3
	- Added hackerman.stagers
		- ptpb
			- upload (function)
		- http
			- serve_once (function)
			- serve (function)
		- tcp
			- serve_once (function)
			- serve (function)
		- examples (dir)
			- ptpb.py
			- http.py
			- tcp.py
	- Added features to hackerman.transport.tcp
		- RawServer (class) (regular tcp server)
		- RawClient (class) (regular tcp client)

# 0.9.2
	- Nevermind, back to UDP, TCP is difficult

# 0.9.1
	- Forgot to mention updated the docs in 0.9.0, still a while to go
	- Changed DNS requests from UDP to TCP for better transport

# 0.9.0	(i don't like doing the double digit final things)
	- Okay so that was a lie, hackerman.transport.ptpb will never work for reasons, so i deleted that
	- still working on hackerman.transport.covert.dot11
	- working a bit more on the reverse dns payload/handler

# 0.8.15
	- final bugfix for hackerman.transport.ptpb

# 0.8.14
	- Quick fix for hackerman.transport.ptpb

# 0.8.13
	- Okay hackerman.transport.covert.dot11 isnt done yet
	- Added hackerman.transport.ptpb

# 0.8.12
	- Finished hackerman.transport.covert.dot11
	- Added "reverse" payload with covert DNS transport (kinda mostly works)
		- hackerman.handlers.reverse_dns
			- Handler
		- hackerman.payloads.reverse.dns
			- Payload

# 0.8.11
	- Improved getfilesize in hackerman.utils to work with folders
	- hackerman.transport.covert.dot11 is still unfinished lol oof

# 0.8.10 (apparently it's not 0.9.0)
	- Added hackerman.transport.covert.dot11 (unfinished)
	- Added getfilesize to hackerman.utils

# 0.8.9
	- Fixed hackerman.transport.covert.dns.SpeedyClient not sending complete data

# 0.8.8
	- PyPi wouldn't let me upload 0.8.7 because i deleted it to re-upload so yeah

# 0.8.7
	- Actually finished hackerman.transport.covert.dns

# 0.8.6
	- Finished hackerman.transport.covert.dns
		- Client: slower but more covert
		- SpeedyClient: quicker (8x) but more detectable

# 0.8.5
	- Added hackerman.transport.dns
	- Added hackerman.transport.covert.dns

# 0.8.4
	- Changed from pyCrypto to pyCryptodome because
		- Speed
		- Compatability

# 0.8.3
	- Improvements and bugfixes in
		- hackerman.transport.dot11
			- Beacon
	- Added hackerman.scanners._http
	- Added hackerman.transport.arp
		- Ability to arpspoof with scapy

# 0.8.2
	- Added hackerman.transport.dot11
		- Beacon class

# 0.8.1
	- Fixed hackerman.transport.serveo

# 0.8.0
	- Moved onion stuff from hackerman.scanners.tcp to hackerman.crypto.onion
	- Finished hackerman.transport.covert.jsc

# 0.7.5
	- Created hackerman.transport.covert
		- hackerman.transport.covert.jsc

# 0.7.4
	- Added onion domain generator in hackerman.scanners.tcp

# 0.7.3
	- Improved hackerman.utils.interactive_sh with KeyboardInterrupt
	- Added hackerman.transport.serveo (tcp, http) serveo integration

# 0.7.2
	- Added utils:
		- rand_bytes

# 0.7.1
	- Changed sh method in reverse_tcp to return raw

# 0.7.0
	- Fixed reverse_tcp bg commands

# 0.6.9 (nice)
	- Fixed hackerman.crypto.hmc not using full password
	- Gave up on exec methon in reverse_tcp
	- Fixed exit in reverse_tcp

# 0.6.8
	- Fixed hackerman.crypto.hmc
	- Added hackerman.crypto.blowfish

# 0.6.7
	- If this doesn't do it then i'm leaving it till tomorrow

# 0.6.6
	- Ok last bugfix fo real in that

# 0.6.5
	- Hopefully last bugfix in tcp pl/hl
		- just en/de code everything in b64

# 0.6.4
	- Fixed bugs in reverse tcp payload and handler
		- sending/recieving files
		- sending cmds

# 0.6.3
	- HMC encryption now returnes bytes instead of str
	- Added reverse TCP payload
	- Added reverse TCP handler
	- Added uid and safe_uid function to hackerman.utils

# 0.6.2
	- Bug fixes in hackerman.transport.tcp
	- Added CHANGELOG.md to be used for update info
