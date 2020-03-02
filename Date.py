


class DateType:
    x = 0
    def __init__(self, key=None, n=None):
        # unique id e.g. 20201120
        self.key  = key
        # self is parent's nth children
        self.n = n
        # Map<date_key, DateType>, sub datetypes e.g. this==Month --> children are Days
        self.children   = {}
        # List<Entry>, entries created during datetype(this) period
        self.entries    = []

    def __contains__(self, key):
        return key in self.children

    # VIRTUAL
    def __child_factory(self, key):
        return 0

    # key --> my nth children
    def decode_key(self, key):
        return int( (key - self.key) / self.x )

    # generate key for nth child
    def encode_key(self, key):
        return self.key + self.decode_key(key) * self.x

    def __key_is_self(self, key):
        return key == self.key

    def __key_is_descendant(self, key):
        return (self.key % key) == self.key

    def __add_new_child(self, n):
        key = self.encode_key(n)
        child = self.__child_factory(key)
        self.children[n] = child

    def get_child(self, key):
        key_masked = self.decode_key(key)
        if key_masked not in self:
            self.__add_new_child(key)
        return self.children[n]

    def add_entry(self, entry, entry_key):
        if self.__key_is_self(entry_key):
            self.entries.append(entry)
            return
        
        elif self.__key_is_descendant(entry_key):
            c = self.get_child(entry.date.day)
            c.add_entry(entry)
            self.children[c.n] = c
            self.entries.append(entry)

        else:
            return # shouldn't go here ever
        



class Year(DateType):
    x_encode = 10000
    x_decode = 100    
    def __init__(self, key, n):
        super(Year, self).__init__(key, n)  
      
    def __child_factory(self, key, n):
        return Month(key, n) 



class Month(DateType):
    x_encode = 100
    x_decode = 1 
    def __init__(self, key, n):
        super(Month, self).__init__(key, n)

    def __child_factory(self, key, n):
        return Day(key, n)



class Day(DateType):
    x_encode = 1
    def __init__(self, key, n):
        super(Day, self).__init__(key, n)
        


