class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for x in nums:
            pos = bisect.bisect_left(tail, x) # find the position "pos" so that tail[i] < x for all i < pos
            tail[pos:pos+1] = [x]             # if tail[pos] exists, update it to be x, otherwise append x
        return len(tail)
