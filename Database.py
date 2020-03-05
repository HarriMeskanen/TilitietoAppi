
from Transaction import Transaction
from Target import Target
from Date import DateType, Year, Month, Day
import Utility 
from datetime import datetime


class Database(DateType): 
    x = 10000
    def __init__( self, data ):
        super(Database, self).__init__(0)
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

    def child_factory(self, key, n):
        return Year(key, n) 

    def datetime_to_key(self, date):
        return self.x * date.year + Year.x * date.month + Month.x * date.day

    def get_all(self):
        return self.children

    def get_year(self, year_number):
        key = self.generate_key(year_number)
        if year_number not in self:
            return Year(key, year_number)
        return self.children[year_number]

    def get_month(self, year, month):
        year = self.get_year(year)        
        return year.get_child(month)

    def get_day(self, year, month, day):
        month = self.get_month(year, month)
        return month.get_child(day)

    def add_transaction( self, transaction, key):
        c = self.get_child(key)
        c.add_transaction(transaction, key)
        self.children[c.key] = c
        self.transactions.append(transaction)
        self.number_of_transactions += 1


