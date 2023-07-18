

class Solution():

    def binarySearch(self, nums, target):

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        return -1

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        leftSearch = self.binarySearch(nums[:left], target)

        if leftSearch != -1:
            return leftSearch
        
        rigthSearch = self.binarySearch(nums[left:], target)

        if rigthSearch != -1:
            return rigthSearch + left
        
        return -1

nums = [1,3]

solution = Solution().search(nums, 3)

print(solution)