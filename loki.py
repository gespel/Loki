import logging
import time
import termcolor

import pyfiglet

from modules.deception import Deceiver
from modules.flooder import Flooder
from modules.scanner import Scanners


def configure_logger(log_file='loki.log', log_level=logging.DEBUG):
    logger = logging.getLogger('loki_log')

    logger.setLevel(log_level)

    formatter = logging.Formatter('[%(asctime)s - %(levelname)s]: %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


def print_logo():
    try:
        ascii_art = pyfiglet.figlet_format("Loki", font="isometric1")
        termcolor.cprint(ascii_art, "green")
        termcolor.cprint("The modern network hacking toolkit", "red")
        termcolor.cprint("By Sten [Gespel] Heimbrodt\nhttps://sten-heimbrodt.de/\n\n", "light_blue")
    except pyfiglet.FigletError as e:
        print(f"Fehler beim Generieren der ASCII-Art: {e}")


class Loki:

    def __init__(self):
        self.logger = configure_logger()
        print_logo()
        time.sleep(0.5)
        self.f = Flooder(self.logger)
        self.d = Deceiver(self.logger)
        self.s = Scanners(self.logger)

    def get_scanner(self):
        return self.s

    def get_deceiver(self):
        return self.d

    def get_flooder(self):
        return self.f

    def start_console(self):
        while True:
            userinput = input("loki> ")
            self.parse_user_input(userinput)

    def parse_user_input(self, userinput):
        if userinput == "help" or userinput == "h":
            self.print_command_list()
        elif userinput == "exit":
            print("Bye! Have a good one")
            exit(0)

    def print_command_list(self):
        print("Enter one of the following commands to start the corresponding routine:")
        print("flood - start the flooding routine")
        print("scan - start the scanner routine")
        print("deceive - start the deceiver routine")