 
import Utility as util


class IO:
    def __init__(self):
        pass


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


    def save_data(self, fileName, data ):

        if type(data) is list:
            file = open( fileName + ".txt", "w", encoding="utf-8")
            data = util.justify_list_items(data)
            for alkio in data:
                row = str(alkio) + "\n"
                file.write( row )

        elif type(data) is dict:
            for key in data:
                file.writelines(data[key])
        else:
            return