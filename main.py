import sys
import keyword as kw
import Database as db


def MACRO_HEADER(header):
    return "<" + 10*"=" + header + (15-len(header))*"=" + ">\n"

"""
def MACRO_FORMAT(key):
    return (KEY_MAX_LENGTH - len(key))*" " + "\t"
"""

def is_key_in_keywords(key, kws):
    key = key.upper()
    for kw in kws:
        if kw in key:
            return True
    return False


def get_month(date):
    kk_lst = [
        "Tammikuu", 
        "Helmikuu", 
        "Maaliskuu", 
        "Huhtikuu", 
        "Toukokuu", 
        "Kesäkuu", 
        "Heinäkuu", 
        "Elokuu", 
        "Syyskuu", 
        "Lokakuu",
        "Marraskuu", 
        "Joulukuu"  ]
    try:
        month = int(date.split(".")[1])
        return kk_lst[month-1]
    except:
        return None


def get_data(file):
    content = []
    try:
        file = open( file, "r", encoding="utf-8")
    except:
        print("File: " + file + " not found. Exiting.")
        return
    for row in file:
        if row != "\n":
            content.append(row)
    file.close()
    return content


def divide_into_tulos_and_menos(entries):
    tulos = {} 
    menos = {}

    for key, value in entries.items():
        if value > 0:
            tulos[key] = value
        else:
            menos[key] = value

    return tulos, menos

    
def categorize_menos(menos):
    kiinteat = {}
    ruoka    = {}
    bensa    = {}
    random   = {}

    for key, val in menos.items():
        if is_key_in_keywords(key, kw.kiinteat):
            kiinteat[key] = val

        elif is_key_in_keywords(key, kw.bensa):
            bensa[key] = val

        elif is_key_in_keywords(key, kw.ruoka):
            ruoka[key] = val

        else:
            random[key] = val

    return {"kiinteät" : kiinteat, 
            "ruoka" : ruoka,
            "bensa" : bensa,
            "muut"  : random }

"""
def save_results(data, filename):
    summary = open( filename +".txt", "w", encoding="utf-8")

    for superkey in data.keys():

        summary.write(MACRO_HEADER(superkey.upper()))
        for key, value in data[superkey].items():
            summary.write(key + MACRO_FORMAT(key) + str(value) + "\n")
            
        summary.write(MACRO_FORMAT("")[0:-1] + "+" "\n")
        summary.write(MACRO_FORMAT("") + str(sum(data[superkey].values())) + "\n")
        summary.write("\n")

    summary.close()
"""

def main(filename=None):

    data = get_data( filename )
    if data == None:
        return
    database = db.make_database( data )
    if database == None:
        return

    

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        main(input("Path to tilitapahtumat:"))