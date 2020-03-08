import numpy as np
import Utility as util

class DataStructure:
    def __init__(self, datetype):
        self.key            = datetype.key_str
        self.incomes        = float
        self.expenses       = float
        self.netsum         = float
        self.catalog        = [] 
        self.children       = []
