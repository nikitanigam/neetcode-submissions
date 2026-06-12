class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        answer=[0]*n
        for i in range(n):
            j=i+1
            while(j<n):
                if(temperatures[i]<temperatures[j]):
                    answer[i]=j-i
                    break
                j+=1
        return answer
        