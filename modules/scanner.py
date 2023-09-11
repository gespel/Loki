import socket
import ipaddress

from concurrent.futures import ThreadPoolExecutor


class Scanners:
    def __init__(self, logger):
        self.logger = logger
        self.logger.info("Scanner module inizialized!")

    def get_all_local_ips(self, network):
        NUM_THREADS = 20

        self.logger.info(f"Setup to scan {network} now")
        ip_range = ipaddress.ip_network(network, strict=False)

        found_ips = []
        self.logger.info(f"Starting {NUM_THREADS} threads and start scan...")
        with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            for ip in ip_range:
                executor.submit(self.scan_target, ip, found_ips)
        self.logger.debug(f"found {found_ips}")
        return found_ips

    def scan_target(self, ip, result_list):
        try:
            host_name = socket.gethostbyaddr(str(ip))[0]
            result_list.append(str(ip))
        except socket.herror:
            pass
