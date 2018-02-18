import sys
import OpenSSL
import ssl, socket
import cffi
import datetime
import dateutil.parser as parser
cert=ssl.get_server_certificate((sys.argv[1], 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
var=x509.get_notAfter()
var1 = parser.parse(var).isoformat()
var2 =  datetime.datetime.now().isoformat()

from datetime import datetime
def __datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S+00:00')
var3 = __datetime(var1)

def ___datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')

var4 = ___datetime(var2)
delta = var3 - var4
var5 = int((delta.total_seconds())/86400)
print(var5)
