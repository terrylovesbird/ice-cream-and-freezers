import csv 
import os.path

from ice_cream import IceCream

class Freezer:
    
    def __init__(self):
        self.icecream_in_freezer = []

    def place_into_freezer(self, ic):
     
          #[{'flavor':0, 'batch':1, 'time':}]
        self.icecream_in_freezer.append(ic)


        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./ic_in_freezer.csv")


        with open(path, 'w') as csvfile:
            reader = csv.writer(csvfile)
            reader.writerow(['flavor', 'batch'])

            for row in self.icecream_in_freezer:
                reader.writerow([row.flavor, row.batch])
                

    def remove_from_freezer():
        pass