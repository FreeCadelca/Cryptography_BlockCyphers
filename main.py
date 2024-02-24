import pprint

from Matrix3x3 import Matrix3x3
from HillCypher import HillCypher
from IntMod import IntMod
from AlphabetConfig import *
from RecHillCypher import RecHillCypher

# key = [[IntMod(2), IntMod(4), IntMod(1)],
#        [IntMod(4), IntMod(1), IntMod(3)],
#        [IntMod(7), IntMod(6), IntMod(4)]]
#
# key2 = [[IntMod(6), IntMod(8), IntMod(9)],
#         [IntMod(3), IntMod(7), IntMod(1)],
#         [IntMod(5), IntMod(4), IntMod(8)]]

key = [[IntMod(3), IntMod(2)],
       [IntMod(6), IntMod(5)]]

key2 = [[IntMod(1), IntMod(4)],
        [IntMod(2), IntMod(9)]]

cypher = RecHillCypher(key, key2)
cypher.info()
print(cypher.encrypt('cryptography'))
print(cypher.decrypt(cypher.encrypt('cryptography')))
