#runner file
from ice_cream import IceCream
from flavor import Flavor
from freezer import Freezer

#iceCream = IceCream(Flavor.VANILLA)
IceCream.make_icecream(Flavor.VANILLA)
a = IceCream.get_icecream(0)
print(a)

f = Freezer()
f.place_into_freezer(a)