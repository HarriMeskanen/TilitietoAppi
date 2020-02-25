
from Entry import Entry
from Target import Target
import Date
import Utility 


class Database: 
    def __init__( self, data ):
        self.__locked           = False
        self.__dateContainer    = Date.DateTypeContainer()
        self.__targetContainer  = {}
        self.number_of_entries  = 0
        self.number_of_targets  = 0
        self.key_max_length     = 0
    
        for data_row in data:
            try:
                # parse date
                date, val, targetName =  Utility.get_entry_data(data_row)
                # create new entry
                entry = Entry(date, val, targetName)
                # add entry to database
                self.add_entry( entry )
                print(Utility.bcolors.OKGREEN + "[Database.__init__][SUCCESS]{e}".format(e=entry))
            except Utility.InvalidDataException as e_data:
                print(Utility.bcolors.WARNING + e_data.message)
                print(Utility.bcolors.FAIL + "[Database.__init__][FAILURE]{dr}".format(dr=data_row))
                continue

            except Exception as e:
                print( Utility.bcolors.FAIL + e.args )

        print(Utility.bcolors.OKBLUE + "[Database.__init__][COMPLETE] Database build finished.\n\
        Number of transaction entries created: " + str(self.number_of_entries) + "\n\
        Number of transaction targets created: " + str(self.number_of_targets))
        self.__locked = True

    def get_all(self):
        return self.__dateContainer.get_all()


    def get_year(self, year):
        return self.__dateContainer.get_year(year)


    def get_month(self, year, month):
        return self.__dateContainer.get_month(year, month)


    def get_day(self, year, month, day):
        return self.__dateContainer.get_day(year, month, day)


    def add_entry( self, entry ):
        self.number_of_entries += 1
        self.__add_to_targetContainer( entry )
        self.__dateContainer.add_entry( entry )
                
          
    def __add_to_targetContainer(self, entry):
        # if target doesnt exist, make new
        if entry.get_target() not in self.__targetContainer:
            target = Target( entry.targetName )
            self.number_of_targets += 1
            if len(target.name) > self.key_max_length:
                self.key_max_length = len(target.name)
        # else get existing one
        else:
            target = self.__targetContainer[entry.targetName]
        # add entry to target
        target.add_entry( entry )
        # add target to database
        self.__targetContainer[target.name] = target

