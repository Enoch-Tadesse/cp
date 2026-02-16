#include <bits/stdc++.h>

#include <algorithm>
#include <cmath>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
void solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    sort(nums.rbegin(), nums.rend());
    long double ans = 0.0;
    for (int i = 0; i < n; i++) {
        int val = nums[i];
        if (i & 1) {
            ans -= val * val;
        } else {
            ans += val * val;
        }
    }
    cout << ans * M_PI  << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
