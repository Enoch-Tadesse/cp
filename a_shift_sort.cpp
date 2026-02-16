#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
	return *max_element(nums.begin(), nums.end());
}
typedef long long ll;
#define forsn(i, s, n) for (int i = s; i < int(n); i++)



void solve(){
	int n;
	cin >> n;
	string bits;
	cin >> bits;
	int cnt = 0;
	int zero = 0;
	for (auto b: bits) cnt += b == '1';
	for (int i = n - cnt; i < n; i++) zero += bits[i] == '0';
	cout << zero << endl;

}
int main(){

	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t = 1;
	cin >> t;
	forsn(i, 0, t){
		solve();
	}
}
