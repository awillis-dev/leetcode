# description
* return true if the input array contains any duplicate elements
* " false if each element is unique
​
# test case
```
given: nums = [3, 5, 7, 9, 9]
output: True
```
​
# brute force
* use a nested for loop to check each element in array and compare with neighbor
* if any elements equal the same value then return True
### complexity
* O(N^2)
​
# optimized solution
​
* initialize a set
* iterate through array
* check if current element is in set
* if yes, item is a duplicate => return True
* add current element to the set
* continue until end of array
* return false if at the end of the array, no duplicates have been found
​
# 1-2 sentence approach
​
# walk through with trace table