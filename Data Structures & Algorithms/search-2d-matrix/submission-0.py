class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while(l<=r):
            mid=int((l+r)/2)
            if target in matrix[mid]:
                return True
            elif(target<matrix[mid][0]):
                r=mid-1
            else:
                l=mid+1
        return False

        