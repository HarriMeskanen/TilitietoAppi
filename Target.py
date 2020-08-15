import Transaction


class TargetContainer:
    def __init__(self):
        self.targets = {}
        self.key_max_length = 0


    def __contains__(self, key):
        return key in self.targets


    def add_target(self, t):
        self.targets[t.name] = t

        if len(t) > self.key_max_length:
            self.key_max_length = len(t)


    def add_transaction(self, t):
        if t.target not in self:            
            self.add_target(Target(t.target) )

        self.targets[t.target].add_transaction(t)


    def get_target_log(self):
        log = ''

        for t in self.targets.values():
            log += '\n\n\n' + t.get_transaction_log()

        return log




class Target(Transaction.TransactionContainer):
    def __init__( self, name ):
        Transaction.TransactionContainer.__init__(self)
        self.name = name
        # e.g. 'food' or 'car' or 'hobby'
        self.category = str

    def __len__(self):
        return len(self.name)


    def get_transaction_log(self):
        log = ''

        log += self.name + '\n' + '-' * len(self)

        for t in self.transactions:
            log += '\n' + t.get_date_str() + '\t' + t.get_val_str()

        log += '\nINCOMES  \t' + str(format(self.incomes,  '.2f'))
        log += '\nEXPENSES \t' + str(format(self.expenses, '.2f'))
        log += '\nNETSUM   \t' + str(format(self.netsum,   '.2f'))

        return log

