
from datetime import datetime

class Entry:
    def __init__(self, date, val, target):
        self.date       = date
        self.val        = val
        self.targetName = target

    def __str__(self):
        return self.date.strftime('%d.%m.%Y') + "\t" + self.targetName + "\t" + str(format(self.val, '.2f'))

    def __len__(self):
        return len(self.targetName)

    def __add__(self, other):
        return self.get_val() + other.get_val()

    def get_date(self):
        return self.date.strftime('%d.%m.%Y')

    def get_val(self):
        return str(format(self.val, '.2f'))

    def get_target(self):
        return self.targetName




        