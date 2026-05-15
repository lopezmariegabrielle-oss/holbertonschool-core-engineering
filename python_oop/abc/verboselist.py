#!/usr/bin/env python3
"""Module définissant une liste bavarde (VerboseList)."""


class VerboseList(list):
    """Une classe de liste qui notifie lors des modifications."""

    def append(self, item):
        """Ajoute un élément et imprime une notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def pop(self, index=-1):
        """Affiche un message avant de retirer l'élément."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

    def extend(self, items):
        """Ajoute plusieurs éléments et affiche le compte."""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Affiche un message avant de supprimer l'élément."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)
