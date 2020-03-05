import sys
from Database import Database
from DataProcessor import DataProcessor
import IO
import Utility as util

__DEBUG__ = True




def main(filename=None):
    io = IO.IO()
    data = io.get_data( filename )
    db = Database( data )

    prcsr = DataProcessor()
    prcsr.set_data( db )
    prcsr.process()

    io.write_dict_to_file(prcsr.transactions, "catalog_")

    print(util.bcolors.OKGREEN + "...\nProgram finished successfully... Exiting.")



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        if __DEBUG__:
            main("2019.txt")
        else:
            main(input("Path to tilitapahtumat:"))