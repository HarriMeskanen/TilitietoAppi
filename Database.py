
from Transaction import Transaction
from Target import Target
from Date import DateType, Year, Month, Day
import Utility 
from datetime import datetime
import numpy as np


class Database(DateType):
    C = np.array( (1, 0, 0) )
    def __init__( self, data ):
        super(Database, self).__init__(np.array( (0, 0, 0) ))
        self.number_of_transactions  = 0
        self.number_of_targets  = 0
        self.key_max_length     = 0
    
        for data_row in data:
            try:
                # parse date
                date, val, target =  Utility.get_transaction_data(data_row)
                # create new transaction
                transaction = Transaction(date, val, target)
                # add transaction to database
                transaction_key = self.datetime_to_key(transaction.date)
                self.add_transaction( transaction, transaction_key )
                print(Utility.bcolors.OKGREEN + "[Database.__init__][SUCCESS]{e}".format(e=transaction))
            except Utility.InvalidDataException as e_data:
                print(Utility.bcolors.WARNING + e_data.message)
                print(Utility.bcolors.FAIL + "[Database.__init__][FAILURE]{dr}".format(dr=data_row))
                continue

            except Exception as e:
                print( Utility.bcolors.FAIL + str(e.args) )

        print(Utility.bcolors.OKBLUE + "[Database.__init__][COMPLETE] Database build finished.\n\
        Number of transaction transactions created: " + str(self.number_of_transactions) + "\n\
        Number of transaction targets created: " + str(self.number_of_targets))


    def child_factory(self, key):
        return Year(key) 

    def datetime_to_key(self, date):
        return np.array( (date.year, date.month, date.day) )

