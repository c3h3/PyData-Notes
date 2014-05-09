#!/usr/bin/env python
# -*- coding: utf8
import logging
from getpass import getuser
import subprocess as sp

# Setup logging
formatter = logging.Formatter(
    '[%(name)s:%(funcName)s][%(levelname)s][%(asctime)s] %(message)s',
    datefmt='%b %d %H:%M:%S'
)
logger = logging.getLogger('PlaY_Data')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()  # (std.stderr) will change to sys.stdout
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


_WELCOME_MSG = r'''
██████╗ ██╗      █████╗ ██╗   ██╗    ██████╗  █████╗ ████████╗ █████╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██████╔╝██║     ███████║ ╚████╔╝     ██║  ██║███████║   ██║   ███████║
██╔═══╝ ██║     ██╔══██║  ╚██╔╝      ██║  ██║██╔══██║   ██║   ██╔══██║
██║     ███████╗██║  ██║   ██║       ██████╔╝██║  ██║   ██║   ██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

    ██╗   ██╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ██╗████████╗
    ██║   ██║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝
    ██║   ██║███████║██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║
    ╚██╗ ██╔╝██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║
     ╚████╔╝ ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║
      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝
        ___         ___                _      ___  _      ___
       / _ \_   _  / __\___  _ __     /_\    / _ \/_\    / __\
      / /_)/ | | |/ /  / _ \| '_ \   //_\\  / /_)//_\\  / /
     / ___/| |_| / /__| (_) | | | | /  _  \/ ___/  _  \/ /___
     \/     \__, \____/\___/|_| |_| \_/ \_/\/   \_/ \_/\____/
            |___/
      ____   ___  _ _  _     _____      _ __    __
     |___ \ / _ \/ | || |   /__   \__ _(_) / /\ \ \__ _ _ __
       __) | | | | | || |_    / /\/ _` | \ \/  \/ / _` | '_ \
      / __/| |_| | |__   _|  / / | (_| | |\  /\  / (_| | | | |
     |_____|\___/|_|  |_|    \/   \__,_|_| \/  \/ \__,_|_| |_|
'''

local = lambda cmd: sp.check_output(
    cmd, stderr=sp.STDOUT, universal_newlines=True)

def welcome():
    logger.info("Greeting messages from PlaY Data")
    print(_WELCOME_MSG)

def check_rstudio_server():
    logger.info("Check RStudio status")
    sp.check_call("rstudio-server verify-installation", shell=True)

def main():
    logger.info("Execute commands by user: {}".format(getuser()))
    check_rstudio_server()


if __name__ == '__main__':
    welcome()
    main()
