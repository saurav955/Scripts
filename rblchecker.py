#!/bin/python

import sys
from multiprocessing import Process, Pool

try:
    import dns.resolver
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5.00
    resolver.lifetime = 5.00
except:
    print('Error : Unable To Load dns Module.')
    print('For python3 : pip3 install dnspython3')
    print('For python2 : pip install dnspython3')
    sys.exit(0)

#ips = ['11.*.*.*', '12.*.*.*', '13.*.*.*']

with open('iplist') as i:
    ips = i.readlines()
ips = [x.strip() for x in ips] 

with open('rbllist') as r:
    rbls = r.readlines()
rbls = [x.strip() for x in rbls] 

def srv_checker(rbl): 
    for ip in ips:
        try:
            resolver.query(ip+'.'+rbl,'A')
            srv_printer(ip, rbl)
            print(ip+' is listed in '+rbl)
        except:
            print('Not Listed')

def srv_printer(ipRev, rbl):
    ipReal = '.'.join( ipRev.split('.')[::-1])
    print(ipReal+' is listed in '+rbl)

#rbls = ['0spam.fusionzero.com', '0spam-killlist.fusionzero.com', 'ipbl.zeustracker.abuse.ch']

pool = Pool(processes=3)
results = pool.map(srv_checker, rbls)
