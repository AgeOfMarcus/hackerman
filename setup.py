import setuptools
import os

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(name='hackerman',
	version='0.10.3',
	description='A python library for penetration testing, security, development, and fun.',
	long_description=read("README.md"),
	url='https://github.com/AgeOfMarcus/hackerman',
	author='Marcus Weinberger',
	author_email='marcus@marcusweinberger.com',
	license='GPL',
	packages=setuptools.find_packages(),
	zip_safe=False,
	install_requires=[
		"pycryptodome",
		"flask",
		"flask-cors",
		"requests",
		"scapy",
		"pyscreenshot",
		"pynput"
	])
