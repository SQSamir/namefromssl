#!/usr/bin/python3

"""
__author__ = "SQS"

extract domain names  from ssl certificate
"""

import socket
import ssl
import sys

try:
    domainname = sys.argv[1]
    port = int(sys.argv[2])
except:
    print( "Usage : "+sys.argv[0]+" example.com 443 or SSL port")
    sys.exit()
cont = ssl.create_default_context()
conn = cont.wrap_socket(socket.socket(socket.AF_INET), server_hostname=domainname)
try:
    conn.connect((domainname, port))
except  (ssl.CertificateError,ssl.SSLError,socket.gaierror) as e:
    print("Error :", e)
    sys.exit()

cert = conn.getpeercert()
subdomains = (cert['subjectAltName'])

for i, domain in subdomains:
    print(domain)
