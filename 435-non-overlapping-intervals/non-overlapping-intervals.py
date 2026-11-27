class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        prev_end=intervals[0][1]
        count=0
        for start,end in intervals[1:]:
            if start<prev_end:
                count+=1
            else:
                prev_end=end
        return count