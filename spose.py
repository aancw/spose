#!/usr/bin/env python3

import sys
import argparse
import urllib.request
from colorama import Fore, Style, init

# Initialize colorama for color support
init(autoreset=True)

class Spose:
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='Spose by Petruknisme',
            description='Squid Pivoting Open Port Scanner'
        )
        parser.add_argument("--proxy", help="Define proxy address URL (http://xxx:3128)",
                            action="store", dest='proxy', required=True)
        parser.add_argument("--target", help="Define target IP behind proxy",
                            action="store", dest='target', required=True)
        parser.add_argument("--ports", help="[Optional] Define target ports behind proxy (comma-separated)",
                            action="store", dest='ports')
        results = parser.parse_args()

        if results.target is None or results.proxy is None:
            parser.print_help()
            sys.exit()

        target = results.target
        proxy = results.proxy
        if results.ports is None:
            ports = [21, 22, 23, 25, 53, 69, 80, 109, 110, 123, 137, 138, 139, 143, 156, 389, 443,
                     546, 547, 995, 993, 2086, 2087, 2082, 2083, 3306, 8080, 8443, 10000]
        else:
            ports = [int(port.strip()) for port in results.ports.split(",")]

        print(f"{Fore.CYAN}Using proxy address {proxy}{Style.RESET_ALL}")

        proxy_handler = urllib.request.ProxyHandler({'http': proxy})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

        for port in sorted(ports):
            try:
                url = f"http://{target}:{port}"
                with urllib.request.urlopen(url) as response:
                    code = response.getcode()
                    if code in [200, 404, 401]:
                        print(f"{Fore.GREEN}{target}:{port} seems OPEN{Style.RESET_ALL}")
            except urllib.error.HTTPError as e:
                # Suppress output for HTTP errors
                if e.code in [503]:
                    continue
            except urllib.error.URLError:
                # Suppress output for URL errors
                continue
            except Exception:
                # Suppress output for all other exceptions
                continue

if __name__ == "__main__":
    Spose()
