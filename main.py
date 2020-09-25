import sys
import os
sys.path.append("C:\\Users\\meskaha\\Documents\\Python\\ML")

import numpy as np
import time
from Database import Database
from ipop import IO
import Utility as util

#import Clustering

__DEBUG__ = True


def main(filename=None):

    io = IO()
    io.set_root( filename )
    print(util.bcolors.OKGREEN + "...\nStarting database build process...")
    time.sleep(1)

    # create database
    data_list, data_array = io.get_data( filename )
    #ci, cm = k_means(data_array, 10)

    db = Database( data_list )
    print(util.bcolors.OKGREEN + "...\n[COMPLETE] Database build finished\
    \nNumber of transactions saved: " + str(len(db.transactions)) +
    "\nTime period: " + str(db.t0) + " - " + str(db.tk))


    # save and present results
    print(util.bcolors.OKGREEN + "...\nSaving results to " + io.root)
    time.sleep(1)
    io.save_data(db, db.key_str + "\\")

    print(util.bcolors.OKGREEN + "...\nProgram finished successfully. Exiting...")



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        if __DEBUG__:
            main("2019.txt")
    else:
        main(input("Path to tilitapahtumat:"))