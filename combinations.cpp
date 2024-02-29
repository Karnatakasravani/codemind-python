#include<bits/stdc++.h>
using namespace std;
void Maya(vector<int>nums,int index,vector<int>ans,int size,int target,int mysum)
{
	if(index>=size || mysum==target)
	{
		if(index>=size or mysum!=target)
		{
		return ;	
		}
	    
	    else 
	    {
		for(int i=0;i<ans.size();i++){
			cout<<ans[i]<<" ";
	    }cout<<endl;
	
		}
		
	}
	else if(mysum>target)
	{
		return ;
	}
	else{
	ans.push_back(nums[index]);
	Maya(nums,index,ans,size,target,mysum+nums[index]);
	ans.pop_back();
	Maya(nums,index+1,ans,size,target,mysum);
	}
	
}
int main()
{
	vector<int>nums;
	int n,x;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>x;
		nums.push_back(x);
	}
	int target;
	cin>>target;
	sort(nums.begin(),nums.end());
	vector<int>ans;
	Maya(nums,0,ans,n,target,0);
//	return 
}
