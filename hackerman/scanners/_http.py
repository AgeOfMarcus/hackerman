from hackerman.scanners  import tcp
import socket, requests

def knock(url, timeout=1):
    try:
        req = requests.get(url, timeout=timeout)
        return req.status_code
    except:
        return False

def rand_url():
    ip = tcp.rand_ipv4()
    url = "http://"+ip
    return url

def site2ip(site):
    ip = socket.gethostbyname(site)
    if type(ip) == list:
        return ip[0]
    else:
        return ip
def ip2site(ip):
    addr = socket.gethostbyaddr(ip)
    if type(addr) == list:
        return addr[0]
    else:
        return addr
