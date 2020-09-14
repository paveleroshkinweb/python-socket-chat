from .socket_helper import SocketHelper
import socket
import sys
from contextlib import suppress
import logging


class AppSocket(SocketHelper):

    def __init__(self, config):
        super().__init__(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.config = config

    def exit(self, msg='', code=0):
        with suppress(Exception):
            sys.stdout.flush()
            self.socket.close()
        if msg:
            if code != 0:
                logging.error(msg)
            else:
                logging.info(msg)
        exit(code)
