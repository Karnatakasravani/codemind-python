#User function Template for python3

class Solution:
    
    def nPr(self, n, r):
        import math
        # code here
        s=math.factorial(n)
        r=math.factorial(n-r)
        res=s//r
        return res
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends
