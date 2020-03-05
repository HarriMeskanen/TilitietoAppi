import matplotlib.pyplot as plt
from Date import DateType


class DataPresenter:
    def __init__(self):
        self.data = [] 

    def set_data(self, data):
        if isinstance(data, list):
            self.data = data
        elif isinstance(data, dict):
            self.data = data.values()
        elif isinstance(data, DateType):
            self.data = [data]
        else:
            return False
        return True

    