import os
import Utility as util
from Date import DateType
import matplotlib.pyplot as plt
import numpy as np

# input output
class IO:
    def __init__(self):
        pass

    def set_root(self, filepath):
        self.root = os.path.dirname(os.path.realpath(filepath)) + "\\"


    def get_data(self, file):
        content = []
        try:
            file = open( file, "r", encoding="utf-8")
        except:
            print(util.bcolors.FAIL + "File: " + file + " not found. Exiting.")
            return
        for row in file:
            if row != "\n":
                content.append(row)
        file.close()
        return content


    def save_data(self, data, path_rel):
        
        # if filepath doesnt exist create folder
        dir = self.root + path_rel

        if not os.path.exists(dir):
            os.makedirs(dir)
        
        file_prefix = data.key_str

        self.save_log( data.transactions.get_transaction_log(data.targets.key_max_length), dir + file_prefix  + '_transactions.txt')
        self.save_log( data.targets.get_target_log(), dir + file_prefix  + '_transaction_targets.txt')
        self.save_incomes_expenses_as_barchart( data.key_str, data.children, dir + file_prefix + '_incomes-and-expenses.png')


        for child in data.children.values():
            self.save_data(child, path_rel + child.key_str + "\\")


    def save_incomes_expenses_as_barchart(self, title, children, fpath):
        labels      = []
        incomes     = []
        expenses    = []
        netsum      = []

        for child in children.values():
            labels.append(child.key_str.split('.')[-1])
            incomes.append(int(child.transactions.incomes))
            expenses.append(int(child.transactions.expenses * -1))
            netsum.append(int(child.transactions.netsum))
        
        fig = util.bar_chart_factory(title, labels, incomes, expenses)
        if fig != None:            
            fig.savefig(fpath)





    def save_log(self, log, fpath):
        # check filename for different call types

        if '.' not in fpath:
            fpath += ".txt"

        # open file for write
        file = open( fpath, "w", encoding="utf-8")

        # save log
        file.write( log )

        # close file
        file.close()


        