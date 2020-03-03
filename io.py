import os
import Utility as util
from Date import DateType


class IO:
    def __init__(self):
        self.outputFolder = os.getcwd() + r'\output'


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


    def write_dict_to_file(self, d, filename_prefix = ""):
        for key, value in d.items():
            filepath = self.outputFolder + "\\" + key
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            file = open( filepath + "\\" + filename_prefix + key + ".txt", "w", encoding="utf-8")
            for elem in value:
                row = elem + "\n"
                file.write( row )
            file.close()
