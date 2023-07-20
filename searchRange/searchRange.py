class Solution():

    def searchRange(self, nums, target):

        firstTargetIndex = self.getFirstTargetIndex(nums, target)
        lastTargetIndex = self.getLastTargetIndex(nums, target)

        return [firstTargetIndex, lastTargetIndex]

    def getFirstTargetIndex(self, nums, target):

        index = -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) / 2

            if nums[mid] == target:
                index = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return index

    def getLastTargetIndex(self, nums, target):

        index = -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) / 2

            if nums[mid] == target:
                index = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return index
