#假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#注意：给定 n 是一个正整数。
#力扣:https://leetcode-cn.com/problemset/all/
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        global res   #添加全局变量
        if  n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            i = 1
            j = 2
            res = 0
            for k in range(2,n):
                res = i + j
                i = j
                j = res
            return res

if __name__ == '__main__':
    a = climbStairs(5)   #括号内的数字可以随便取
    print(a)
