class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        n=len(s)
        i=0
        j=0
        r=set()
        for j in range (n):
            while(s[j] in r):
                r.remove(s[i])
                i+=1
            r.add(s[j])
            longest=max(longest,j-i+1)
        return longest
        