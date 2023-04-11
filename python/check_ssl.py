"""
获取域名证书到期的详细天数
"""

import json
import idna
import time
import datetime
from socket import socket
from OpenSSL import SSL

domain = "a.com"
port = 443
hostname = "www." + domain
hostname_idna = idna.encode(hostname)
sock = socket()
sock.connect((hostname, port))
# peername = sock.getpeername()
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.check_hostname = False
ctx.verify_mode = SSL.VERIFY_NONE
sock_ssl = SSL.Connection(ctx, sock)
sock_ssl.set_connect_state()
sock_ssl.set_tlsext_host_name(hostname_idna)
sock_ssl.do_handshake()
cert = sock_ssl.get_peer_certificate()
crypto_cert = cert.to_cryptography()
sock_ssl.close()
sock.close()
startTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
start = time.mktime(time.strptime(str(startTime), '%Y-%m-%d %H:%M:%S'))
end = time.mktime(time.strptime(str(crypto_cert.not_valid_after), '%Y-%m-%d %H:%M:%S'))
expireDays = int((end - start) / (24 * 60 * 60))
print(expireDays)