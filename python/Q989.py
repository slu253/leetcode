class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        cat = ''.join(str(i) for i in A)
        num = int(cat)+K
        result = [s for s in str(num)]
        
        return result

