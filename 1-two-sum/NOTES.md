# 1. Understand problem
- given an array and a target value, return the indices of the 2 values that add up to target
​
## happy case example
```
input: nums= [2, 4, 6, 8, 10] ; target= 16
output: (2, 4)
```
​
# 2. Explore possible solutions
​
## a) brute force
* use double nested for loop to add current element and next element then see if the sum equals the given target
​
## b) optimized solution?
- initialize a dictionary where `{ val: idx }`
- iterate through array
- initialize a `difference` variable that is the given `target - current element`
- check if `difference` exists in the dictionary
-  if yes, return (dict[difference], current elements index)
-  if not, set dictionary key to arrays current value and have it point to its' index
​
###  time and space complexity
a) time: O(N^2)
space: O(1)
b) time: O(N)
space: O(N)
​
​
​