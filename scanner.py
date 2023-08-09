import socket
import ipaddress

from concurrent.futures import ThreadPoolExecutor


class Scanners:
    def __init__(self):
        pass

    def get_all_local_ips(self, network):
        network = "192.168.2.0/24"  # Ändern Sie dies entsprechend Ihrem Netzwerk
        ip_range = ipaddress.ip_network(network, strict=False)

        found_ips = []

        with ThreadPoolExecutor(max_workers=20) as executor:
            for ip in ip_range:
                executor.submit(self.scan_target, ip, found_ips)
        return found_ips

    def scan_target(self, ip, result_list):
        try:
            host_name = socket.gethostbyaddr(str(ip))[0]
            result_list.append(str(ip))
        except socket.herror:
            pass