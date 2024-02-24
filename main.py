import pprint

from Matrix3x3 import Matrix3x3
from HillCypher import HillCypher
from IntMod import IntMod
from AlphabetConfig import *

key = [[IntMod(2), IntMod(4), IntMod(1)],
       [IntMod(4), IntMod(1), IntMod(3)],
       [IntMod(7), IntMod(6), IntMod(4)]]
cypher = HillCypher(key)
cypher.info()
print(cypher.encrypt('cryptography'))
print(cypher.decrypt(cypher.encrypt('cryptography')))
