
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
        self.t0 = None
        self.tk = None
    
        for data_row in data:
            try:
                # parse date
                date, val, target_name =  Utility.get_transaction_data(data_row)
                
                # see if this is youngest of oldest transaction instance
                self.update_date_limits(date)
                
                # create new transaction
                transaction = Transaction(date, val, target_name)

                # add transaction to database
                transaction_key = self.datetime_to_key(transaction.date)
                self.add_transaction( transaction, transaction_key )
                print(Utility.bcolors.ENDC + "New Transaction {t}".format(t=transaction))


            except Utility.InvalidDataException as e_data:
                print(Utility.bcolors.WARNING + e_data.message)
                print(Utility.bcolors.FAIL + "{dr}".format(dr=data_row))
                continue

            except Exception as e:
                print( Utility.bcolors.FAIL + str(e.args) )


    def child_factory(self, key):
        return Year(key) 


    def datetime_to_key(self, date):
        return np.array( (date.year, date.month, date.day) )


    def update_date_limits(self, date):
        if self.t0 == None or date < self.t0:
            self.t0 = date

        if self.tk == None or date > self.tk:
            self.tk = date

