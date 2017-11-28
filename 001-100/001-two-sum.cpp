// Only the solution part is shown
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> a;
		for(int i = 0;i < nums.size();i++){
			for (int j = i+1; j < nums.size(); j++){
				if(nums[i] + nums[j] == target){
					a.insert(a.begin(), i);
					a.insert(a.begin()+1,j);
				}
			}
		}
		return a;
    }
};
