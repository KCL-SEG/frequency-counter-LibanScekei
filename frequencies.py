"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
   frequencies = {}
   for key in items:
    values = str(items)
    total = values.count(str(key))
    frequencies.update({str(key) : total})
   return frequencies
