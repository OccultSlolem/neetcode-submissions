class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = set()
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            if compliment in visited:
                return [nums.index(compliment), i]
            visited.add(num)
        return []
        