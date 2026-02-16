#include <bits/stdc++.h>
#include <numeric>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n, k, x;
    cin >> n >> k >> x;
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    int total = 0;
    accumulate(nums.begin(), nums.end(), total);
    for
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
