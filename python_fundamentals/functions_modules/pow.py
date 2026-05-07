#!/usr/bin/env python3
def pow(a, b):
    if b < 0:
        return None
    resultat = 1
    for i in range(b):
        resultat = resultat * a
    return resultat
