# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys
sys.path.append(r"D:\Games")
print(sys.path)

# pyrefly: ignore [missing-import]
import elzero
print(dir(elzero))

elzero.sayHello("Ahmed")
elzero.sayHello("Osama")
elzero.sayHello("Mohamed")

elzero.sayHowAreYou("Ahmed")
elzero.sayHowAreYou("Osama")
elzero.sayHowAreYou("Mohamed")

# Alias
# pyrefly: ignore [import-as-alias, missing-import]
import elzero as ee

ee.sayHello("Ahmed")
ee.sayHello("Osama")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")
# 
# pyrefly: ignore [missing-import]
from elzero import sayHello

sayHello("Osama")

# pyrefly: ignore [missing-import]
from elzero import sayHello as ss

ss("Osama")