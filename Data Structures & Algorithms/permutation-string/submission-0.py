class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        n=len(s2)
        l1=[0]*26
        l2=[0]*26
        if(k>n):
            return False
        for i in range(k):
            l1[ord(s1[i])-ord('a')]+=1
            l2[ord(s2[i])-ord('a')]+=1
        if(l1==l2):
            return True
        for i in range(k,n):
            l2[ord(s2[i])-ord('a')]+=1
            l2[ord(s2[i-k])-ord('a')]-=1
            if(l1==l2):
                return True
        return False
        