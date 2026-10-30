class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        target=[0]*(len(triangle)+1)
        for i in triangle[::-1]:
            for j,k in enumerate(i):
                target[j]=k+min(target[j],target[j+1])
        return target[0]        
        