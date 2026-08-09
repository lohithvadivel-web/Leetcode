class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            # Find the farthest index we can reach
            farthest = max(farthest, i + nums[i])

            # We have reached the end of the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
