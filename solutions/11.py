class Solution:
    def maxArea(self, height: List[int]) -> int:    
        left =0
        right = len(height)-1
        area = 0
        AREA = 0
        while left < right:
            area = abs((right-left)*(min(height[right],height[left])))
            if area > AREA:
                AREA = area
            if height[left] < height[right]:
                left = left+1
            elif height[left] > height[right]:
                right = right -1  
            else:
                left = left+1
                right = right -1
        
        return AREA 