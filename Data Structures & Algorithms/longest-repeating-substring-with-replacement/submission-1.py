class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        l=[0]*26
        longest=0
        for j in range(len(s)):
            l[ord(s[j])-65]+=1
            while(j-i+1)-max(l)>k:
                l[ord(s[i])-65]-=1
                i+=1
            longest=max(longest,j-i+1)
        return longest
        
        