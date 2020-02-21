import sys
import Database as db
import formatting as frm

__DEBUG__ = False


def get_data(file):
    content = []
    try:
        file = open( file, "r", encoding="utf-8")
    except:
        print(frm.bcolors.FAIL + "File: " + file + " not found. Exiting.")
        return
    for row in file:
        if row != "\n":
            content.append(row)
    file.close()
    return content


def save_data( fileName, data ):

    if type(data) is list:
        file = open( fileName + ".txt", "w", encoding="utf-8")
        data = frm.format_list(data)
        for alkio in data:
            row = str(alkio) + "\n"
            file.write( row )

    elif type(data) is dict:
        for key in data:
            file.writelines(data[key])

    else:
        return



def main(filename=None):

    data = get_data( filename )
    if data == None:
        return
    database = db.make_database( data )
    if database == None:
        return
    save_data(filename + "_parsittu", database.entries)
    save_data(filename + "_kohteet", database.targets)

    

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        if __DEBUG__:
            main("2019.txt")
        else:
            main(input("Path to tilitapahtumat:"))