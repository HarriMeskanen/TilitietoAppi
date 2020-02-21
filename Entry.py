
from datetime import datetime
import formatting as frm

class Entry:
    def __init__(self, date, target, val):
        self.date = date
        self.targetName = target
        self.val = val

    def __str__(self):
        return self.date.strftime('%d.%m.%Y') + "\t" + self.targetName + "\t" + str(format(self.val, '.2f'))

    def __len__(self):
        return len(self.targetName)



def make_entry( entry_data ):
    lst_entry = entry_data.split("\t")
    try:
        date = lst_entry[2]
        date = datetime.strptime(date, '%d.%m.%Y')  
        val = lst_entry[3]
        val = val.replace(",", ".")
        val = float(val)
        targetName = lst_entry[4] 
    except Exception as e:
        print(frm.bcolors.WARNING + "[EXCEPTION]: '{error}'. Unable to create Entry from data row: {row}".format(error=e, row=entry_data))
        return None
    return Entry( date, targetName, val )


        