
#import matplotlib.pyplot as plt
from Entry import Entry
from Date import DateType

class DataProcessor:
    def __init__(self):
        self.dataset    = None
        self.incomes    = {}
        self.expenses   = {}
        self.sum        = {}

    def process(self):
        self.__get_net_income_and_expense()

    def set_dataset(self, dataset):
        self.dataset = dataset

    def __get_net_income_and_expense(self):
        data = self.dataset
        if type(data) is dict:
            for key, value in data.items():
                self.sum[key] = sum(value.entries)
                for entry in value.entries:
                    val = entry.val
                    if val < 0:
                        self.expenses[key] += val
                    else:
                        self.incomes[key] += val
            
        for elem in data:
            if type(elem) is not Entry:
                continue
            val = elem.get_val()
            if val >= 0:
                income += val
            else:
                expense += val
                
        return income, expense


