#include <bits/stdc++.h>
#include <cmath>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
	return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
	ll a , b;
	cin >> a >> b;
	ll dif = (abs(a - b));
	ll out = dif / 10;
	cout << out + int(dif % 10 != 0) << "\n";
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
