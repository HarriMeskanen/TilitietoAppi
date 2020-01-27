
from datetime import datetime

class Entry:
    def __init__(self, date, target, val):
        self.date = date
        self.target = target
        self.val = val
        self.key_length = len(target)

def make_entry( entry_data ):
    lst_entry = entry_data.split("\t")
    try:
        date = lst_entry[2]
        date = datetime.strptime(date, '%d.%m.%Y')  
        val = lst_entry[3]
        val = val.replace(",", ".")
        val = float(val)
        target = lst_entry[4] 
    except Exception as e:
        print("Error:", e, "in entry_data: " + entry_data)
        return None
    return Entry( date, target, val )


        