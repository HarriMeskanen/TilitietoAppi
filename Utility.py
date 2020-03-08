from datetime import datetime
import numpy as np
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
        justified.append( item.target + format_char * ( key_max_length - len(item) ) ) 
    return justified, key_max_length


def get_transaction_data( raw_data ):
    lst_transaction = raw_data.split("\t")
    if len(lst_transaction) < 5: 
        raise InvalidDataException("Data contains invalid number of elements: " + str(lst_transaction))

    try:
        date = lst_transaction[2]
        date = datetime.strptime(date, '%d.%m.%Y') 
    except Exception:
        raise InvalidDataException("Unable to create date object from string: " + lst_transaction[2])

    try:
        val = lst_transaction[3]
        val = val.replace(",", ".")
        val = float(val)
    except Exception: 
        raise InvalidDataException("Invalid transaction value: " + lst_transaction[3])

    try:
        target = lst_transaction[4]
        if target == "":
            raise InvalidDataException("Invalid transaction target: " + lst_transaction[4])
        
    except Exception: 
        raise InvalidDataException("Invalid transaction target: " + lst_transaction[4])

    return date, val, target

        

