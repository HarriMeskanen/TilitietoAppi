import numpy as np
import Utility as util
import Transaction
import Target

class DateType:
    # self mask
    S = np.zeros(3)
    # child mask
    C = np.zeros(3)
    def __init__(self, key):
        # e.g. np.array( [1992, 6, 23] )
        self.key  = key
        self.key_str = DateType.key_to_str(key)
        self.transactions = Transaction.TransactionContainer()
        self.targets = Target.TargetContainer()
        # Map<date_key, DateType>, sub datetypes e.g. this==Month --> children are Days
        self.children   = {}

    def child_factory(self, key):
        return 0


    def __str__(self):
        return self.key_str

    @staticmethod
    def key_to_str(key):
        key_nonzero = key[key > 0]
        return ".".join(key_nonzero.astype(int).astype(str))

    # generate key for nth child EITHER from int or key
    def get_child_key(self, n_or_key):
        return self.key + self.C * n_or_key


    def __is_self(self, key):
        return (key == self.key).all() == True


    # is excisting child !!!
    def __is_child(self, key):
        return DateType.key_to_str(key) in self.children 


    def get_child(self, key):
        # check if key is me
        if self.__is_self(key):
            return self
        
        # if not me then create key for child
        child_key = self.get_child_key(key)
        child_key_str = DateType.key_to_str(child_key)

        # create new if child doesnt exist yet
        if not self.__is_child(child_key):
            self.children[child_key_str] = self.child_factory(child_key)

        # iterate recursively
        return self.children[child_key_str].get_child(key)


    def add_transaction(self, transaction, key):
        # add transaction to parent's transactions too... 
        self.transactions.add_transaction(transaction)        
        self.targets.add_transaction(transaction)

        # break iteration if key is me
        if self.__is_self(key):            
            return
        
        # if key is no me then it is one my children
        child_key = self.get_child_key(key)
        child_key_str = DateType.key_to_str(child_key)

        # create new if child doesnt exist yet
        if not self.__is_child(child_key):
            self.children[child_key_str] = self.child_factory(child_key)

        # iterate recursively
        self.children[child_key_str].add_transaction(transaction, key)



class Year(DateType):
    S = np.array(( 1, 0, 0 ))
    C = np.array(( 0, 1, 0 ))
    def __init__(self, key):
        super(Year, self).__init__(key)


    def child_factory(self, key):
        return Month(key) 



class Month(DateType):
    S = np.array(( 1, 1, 0 ))
    C = np.array(( 0, 0, 1 ))
    def __init__(self, key):
        super(Month, self).__init__(key)


    def child_factory(self, key):
        return Day(key)



class Day(DateType):
    S = np.array(( 1, 1, 1 ))
    def __init__(self, key):
        super(Day, self).__init__(key)
        


