class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        arrows=1
        last_end=points[0][1]
        for start,end in points[1:]:
            if start>last_end:
                arrows+=1
                last_end=end
        return arrows