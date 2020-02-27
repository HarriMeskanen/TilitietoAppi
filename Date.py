


class DateType:
    def __init__(self):
        pass
    
    def __init__(self, n):
        # järj. luku
        self.n          = int(n)
        # sub datetypes e.g. this==Month --> children are Days
        self.children   = {}
        # entries created during datetype(this) period
        self.entries    = []

    def __contains__(self, n):
        return n in self.children

   

class Year(DateType):
    def __init__(self, year_number):
        super(Year, self).__init__(year_number)


    def get_month(self, month_number):
        if month_number not in self:
            self.children[month_number] = Month(month_number)
        return self.children[month_number]

    def add_entry(self, entry):
        m = self.get_month(entry.date.month)
        m.add_entry(entry)
        self.children[entry.date.month] = m 
        self.entries.append(entry)



class Month(DateType):
    def __init__(self, month_number):
        super(Month, self).__init__(month_number)

    def get_day(self, day_number):
        if day_number not in self:
            self.children[day_number] = Day(day_number)
        return self.children[day_number]

    def add_entry(self, entry):
        d = self.get_day(entry.date.day)
        d.add_entry(entry)
        self.children[entry.date.day] = d
        self.entries.append(entry)



class Day(DateType):    
    def __init__(self, day_number):
        super(Day, self).__init__(day_number)

    def add_entry(self, entry):
        self.entries.append(entry)

