import sys
import time
from Database import Database
from DataProcessor import DataProcessor
from ipop import IO
import Utility as util


__DEBUG__ = True


def main(filename=None):

    io = IO()
    io.set_root( filename )
    print(util.bcolors.OKGREEN + "...\nStarting database build process...")
    time.sleep(1)

    # create database
    data = io.get_data( filename )
    db   = Database( data )    
    print(util.bcolors.OKGREEN + "...\n[COMPLETE] Database build finished\
    \nNumber of transactions saved: " + str(db.number_of_transactions) +
    "\nNumber of DateType objects created: " + str(db.number_of_datetypes))
    time.sleep(1)
    print(util.bcolors.OKGREEN + "...\nStarting to process collected data...")
    time.sleep(1)

    # process data
    prcsr  = DataProcessor()
    output = prcsr.process(db)
    print(util.bcolors.OKGREEN + "...\nData processing completed...")
    time.sleep(1)


    # save and present results
    print(util.bcolors.OKGREEN + "...\nSaving results to " + io.root)
    time.sleep(1)
    io.save_output(output, io.root + '\\' + output.key)

    print(util.bcolors.OKGREEN + "...\nProgram finished successfully. Exiting...")



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        if __DEBUG__:
            main("2019.txt")
        else:
            main(input("Path to tilitapahtumat:"))