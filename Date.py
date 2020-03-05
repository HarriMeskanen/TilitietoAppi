import numpy as np


class DateType:
    x = 0
    def __init__(self, key=None, n=None):
        # unique id e.g. 20201120
        self.key  = key
        self.key_str = self.__key_str__()
        # self is parent's nth children
        self.n = n
        # Map<date_key, DateType>, sub datetypes e.g. this==Month --> children are Days
        self.children   = {}
        # List<Transaction>, transactions created during datetype(this) period
        self.transactions    = []

    def __str__(self):
        return self.key_str

    def __key_str__(self):
        key_str = str(self.key)
        if len(key_str) != 8:
            return key_str
        key_lst = np.array([key_str[6:8], key_str[4:6], key_str[0:4]]).astype(int)
        key_lst = key_lst[key_lst > 0].astype(str)
        return ".".join(key_lst)

    # VIRTUAL
    def child_factory(self, key, n):
        return 0
    
    # generate key for nth child
    def generate_key(self, n):
        return self.key + n * self.x

    def mask_key(self, key):
        n = self.decode_key(key)
        return self.generate_key(n)

    # key --> my nth children
    def decode_key(self, key):
        return int( (key - self.key) / self.x )

    # generate key (from key) for nth child
    def encode_key(self, key):
        return self.key + self.decode_key(key) * self.x

    def __key_is_self(self, key):
        return key == self.key

    def __key_is_descendant(self, key):
        return (self.key % key) == self.key

    def __add_new_child(self, key):
        n = self.decode_key(key)
        child = self.child_factory(key, n)
        self.children[key] = child

    def get_child(self, key):
        child_key = self.mask_key(key)
        if child_key not in self.children:
            self.__add_new_child(child_key)
        return self.children[child_key]

    def add_transaction(self, transaction, key):
        if self.__key_is_self(key):
            self.transactions.append(transaction)
            return
        
        elif self.__key_is_descendant(key):
            c = self.get_child(key)
            c.add_transaction(transaction, key)
            self.children[c.key] = c
            self.transactions.append(transaction)

        else:
            return # shouldn't go here, ever
        



class Year(DateType):
    x = 100    
    def __init__(self, key, n):
        super(Year, self).__init__(key, n)  
      
    def child_factory(self, key, n):
        return Month(key, n) 



class Month(DateType):
    x = 1 
    def __init__(self, key, n):
        super(Month, self).__init__(key, n)

    def child_factory(self, key, n):
        return Day(key, n)



class Day(DateType):
    def __init__(self, key, n):
        super(Day, self).__init__(key, n)
        


