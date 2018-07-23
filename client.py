#!/usr/bin/env python3

from src.daemon import ClientDaemon

if __name__ == '__main__':

    daemon = ClientDaemon()

    daemon.start()
