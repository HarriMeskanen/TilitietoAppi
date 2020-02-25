

class Target:
    def __init__( self, name ):
        self.name = name
        self.entries = []
        self.sum = 0

    def add_entry(self, entry):
        self.entries.append(entry)
        self.sum += entry.val

    def __contains__(self, key):
        return key == self.name

    def __str__(self):
        s = self.name + "\n"
        for e in self.entries:
                s = s + "\t" + e.date.strftime('%d.%m.%Y') + "\t" + str(format(e.val, ".2f")) + "\n"
        s = s + "YHT. \t" + str( format(self.sum, ".2f"))
        return s

    def __len__(self): 
        return len(self.name)

