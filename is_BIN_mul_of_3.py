#User function Template for python3
class Solution:
	def isDivisible(self, s):
		# code here
		d=int(s,2)
		if d%3==0:
		    return 1
		else:
		    return 0

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)

# } Driver Code Ends
