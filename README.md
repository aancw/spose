# Spose
Squid Pivoting Open Port Scanner

Detecting open port behind squid proxy for CTF and pentest purpose using http proxy method. Only for Python 3 version.

## Install & Usage

```
↳ python spose.py                                                           
usage: spose.py [-h] [--proxy PROXY] [--target TARGET]

optional arguments:
  -h, --help       show this help message and exit
  --proxy PROXY    Define proxy address url(http://xxx:3128)
  --target TARGET  Define target IP behind proxy
```

## VulnHub VM

- sickOS 1.1
- pinkys-palace

## References

https://www.rapid7.com/db/modules/auxiliary/scanner/http/squid_pivot_scanning

## License

This program is under MIT License.