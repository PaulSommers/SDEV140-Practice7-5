"""
Author: Paul Sommers
Date written: 11/18/2024
Assignment: Exercise 7-5 - Recursive Function Test
Short Desc: This program tests a recursive function that prints the elements of a sequence. 
            It traces the argument on each recursive call and demonstrates the hidden costs of recursion.
"""

# Recursive function to print all elements in a sequence
def printAll(seq):
    if seq:
        # Trace the current sequence and print the first element
        print(seq, "->", seq[0])
        # Recursive call with the rest of the sequence (sliced from index 1)
        printAll(seq[1:])

# Test the function
printAll([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])