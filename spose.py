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
        parser.add_argument("--allports", help="[Optional] Scan all 65535 TCP ports behind proxy",
                            action="store_true", dest='allports')
        results = parser.parse_args()

        target = results.target
        proxy = results.proxy

        # Determine the list of ports to scan
        if results.allports:
            ports = range(1, 65536)  # All TCP ports
            print(f"{Fore.YELLOW}Scanning all 65,535 TCP ports{Style.RESET_ALL}")
        elif results.ports:
            ports = [int(port.strip()) for port in results.ports.split(",")]
            print(f"{Fore.YELLOW}Scanning specified ports: {results.ports}{Style.RESET_ALL}")
        else:
            ports = [21, 22, 23, 25, 53, 69, 80, 109, 110, 123, 137, 138, 139, 143, 156, 389, 443,
                     546, 547, 995, 993, 2086, 2087, 2082, 2083, 3306, 8080, 8443, 10000]
            print(f"{Fore.YELLOW}Scanning default common ports{Style.RESET_ALL}")

        print(f"{Fore.CYAN}Using proxy address {proxy}{Style.RESET_ALL}")

        # Set up proxy
        proxy_handler = urllib.request.ProxyHandler({'http': proxy})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

        # Scan the ports
        for port in ports:
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
