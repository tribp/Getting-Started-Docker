#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test
"""

import time
import sys


def main():
    ###
    # Main
    ###
    counter =0
    breakpoint()
    while counter < 4:
    
        # Run in simulation
        counter +=1
        print("Running in simulation mode: ",counter)
        time.sleep(3)
    return 0

if __name__ == "__main__":
    sys.exit(main())


# End of program