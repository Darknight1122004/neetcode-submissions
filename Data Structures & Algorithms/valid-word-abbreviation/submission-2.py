class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i=0
        j=0
        m=len(word)
        n=len(abbr)
        while i<m and j<n:
              if abbr[j].isdigit(): 
                if abbr[j]=="0":
                    return False
                nums=0    
                while j<n and abbr[j].isdigit():
                    nums=nums*10+int(abbr[j])
                    j+=1
                i+=nums
              else :
                if word[i]!=abbr[j]:
                    return False
                i+=1
                j+=1
        return i==m and j==n                

        