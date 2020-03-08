
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
        self.key_str = "output"
        self.number_of_transactions  = 0
        self.number_of_datetypes    = 0
        self.number_of_targets  = 0
    
        for data_row in data:
            try:
                # parse date
                date, val, target =  Utility.get_transaction_data(data_row)
                # create new transaction
                transaction = Transaction(date, val, target)
                # add transaction to database
                transaction_key = self.datetime_to_key(transaction.date)
                self.add_transaction( transaction, transaction_key ) 
                self.number_of_transactions += 1
                print(Utility.bcolors.ENDC + "[Database]{e}".format(e=transaction))

            except Utility.InvalidDataException as e_data:
                print(Utility.bcolors.WARNING + e_data.message)
                print(Utility.bcolors.FAIL + "[Database]{dr}".format(dr=data_row))
                continue

            except Exception as e:
                print( Utility.bcolors.FAIL + str(e.args) )

        self.iterate(self)

    def child_factory(self, key):
        return Year(key) 

    def datetime_to_key(self, date):
        return np.array( (date.year, date.month, date.day) )

    def iterate(self, dt):

        for child in dt.children.values():
            self.number_of_datetypes += 1
            self.iterate(child)


