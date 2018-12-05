# 0.8.9
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
