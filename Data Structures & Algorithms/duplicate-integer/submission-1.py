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

        visited_set = {}
        for each element in the list
            if visited[element] exists: return true
            else add element to visited_set
        return false
        """

        visited_nums_set = set()
        for num in nums:
            if num in visited_nums_set: return True
            visited_nums_set.add(num)
        return False

        