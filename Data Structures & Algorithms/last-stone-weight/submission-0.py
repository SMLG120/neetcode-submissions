class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest1 = heapq.heappop(max_heap)
            largest2 = heapq.heappop(max_heap)
            # if x == y, destroy both
            if largest1 == largest2:
                continue
            # destroy x, then y = y - x
            if largest1 < largest2:
                heapq.heappush(max_heap, largest1 - largest2)
            
        return -max_heap[0] if max_heap else 0