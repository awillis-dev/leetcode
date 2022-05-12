- set a pointer at beg & end of array
- set max area variable to 0
​
- loop through array while p1 < p2:
- find the new height by finding the minimum value between the 2 pointers
- find the width by calculating the diff between p2 & p1
- calc curr area by multiplying new height & width
- set max area to maximum number between curr area and max area
​
- if p1 < = p2:
- p1 increments
-else:
- p2 decrements
​
return max area