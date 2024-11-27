# Spose
Squid Pivoting Open Port Scanner

Detecting open port behind squid proxy for CTF and pentest purpose using http proxy method. Only for Python 3 version.

## Install & Usage

```
❯ python3 ./spose.py --help
usage: Spose by Petruknisme [-h] --proxy PROXY --target TARGET [--ports PORTS]

Squid Pivoting Open Port Scanner

options:
  -h, --help       show this help message and exit
  --proxy PROXY    Define proxy address URL (http://xxx:3128)
  --target TARGET  Define target IP behind proxy
  --ports PORTS    [Optional] Define target ports behind proxy (comma-separated)
```

## VulnHub VM

- sickOS 1.1
- pinkys-palace

## References

https://www.rapid7.com/db/modules/auxiliary/scanner/http/squid_pivot_scanning

## License

This program is under MIT License.