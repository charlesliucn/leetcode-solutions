class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
		int sum = 0;
		myquicksort(nums,0,nums.size()-1);
		for (int i = 0;i<nums.size();i = i+2)
			sum += nums[i];
		return sum;

    }
	/*void InsertSort2(vector<int>& nums){ // two slow for being accepted
		for(int i = 1;i < nums.size();++i){
			for(int j = i;j > 0;--j){
				if(nums[j] < nums[j - 1]){
					int temp = nums[j];
					nums[j] = nums[j-1];
					nums[j-1] = temp;
				}
			}
		}
	}*/
	void myquicksort(vector<int>& vec, int low, int high){
		if (low < high){
			int l = low;
			int r = high;
			int key = vec[l];

			while (l < r){
				while (l < r&&key <= vec[r])
					--r;
				vec[l] = vec[r];
				while (l < r&&key >= vec[l])
					++l;
				vec[r] = vec[l];
			}
			vec[l] = key;

			myquicksort(vec, low, l-1);
			myquicksort(vec, r + 1, high);
		}
	}
};