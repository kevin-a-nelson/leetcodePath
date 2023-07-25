

class Solution():

    def permute(self, nums):

        DP = [[] for _ in range(len(nums))]

        for num in nums:
            DP[0].append([num])

        for i in range(1, len(nums)):
            for num in nums:
                for permutation in DP[i - 1]:
                    # print(permutation)
                    if num in permutation:
                        continue

                    DP[i].append(permutation + [num])

        return DP[-1]


solution = Solution().permute([1, 2, 3])

print(solution)
