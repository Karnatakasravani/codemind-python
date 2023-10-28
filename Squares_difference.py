#User function Template for python3
class Solution:
    def squaresDiff (self, N):
        # code here 
        a = int((N*(N+1)*(2*N+1))/6)
        b = int((N*(N+1))/2)
        c = a - (b**2)
        d = abs(c)
        return d


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.squaresDiff(N))
# } Driver Code Ends
