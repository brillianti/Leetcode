'''
#要求:
# 给定一个整数数组 nums 和一个目标值 target
# 请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''

nums = [2, 7, 11, 15]
target = 9

def twoSum(nums,target):
	n = len(nums) # 获取nums的长度，是4
	for x in range(n): # 外层循环先取出下标0，对应着数组里的第一个数字
		for y in range(x+1,n): # 内层循环取出下标1，对应着数组里的第二个数字
			if nums[x] + nums[y] == target: # 如果第一个数字+第二个数字=target
				return x,y # 上面的判断是对的话，那么就返回下标
				break       # 并停止程序
			else: # 如果上面的条件不满足的话，内层for循环就会继续取出下标2进行判断...如果都不满足，那么外层for循环就会取出下标1...依次类推
				continue

if __name__ == '__main__':
	a = twoSum(nums, target)
	print(a)
