#User function Template for python3

class Solution:
	def distance(self, x1, y1, x2, y2):
		# Code here
		import math
		dis=math.sqrt(((x1-x2)*(x1-x2))+((y2-y1)*(y2-y1)))
		return round(dis)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x1, y1, x2, y2 = input().split()
		x1 = int(x1);
		y1 = int(y1);
		x2 = int(x2);
		y2 = int(y2);
		ob = Solution();
		ans = ob.distance(x1, y1, x2, y2)
		print(ans)
# } Driver Code Ends
