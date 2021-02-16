# --------------- Main.py ---------------
# Supplied main function implementation for Scanner.
#
# Version:  Python 3.8
# Author:   Alex Hoke
# Date:		01/20/2021

from Scanner import Scanner
from Parser import Parser
from Core import Core
import sys


def main():
    # Initializes the parser class
    parser = Parser()
    parser.parse()

if __name__ == "__main__":
    main()
