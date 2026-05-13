#!/usr/bin/env python3
raise_exception_msg = __import__('raise_exception_msg').raise_exception_msg

try:
    # On appelle ta fonction avec un message spécifique
    raise_exception_msg("C'est un message de test !")
except NameError as ne:
    # On attrape l'erreur et on affiche le message qu'elle contient
    print(ne)
    