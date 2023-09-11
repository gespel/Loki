from loki import Loki
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Loki - the modern network hacking toolkit")
    parser.add_argument("--scanner", type=str, help="network to perform scan on")
    parser.add_argument("--tcpflood", type=str, help="ip to tcp flood")
    parser.add_argument("--udpflood", type=str, help="ip to udp flood")
    parser.add_argument("--console", action="store_true", help="start the loki console")
    args = parser.parse_args()

    loki = Loki()

    if args.scanner is not None:
        loki.get_scanner().get_all_local_ips(args.scanner)
    if args.tcpflood is not None:
        loki.get_flooder().tcp_syn_flood(args.tcpflood)
    if args.udpflood is not None:
        loki.get_flooder().udp_flood(args.udpflood, 80, "asd")
    if args.console:
        loki.start_console()
