#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
    int n;
    cin >> n;

    vector<ll> nums(n);
    for (ll &num : nums) cin >> num;
	for (int i =0; i < n - 1; i++) {
		if (nums[i] > nums[i + 1]){
			cout << nums[i] / nums[i + 1] << endl;
			return;
		}
	}
	cout << 1 << endl;


}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
}
