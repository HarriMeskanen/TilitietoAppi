

class Target:
    def __init__( self, name ):
        self.name = name
        self.transactions = []
        self.sum = 0

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.sum += transaction.val

    def __contains__(self, key):
        return key == self.name

    def __str__(self):
        s = self.name + "\n"
        for t in self.transactions:
                s = s + "\t" + t.date.strftime('%d.%m.%Y') + "\t" + str(format(t.val, ".2f")) + "\n"
        s = s + "YHT. \t" + str( format(self.sum, ".2f"))
        return s

    def __len__(self): 
        return len(self.name)

