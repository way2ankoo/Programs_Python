'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.'''
from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        # mid = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return left


if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 7
    sol = Solution()
    print(sol.search_insert(nums, target))
