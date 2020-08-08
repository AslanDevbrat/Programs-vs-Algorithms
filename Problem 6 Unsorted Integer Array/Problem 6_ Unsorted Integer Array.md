# Explaination
This algorithm make two assumption: 

 - Minimun number in the input list is -float('inf')
 - Maximum number in the input_list is float('inf')

Initialize max to 1 and min to 999999999 Now traverse the whole arr and keep comparing the corresponding element with min and Max:
if the element is greater than max the update the max to that element.
Similarly if the element is smaller than min then update the min to that element.
## Time complexity:
**O(n)** because single traversal

## Space Complexity:
**O(n)**

