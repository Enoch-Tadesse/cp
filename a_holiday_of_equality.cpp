#include <bits/stdc++.h>
#include <cmath>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
	return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
	int n;
	cin >> n;
	vector<int> nums(n);
	for (int &x : nums){
		cin >> x;
	}
	int maxNum = *max_element(nums.begin(), nums.end());
	int counter = 0;
	for (int num: nums){
		counter += (maxNum - num);
	}
	cout << counter << endl;
}
int main(){

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t = 1;
	
	while(t--){
		solve();
	}
}
