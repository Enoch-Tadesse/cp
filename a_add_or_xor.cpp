#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
	return *max_element(nums.begin(), nums.end());
}
typedef long long ll;



void solve(){
	int a, b , x, y;
	cin >> a >> b >> x >> y;
	if (b == a) {
		cout << "0\n";
		return;
	}
	if (b < a){
		if ((a ^ 1) == b){
			cout << y << endl;
		}else{
			cout << -1 << endl;
		}
		return;
	}
	int counter = 0;
	while (a != b) {
		int n = a ^ 1;
		if (n <= a){
			counter += x;
			a += 1;
		}else{
			if ((n - a) * x < y){
				counter += (n - a) * x;
			}else{
				counter += y;
			}
			a = n;
		}
	}
	cout << counter << endl;
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
