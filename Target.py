

class Target:
    def __init__( self, name ):
        self.name = name
        self.entries = []
        self.sum = 0

    def add_entry(self, entry):
        self.entries.append(entry)
        self.sum += entry.val

def make_target( target_name ):
    if target_name != "":
        return Target( target_name )
    else: 
        return None
