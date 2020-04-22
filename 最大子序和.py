# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组
#（子数组最少包含一个元素），返回其最大和。
# 因为是连续子序列和，所以每次从当前数出发，考察到该位置的最大和，
# 该位置的数要么参与了和，要么就是它本身，
# 如果当前数 + 前一个数能使得当前数的处境更好，则相加，否则不作为

class Solution:
    def maxSubArray(self, nums):
        if not nums:return
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] > nums[i]:
                nums[i] += nums[i - 1]
        return max(nums)

if __name__ == '__main__':
    So = Solution()
    num = So.maxSubArray([1,2,3,4,-5,3,-7])
    print(num)
