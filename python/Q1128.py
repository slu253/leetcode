
class Solution:
    def numEquivDominoPairs(self, dominoes):
        ans = 0
        d = dict()
        for d1, d2 in dominoes:
            # 排序后加入字典
            print(d1)
            print(d2)
            index = tuple(sorted((d1, d2)))
            if index in d:
                d[index] += 1
            else:
                d[index] = 1
        # 计算答案
        for i in d:
            ans += d[i] * (d[i] - 1) // 2
        return ans

#链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/pai-xu-ha-xi-zi-dian-python3-by-smoon1989/
