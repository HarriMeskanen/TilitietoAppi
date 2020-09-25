
from datetime import datetime

class TransactionContainer:
    def __init__(self):
        self.transactions = []
        self.incomes = 0.0
        self.expenses = 0.0
        self.netsum = 0.0

    
    def get_transaction_log(self, kml):
        log = ''
        
        for t in self.transactions:
            whitespaces = ' ' * ( kml - len(t) )
            log += '\n' + t.get_date_str() + '\t' + t.target + whitespaces + t.get_val_str()

        log += '\n' + '--' * kml
        log += '\nINCOMES  ' + ' ' * kml + '\t' + str(format(self.incomes,  '.2f'))
        log += '\nEXPENSES ' + ' ' * kml + '\t' + str(format(self.expenses, '.2f'))
        log += '\nNETSUM   ' + ' ' * kml + '\t' + str(format(self.netsum,   '.2f'))
         
        return log


    def add_transaction(self, t):
        self.transactions.append(t)
        # process value
        val = t.val
        if val >= 0:
            self.incomes += val
        else:
            self.expenses += val
        self.netsum += val

    def __len__(self):
        return len(self.transactions)


class Transaction:
    def __init__(self, date, val, target, category=None):
        # datetime
        self.date   = date
        # float
        self.val    = float(val)
        # str
        self.target = target
        # str
        self.category = category

    def __str__(self):
        return self.date.strftime('%d.%m.%Y') + "\t" + self.target + "\t" + str(format(self.val, '.2f'))

    def __len__(self):
        return len(self.target)

    def __add__(self, other):
        return self.val + other

    def __radd__(self, other):
        return self.val + other

    def get_date_str(self):
        return self.date.strftime('%d.%m.%Y')

    def get_val_str(self):
        return str(format(self.val, '.2f'))

    def get_target(self):
        return self.target




        