class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_appearances = {}
        for num in nums:
            if num not in num_appearances: num_appearances[num] = 0
            num_appearances[num] += 1
        
        sorted_appearances = sorted(num_appearances, key=num_appearances.get, reverse=True)
        top_k_frequent = []
        for i in range(k):
            top_k_frequent.append(sorted_appearances[i])
        return top_k_frequent
        