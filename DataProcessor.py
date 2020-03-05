
import numpy as np
from Transaction import Transaction
from Date import DateType
from Date import Day
import Utility as util
from DataStructure import DataStructure

class DataProcessor:
    def __init__(self):
        self.data = None
        self.dataStructures = np.array
        self.transactions   = {}
        self.incomes        = {}
        self.expenses       = {}
        self.netsum         = {}
        

    def set_data(self, data):
        if isinstance(data, list):
            self.data = data
        elif isinstance(data, dict):
            self.data = data.values()
        elif isinstance(data, DateType):
            self.data = [data]
        else:
            return False
        return True
        


    def process(self):
        for item in self.data:

            # resurcion break condition
            if not isinstance(item, DateType) or isinstance(item, Day):
                break

            self.__calculate_incomes_and_expenses(item)
            self.__save_transactions(item)
            #
            # CALCULATE OTHER STUFF
            #

            # process children recursively
            self.set_data(item.children)        
            self.process()


    def __save_transactions(self, item):
        targets, kml = util.justify_list_items(item.transactions)
        ts = []
        for ii, t in enumerate(item.transactions):
            t_str = t.get_date() + "\t" + targets[ii] + t.get_val_str()
            ts.append(t_str)
        ts.append("--" * kml)
        ts.append("INCOMES " + " " * kml + "\t+" + str(format(self.incomes[item.key_str],  '.2f')))
        ts.append("EXPENSES" + " " * kml + "\t"  + str(format(self.expenses[item.key_str], '.2f')))
        ts.append("SUM     " + " " * kml + "\t"  + str(format(self.netsum[item.key_str],   '.2f')))
        self.transactions[item.key_str] = ts


    def __calculate_incomes_and_expenses(self, item):
        fx_extract = np.vectorize(lambda x: x.val)
        t = np.array(item.transactions)
        values = fx_extract(t)
        self.expenses[item.key_str] = np.sum(values[values < 0] )
        self.incomes[item.key_str]  = np.sum(values[values >= 0])
        self.netsum[item.key_str]   = np.sum(values)
        

