#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, socket
import ssl
import argparse
from url_request import URLRequest 

class Spose(object):
    def __init__(self):
        req = URLRequest()
        parser = argparse.ArgumentParser(
            prog='Spose by Petruknisme',
            description='Squid Pivoting Open Port Scanner'
        )
        parser.add_argument("--proxy", help="Define proxy address url(http://xxx:3128)",
                    action="store", dest='proxy')
        parser.add_argument("--target", help="Define target IP behind proxy",
                    action="store", dest='target')
        results = parser.parse_args()

        if results.target is None or results.proxy is None:
            parser.print_help()
            sys.exit()

        target = results.target
        proxy = results.proxy
        common_ports = {21,22,23,25,53,69,80,109,110,123,137,138,139,143,156,389,443,546,547,995,993,2086,2087,2082,2083,3306,8080,8443,10000}

        print("Using proxy address {}".format(proxy))

        for n in sorted(common_ports):
            try:        
                data = req.get("http://{}:{}".format(target, str(n)), "{}".format(proxy))
                code = data.getcode()
                if code == 200 or code == 404 or code == 401:
                    print("{} {} seems OPEN ".format(target, str(n)))
            except:
                pass

if __name__ == '__main__':
    Spose = Spose()
