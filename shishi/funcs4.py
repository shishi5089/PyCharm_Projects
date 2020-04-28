# file is a module
from funcs3 import *  # imports everything
from math import sqrt, floor
from operator import itemgetter

say_hi()
greet("Musa")

print(say_hi.__doc__)

print(itemgetter.__doc__)

converter2(1000 , "USD", accuracy=2)
converter2(1000 , "GBP", accuracy=3)
converter2(1000 , "UGX", accuracy=4)
converter2(1000 , "TZS", accuracy=1)

converter3(400 , "dis_cm", accuracy= 2)
converter3(487 , "dis_km", accuracy= 2)
converter3(47 , "dis_th", accuracy= 2)
