import os
import Utility as util
from Date import DateType
import matplotlib.pyplot as plt


class IO:
    def __init__(self):
        pass

    def set_root(self, filepath):
        self.root = os.path.dirname(os.path.realpath(filepath))


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


    def save_output(self, data, fpath):
        
        # if filepath doesnt exist create folder
        if not os.path.exists(fpath):
            os.makedirs(fpath)

        fname = fpath + '\\' + data.key + '_catalog.txt'
        self.write_list_to_file( data.catalog, fname )

        for child in data.children:
            self.save_output(child, fpath + '\\' + child.key)


    def write_list_to_file(self, lst, fpath):
        # check filename for different call types

        if '.' not in fpath:
            fpath += ".txt"

        # open file for write
        file = open( fpath, "w", encoding="utf-8")

        # write list elements to file
        for elem in lst:
            row = elem + "\n"
            file.write( row )

        # close file
        file.close()
