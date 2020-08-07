# Explanation

This Solution uses a modified Binary search to find the index of a target number in a Sorted But Rotated Array.

 1. Find the middle index = (start+end)//2
 2. If the start > end that means the element doesn't exists in the array.
 3. If the target is present on the middle index then return that index.
 4. If the arr[start:mid] is sorted
		 1. If the target is lyining between arr[start] and arr[mid], then we recurse 				on on the arr[start:mid-1]
		 2. else recurse on the arr[mid+1,stop]
 5. Else arr[start:mid] is not sorted (i.e. arr[mid+1,stop] is sorted because the given array is sorted but rotated):
		 1. if the target is lying between arr[mid+1] and arr[end] , the we recurse on the arr[mid+1,stop]
		 2. else recurse on the arr[start,mid-1]

## Time complexity
Since every time the search range is reduced to half. Therefore the time complexity is **O(log(n))**

## Space complexity
Since its an in-place search Therefore **O(1)**

