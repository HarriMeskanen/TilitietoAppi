import sys
from Database import Database
import IO
import Utility as util
import Analytics

__DEBUG__ = True




def main(filename=None):
    io = IO.IO()
    data = io.get_data( filename )
    db = Database( data )

    processor = Analytics.DataProcessor()
    years = db.get_all()
    for year, year_data in years:
        processor.set_dataset( year_data )
        processor.process()
        io.save_data(year + ".txt" )

    print(util.bcolors.OKGREEN + "...\nProgram finished successfully... Exiting.")



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        if __DEBUG__:
            main("2019.txt")
        else:
            main(input("Path to tilitapahtumat:"))