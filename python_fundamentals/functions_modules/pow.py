#!/usr/bin/env python3
def pow(a, b):
    exp = abs(b)

    resultat = 1
    for i in range(exp):
        resultat = resultat * a
    if b < 0:
        return 1 / resultat

    return resultat
