class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for p,s in zip(position,speed):
            t=(target-p)/s
            time.append([p,t])
        time.sort()
        fleet=0
        fleet_time=0

        for i in range(len(time)-1,-1,-1):
            curr=time[i][1]
            if (curr>fleet_time):
                fleet+=1
                fleet_time=curr
            
        return fleet

        