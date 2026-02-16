#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    sort(nums.begin(), nums.begin() + n);
    cout << nums[n - 1] - nums[0] << "\n";
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
