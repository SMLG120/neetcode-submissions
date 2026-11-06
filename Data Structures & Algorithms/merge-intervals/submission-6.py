class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # sort start time
        intervals.sort(key=lambda interval: interval[0])
        result = [intervals[0]]
        # get lastEnd and compare to start of cur interval:
        for start, end in intervals[1:]:
            lastMerged = result[-1]
            lastEnd = lastMerged[1]
            if start <= lastEnd:
                lastMerged[1] = max(lastMerged[1], end)
            else:
                result.append([start, end])
        return result
        