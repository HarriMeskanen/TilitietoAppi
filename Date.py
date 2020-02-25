


class DateType:
    def __init__(self, instance_number):
        # str
        self.n        = instance_number
        self.children = {}
        self.entries  = []

    def __contains__(self, n):
        return n in self.children



class DateTypeContainer:
    def __init__(self):
        self.container = {}
        self.entries = []

    def get_all(self):
        return self.container

    def get_year(self, year_number):
        if year_number not in self.container:
            return Year(year_number)
        return self.container[year_number]

    def get_month(self, year, month):
        year = self.get_year(year)        
        return year.get_child(month)

    def get_day(self, year, month, day):
        month = self.get_month(year, month)
        return month.get_child(day)

    def add_entry(self, entry):
        y = self.get_year(entry.date.year)
        y.add_entry(entry)
        self.container[entry.date.year] = y
        self.entries.append(entry)
        


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

