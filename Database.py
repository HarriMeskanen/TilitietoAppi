
from Transaction import Transaction
from Target import Target
from Date import DateType, Year, Month, Day
import Utility as util
from datetime import datetime
import numpy as np


class Database(DateType):
    C = np.array( (1, 0, 0) )

    def __init__( self, data ):
        super(Database, self).__init__(np.array( (0, 0, 0) ))
        self.key_str = "output"
        self.t0 = None
        self.tk = None
    
        for data_item in data:
            if len(data_item) == 3:
                date, val, target_name = data_item[0], data_item[1], data_item[2]
                transaction_category = None

            # data also contains category
            elif len(data_item) == 4:
                date, val, target_name, transaction_category = data_item[0], data_item[1], data_item[2], data_item[3]

            else: 
                print(util.bcolors.WARNING + "Unexpected data item: " + data_item)
                continue
            
            # see if this is youngest of oldest transaction instance
            self.update_date_limits(date)
            
            # create new transaction
            transaction = Transaction(date, val, target_name, transaction_category)

            # add transaction to database
            transaction_key = self.datetime_to_key(transaction.date)
            self.add_transaction( transaction, transaction_key )
            print(util.bcolors.ENDC + "New Transaction {t}".format(t=transaction))




    def child_factory(self, key):
        return Year(key) 


    def datetime_to_key(self, date):
        return np.array( (date.year, date.month, date.day) )


    def update_date_limits(self, date):
        if self.t0 == None or date < self.t0:
            self.t0 = date

        if self.tk == None or date > self.tk:
            self.tk = date

