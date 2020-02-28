from datetime import datetime



def datetime_to_key(date):
    if type(date) == type(datetime):
        return Year.x_encode * date.year + Month.x_encode * date.month + Day.x_encode * date.day


class DateType:
    x_encode = None
    x_decode = None
    def __init__(self, key=None, n=None):
        # unique id e.g. 20201120
        self.key  = key
        # self is parent's nth children
        self.n = n
        # Map<n, DateType>, sub datetypes e.g. this==Month --> children are Days
        self.children   = {}
        # List<Entry>, entries created during datetype(this) period
        self.entries    = []

    # VIRTUAL
    def __child_factory(self, key):
        return -1

    # VIRTUAL
    def __decode_key(self, key):
        return int( (key - self.key) / self.x_decode )

    def __encode_key(self, n):
        return self.key + self.x_encode * n

    def __contains__(self, n):
        return n in self.children

    def __key_is_self(self, key):
        return key == self.key

    def __key_is_descendant(self, key):
        return (self.key % key) == self.key

    def __add_new_child(self, n):
        key = self.__encode_key(n)
        child = self.__child_factory(key)
        self.children[n] = child

    def get_child(self, n):
        if n not in self:
            self.__add_new_child(n)
        return self.children[n]

    def add_entry(self, entry):
        entry_key = datetime_to_key(entry.date)

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
        


