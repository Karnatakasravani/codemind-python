#User function Template for python3

class Solution:
	def find_median(self, v):
		
        p=sorted(v)
        size = len(p)
        if size%2 != 0:
            n = int((size+1)/2)
            return p[n-1]
        else:
            n1 = int(size/2 -1)
            n2 = n1 + 1
            av = (p[n1]+p[n2])/2
            av1 = int(av)
            return av1
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends
