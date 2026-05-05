class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        A naive implementation would go something like

        for each element in list
            loop through list
                if index == element return true
        return false

        This is inefficient because we're revisiting the same element over and over again

        Instead:

        for each element in the list
            if list[element] exists: return true
            else list[element] = element
        return false
        """

        visited_nums_set = set()
        for num in nums:
            if num in visited_nums_set: return True
            visited_nums_set.add(num)
        return False

        