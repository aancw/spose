#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, socket
import ssl
import urllib.request, urllib.error, urllib.parse, http.client
from urllib.parse import urlparse

class URLRequest(object):
    def get(self, url_request, proxy_address):

        try:
            # if proxy_address is not "":
            #     print("[*] Using Proxy Address : {}".format(proxy_address))
            # else:
            #     print("Squid Proxy address empty, try again!")

            parse = urlparse(proxy_address)
            proxy_scheme = parse.scheme
            proxy = str(parse.hostname) + ':' + str(parse.port)
            proxy_handler = urllib.request.ProxyHandler({ proxy_scheme: proxy})
            opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(opener)
            req = urllib.request.Request(url_request)
            data = urllib.request.urlopen(req, timeout=1)
            
            return data
        except urllib.error.HTTPError as e:
            return e.code
        except urllib.error.URLError as e:
            return e.reason
        except Exception as detail:
            pass

if __name__ == '__main__':
    URLRequest = URLRequest()
    URLRequest