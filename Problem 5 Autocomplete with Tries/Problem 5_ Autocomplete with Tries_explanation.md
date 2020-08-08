# Explaination

Uses a dictionary to store the letters of words. Lookups and insertions should be faster than a BST.

## Big O Space Complexity

The suffixes function determines the overall runtime which is best described as O(n x m) where n is the 
number of inputs and m is the length of the average input. The number of characters in an individual
input has an impact on runtime in this scenario.

## Big O Time Complexity

Looking up words as well as inserting and finding a word runs in O(n) where n is the length of the search string.
