# As a ice cream maker, I want to make different types of ice cream (peanut butter, chocolate chip, etc.).
# As a ice cream maker, I want to place batches of ice cream in an freezer.
# As a ice cream maker, I want to know when a batch of ice cream is ready to be removed from the freezer.
from flavor import Flavor

class IceCream:
    batch = 0
    icecream_we_have = []

    def __init__(self, flavor, batch):
        self.flavor = flavor
        self.batch = batch
        
    @classmethod
    def make_icecream(self, flavor):
        self.flavor = flavor
        #self.batch =0
        ic = IceCream(self.flavor, self.batch)
        self.batch +=1
        self.icecream_we_have.append(ic)

    @classmethod
    def get_icecream(cls,batch):
        for ic in cls.icecream_we_have:
            if ic.batch == batch:
                return ic
        return None

    def __str__(self):
        return f"{self.flavor} {self.batch}"

       


    

