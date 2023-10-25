#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (self, n):
        # code here 
        s = 0
        temp = n
        while temp > 0 :
            rem = temp % 10
            s +=(rem**3)
            temp = temp // 10
            
        return "Yes" if s == n else "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
