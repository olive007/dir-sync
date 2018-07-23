#!/usr/bin/env python3

from src.daemon import ServerDaemon

if __name__ == '__main__':

    daemon = ServerDaemon()

    daemon.start()
