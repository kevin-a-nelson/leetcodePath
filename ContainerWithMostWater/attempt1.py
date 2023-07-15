

class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        maxArea = float('-inf')

        while left < right:

            containerHeight = min(height[left], height[right])
            containerWidth = abs(left - right) 

            area = containerHeight * containerWidth
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea


solution = Solution().maxArea([2,3,4,5,18,17,6])

print(solution)