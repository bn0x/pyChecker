import socks
import socket
import urllib2

def activateProxy(type, ip, port):
	eval('socks.setdefaultproxy(socks.PROXY_TYPE_%s, ip, int(port))' % type.upper())
	socket.socket = socks.socksocket

def checkProxy(type, ip, port):
	if 'socks5' in type:
		functData = eval('socks5(\'%s\', \'%s\', \'%s\')' % (type, ip, port))
		return functData
	elif 'http' in type:
		return eval('http(\'%s\', \'%s\', \'%s\')' % (type, ip, port))
	elif 'socks4' in type:
		return eval('socks4(\'%s\', \'%s\', \'%s\')' % (type, ip, port))
	else:
		return False

def socks5(type, ip, port):
	activateProxy(type, ip, port)
	try:
		testProxy = urllib2.urlopen('http://google.com/').read()
		return '%s is alive on: %d, using: %s' % (ip, int(port), type.upper()) 
	except:
		return '%s is dead on: %d, using: %s' % (ip, int(port), type.upper())


def http(type, ip, port):
	activateProxy(type, ip, port)
	try:
		testProxy = urllib2.urlopen('http://google.com/').read()
		return '%s is alive on: %d, using: %s' % (ip, int(port), type.upper()) 
	except:
		return '%s is dead on: %d, using: %s' % (ip, int(port), type.upper())

def socks4(type, ip, port):
	activateProxy(type, ip, port)
	try:
		testProxy = urllib2.urlopen('http://google.com/').read()
		return '%s is alive on: %d, using: %s' % (ip, int(port), type.upper()) 
	except:
		return '%s is dead on: %d, using: %s' % (ip, int(port), type.upper())
