def CountSort(array):
    res=[0 for _ in  range(10)]
    ans=[]
    n=len(array)
    for i in range(n):
        res[array[i]]+=1
    for i in range(len(res)):
         while res[i]>0:
             ans.append(i)
             res[i]-=1
    return ans
if __name__ == '__main__':
    array=list(map(int,input().split()))
    print(*CountSort(array))
"""
Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.

Example Input

Input 1:
A = [1, 3, 1]
Input 2:
A = [4, 2, 1, 3]
"""

