# reference: https://blog.csdn.net/milk_paramecium/article/details/113251513

class UnionFindSet():
    def __init__(self,n):
        self.setSize = n  #不连通区域
        self.father = {}

    def add(self,x):  #添加根节点
        if x not in self.father:
            self.father[x] = -1
            #self.setSize += 1

    def find(self,x):
        root = x
        while self.father[root] != -1:  #找根节点
            root = self.father[root]

        while (x != root): #路径压缩
            o = self.father[x]  #找x的父节点
            self.father[x] = root  #把x的父节点设置成刚才找到的根
            x = o  #往上一层

        return root

    def merge(self,x, y):
        self.add(x)
        self.add(y)
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        else:
            self.father[root_x] = root_y  #合并
            self.setSize -= 1
            return True
            
    def is_Union(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_a, uf_b = UnionFindSet(n), UnionFindSet(n)
        ans = 0

        for t, i, j in edges:
            if t == 3:
                if not uf_a.merge(i, j):
                    ans += 1
                else:
                    uf_b.merge(i, j)
        for t, i, j in edges:
            if t == 1:
                if not uf_a.merge(i, j):
                    ans += 1
            elif t == 2:
                if not uf_b.merge(i, j):
                    ans += 1
        if uf_a.setSize != 1 or uf_b.setSize != 1:
            return - 1
        else:
            return ans