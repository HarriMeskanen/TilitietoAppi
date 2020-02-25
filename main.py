import sys
from Database import Database
from io import IO
import Utility as util
import Analytics

__DEBUG__ = True




def main(filename=None):
    io = IO()
    processor = Analytics.DataProcessor()
    data = io.get_data( filename )
    db = Database( data )
    processor.dataset = db.get_all()
    daatta = processor.get_net_income_and_expense()
    print(util.bcolors.OKGREEN + "...\nProgram finished successfully... Exiting.")


    



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        if __DEBUG__:
            main("2019.txt")
        else:
            main(input("Path to tilitapahtumat:"))