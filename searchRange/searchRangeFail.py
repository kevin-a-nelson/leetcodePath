

class Solution():

    def searchRange(self, nums, target, currentIdx=0, operator="plus"):

        if len(nums) == 2:
            if nums[0] == target:
                if operator == "plus":
                    return currentIdx + 1
                if operator == "minus":
                    return currentIdx - 2
            if nums[1] == target:
                if operator == "plus":
                    return currentIdx + 2
                if operator == "minus":
                    return currentIdx

        mid = len(nums) // 2

        if operator == "plus":
            currentIdx += mid
        if operator == "minus":
            currentIdx -= mid

        if nums[mid] == target:
            return currentIdx

        if nums[mid] > target:
            self.searchRange(nums[mid + 1:], target, currentIdx, "plus")
        if nums[mid] < target:
            self.searchRange(nums[:mid], target, currentIdx, "minus")

    def search(self, nums, target):
        return self.searchRange(nums, target)
