#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
	return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
	ll n;
	cin >> n;
	while (n > 1){
		if (n & 1){
			cout << "YES\n";
			return;
		}
		n = n >> 1;
	}
	cout << "NO\n";
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
