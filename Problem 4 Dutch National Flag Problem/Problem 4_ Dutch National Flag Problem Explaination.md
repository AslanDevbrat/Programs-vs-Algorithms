# Explaination

The idis is to place all 0's and 2's at their right position, which will automatically place all 1's in there right position. For that I have taken two variable named 'index_of_0' and 'index_of_2' which will keep track of the next index to be filled for 0 and 2 respectively. Then the fuction will traverse the whole arr (in worst case) and swaps the number according to the need.

## Time Complexity
Since the function traverse only the input_list once therefore **O(n)**

## Space Complexity
Since it is a inplace sorting it require **O(n)**  
