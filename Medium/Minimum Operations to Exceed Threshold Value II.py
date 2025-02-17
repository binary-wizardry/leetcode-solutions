class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)
        count = 0
        while True:
            n1 = heapq.heappop(heap)
            if n1 >= k:
                break
            n2 = heapq.heappop(heap)
            new = n1 * 2 + n2
            heapq.heappush(heap, new)
            count += 1
        return count

# priority queue
