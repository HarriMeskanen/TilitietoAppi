
import Entry
import Target

class Database: 
    def __init__( self ):
        # List<Entry>
        self.entries    = []

        # dict<String, Target>
        self.targets    = {}

        # list<Entry>
        self.incomes    = []

        # list<Entry>
        self.expenses   = []

        # int
        self.number_of_entries  = 0

        # int
        self.key_max_length     = 0

    def add_entry( self, entry ):
        self.entries.append( entry )
        self.number_of_entries += 1
        if entry.val > 0:
            self.incomes.append( entry )
        else:
            self.expenses.append( entry )
        if len(entry.target) > self.key_max_length:
            self.key_max_length = len(entry.target)
            
    def add_target( self, entry):
        # if target doesnt exist, make new
        if entry.target not in self.targets:
            target = Target.make_target( entry.target )
        # else get existing one
        else:
            target = self.targets[entry.target]
        
        target.add_entry( entry )
        self.targets[entry.target] = target


def make_database( data ):
    db = Database()
    for data_row in data:
        # create new entry
        entry = Entry.make_entry( data_row )
        # abort if invalid entry data 
        if entry is None:
            continue
        db.add_entry( entry )
        db.add_target( entry )
    return db