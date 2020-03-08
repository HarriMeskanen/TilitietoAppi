
import numpy as np
from Transaction import Transaction
from Date import DateType
from Date import Day
import Utility as util
from DataStructure import DataStructure

class DataProcessor:
    def __init__(self):
        pass


    def process(self, data):
        
        print(util.bcolors.ENDC + "[DataProcessor] Processing data object from time period " + data.key_str)
        ds = DataStructure(data)
        ds.incomes, ds.expenses, ds.netsum = self.__calculate_incomes_and_expenses(data.transactions)
        ds.catalog = self.__save_catalog(data.transactions, ds.incomes, ds.expenses, ds.netsum)

        for child in data.children.values():
            ds.children.append( self.process(child) )
        
        return ds


    def __save_catalog(self, transactions, incomes, expenses, netsum):
        targets, kml = util.justify_list_items(transactions)
        ts = []
        for ii, t in enumerate(transactions):
            t_str = t.get_date() + "\t" + targets[ii] + t.get_val_str()
            ts.append(t_str)
        ts.append("--" * kml)
        ts.append("INCOMES " + " " * kml + "\t+" + str(format(incomes,  '.2f')))
        ts.append("EXPENSES" + " " * kml + "\t"  + str(format(expenses, '.2f')))
        ts.append("SUM     " + " " * kml + "\t"  + str(format(netsum,   '.2f')))
        return ts


    def __calculate_incomes_and_expenses(self, transactions):
        fx_extract = np.vectorize(lambda x: x.val)
        t = np.array(transactions)
        values = fx_extract(t)
        expenses = np.sum(values[values < 0] )
        incomes  = np.sum(values[values >= 0])
        netsum   = np.sum(values)
        return incomes, expenses, netsum
        

