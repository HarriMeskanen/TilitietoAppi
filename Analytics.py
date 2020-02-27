
#import matplotlib.pyplot as plt
from Entry import Entry
from Date import DateType
import Utility as util

class DataProcessor:
    def __init__(self):
        self.data = None
        self.incomes    = {}
        self.expenses   = {}
        self.netsum     = {}
        

    def set_data(self, data):
        if type(data) == type(dict):
            self.data = data
        elif type(data) == type(DateType):
            self.data = { data.n : data }
        else:
            return False
        return True


    def process(self, resursion = False):
        for n, obj in self.data:
            self.__calculate_incomes_and_expenses(obj)


    def __calculate_incomes_and_expenses(self, obj):
        data = self.data
        incomes     = None
        expenses    = None 
        netsum      = None
        for entry in obj.entries:
            pass



    def __calculate_incomes_and_expenses(self):
        data = self.data
        incomes     = None
        expenses    = None 
        netsum      = None

        for key, value in data.items():
            for entry in value.entries:
                val = entry.val
                if val < 0:
                    expenses += val
                else:
                    incomes += val
            netsum = incomes + expenses
            util.dict_plus_equals_value(self.incomes, key, incomes)
            util.dict_plus_equals_value(self.expenses, key, expenses)
            util.dict_plus_equals_value(self.netsum, key, netsum)


