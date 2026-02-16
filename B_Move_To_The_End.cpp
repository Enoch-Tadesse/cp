#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n;
    cin >> n;
    vector<long long> nums(n);
    for (long long &x : nums) {
        cin >> x;
    }
    vector<long long> _maxs(n);
    long long curr = 0;
    for (int i = 0; i < n; i++) {
        curr = max(curr, nums[i]);
        _maxs[i] = curr;
    }
    long long _sum = 0;
    for (int i = n - 1; i > -1; i--) {
        cout << _maxs[i] + _sum << " ";
        _sum += nums[i];
    }
    cout << "\n";
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
