class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        max_area = 0
        
        while left < right:
            new_height = min(height[left], height[right])
            width = right - left
            curr_area = (new_height * width)
            
            if curr_area > max_area:
                max_area = curr_area
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        
        return max_area
        
        
        
