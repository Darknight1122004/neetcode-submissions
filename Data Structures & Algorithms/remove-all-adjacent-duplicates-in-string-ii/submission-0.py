class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for char in s:
            if stack and stack[-1][0]==char:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([char,1])
        res=""
        for k in stack:
            res+=(k[0]*k[1])
        return res                    