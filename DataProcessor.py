
import numpy as np
from Entry import Entry
from Date import DateType
from Date import Day
import Utility as util

class DataProcessor:
    def __init__(self):
        self.data = None
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

            self.__save_transactions(item)
            self.__calculate_incomes_and_expenses(item)
            #
            # CALCULATE OTHER STUFF
            #

            # process children recursively
            self.set_data(item.children)        
            self.process()


    def __save_transactions(self, item):
        targets = util.justify_list_items(item.entries)
        t = []
        for ii, e in enumerate(item.entries):
            e_str = e.get_date() + "\t" + targets[ii] + e.get_val_str()
            t.append(e_str)
        self.transactions[item.key_str] = t


    def __calculate_incomes_and_expenses(self, item):
        fx_extract = np.vectorize(lambda x: x.val)
        e = np.array(item.entries)
        values = fx_extract(e)
        self.expenses[item.key_str] = np.sum(values[values < 0] )
        self.incomes[item.key_str]  = np.sum(values[values >= 0])
        self.netsum[item.key_str]   = np.sum(values)
        

