from datetime import datetime
from colorama import init

init()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class InvalidDataException(Exception): 
    def __init__(self, message):
        self.message = "[InvalidDataException]" + message


 

def dict_plus_equals_value(container, key, value):
        if key in container: 
            if type(container[key]) is type(value):
                container[key] += value
        else:
            container[key] = value   


def justify_list_items( lst, format_char = " " ):
    key_max_length = len(max(lst, key = len))
    justified = []
    for item in lst:
        justified.append( item.targetName + format_char * ( key_max_length - len(item) ) ) 
    return justified


def get_entry_data( raw_data ):
    lst_entry = raw_data.split("\t")
    if len(lst_entry) < 5: 
        raise InvalidDataException("Data contains invalid number of elements: " + str(lst_entry))

    try:
        date = lst_entry[2]
        date = datetime.strptime(date, '%d.%m.%Y') 
    except Exception:
        raise InvalidDataException("Unable to create date object from string: " + lst_entry[2])

    try:
        val = lst_entry[3]
        val = val.replace(",", ".")
        val = float(val)
    except Exception: 
        raise InvalidDataException("Invalid transaction value: " + lst_entry[3])

    try:
        targetName = lst_entry[4]
        if targetName == "":
            raise InvalidDataException("Invalid transaction target: " + lst_entry[4])
        
    except Exception: 
        raise InvalidDataException("Invalid transaction target: " + lst_entry[4])

    return date, val, targetName

        

