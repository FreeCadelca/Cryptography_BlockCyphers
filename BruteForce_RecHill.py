from AlphabetConfig import *
from IntMod import IntMod

for a in range(0, m):
    for b in range(0, m):
        for c in range(0, m):
            for d in range(0, m):
                if (IntMod(3) * IntMod(a) + IntMod(8) * IntMod(b)).getValue() == 25:
                    if (IntMod(3) * IntMod(c) + IntMod(8) * IntMod(d)).getValue() == 9:
                        if (IntMod(24) * IntMod(a) + IntMod(4) * IntMod(b)).getValue() == 31:
                            if (IntMod(24) * IntMod(c) + IntMod(4) * IntMod(d)).getValue() == 17:
                                print(f'key1 = {a} {b}\n'
                                      f'       {c} {d}\n')

for e in range(0, m):
    for f in range(0, m):
        for g in range(0, m):
            for h in range(0, m):
                if (IntMod(12) * IntMod(e) + IntMod(0) * IntMod(f)).getValue() == 12:
                    if (IntMod(12) * IntMod(g) + IntMod(0) * IntMod(h)).getValue() == 24:
                        if (IntMod(0) * IntMod(e) + IntMod(19) * IntMod(f)).getValue() == 27:
                            if (IntMod(0) * IntMod(g) + IntMod(19) * IntMod(h)).getValue() == 24:
                                print(f'key2 = {e} {f}\n'
                                      f'       {g} {h}\n')

