import socket
import sys


def get_constants(prefix):
    return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')


def get_address_info(port):
	host = 'localhost'
	for response in socket.getaddrinfo(host, port):
		fam, typ, pro, nam, add = response
		print('socket address: {}'.format(add))
		print('family: {}'.format(families[fam]))
		print('type: {}'.format(types[typ]))
		print('protocol: {}'.format(protocols[pro]))
		print('canonical name: {}'.format(nam))

def get_port_info(lowerbound=1, upperbound=10):

	if 0 <= lowerbound and upperbound <= 65535 and lowerbound <= upperbound:
		for portnum in range(lowerbound, upperbound):
			print(get_address_info(portnum))
	else:
		raise ValueError('Invalid port range. Valid ports are 0-65535')
		
get_port_info(10, 20)