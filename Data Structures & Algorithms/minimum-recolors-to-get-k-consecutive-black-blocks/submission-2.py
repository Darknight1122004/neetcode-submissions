class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=blocks[:k].count('W')
        res=l
        for i in range(k,len(blocks)):
            if blocks[i]=='W':
                l+=1
            if blocks[i-k]=='W':
                l-=1
            res=min(l,res) 
        return res           
        