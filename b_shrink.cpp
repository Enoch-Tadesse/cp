#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
	return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
	int n;
	cin >> n;
	cout << "1 ";
	for (int i = n; i > 2; i--){
		cout << i << " ";
	}
	cout << 2 << endl;
}
int main(){

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t = 1;
	cin >> t;
	while(t--){
		solve();
	}
}
