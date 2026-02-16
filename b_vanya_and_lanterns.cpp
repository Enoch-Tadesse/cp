#include <bits/stdc++.h>

#include <algorithm>
#include <cmath>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

bool can(vector<int> nums, double mid, int k) {
    if (mid < nums[0]) return false;
    if (mid < k - nums[nums.size() - 1]) return false;

    for (int i = 0; i < nums.size() - 1; i++) {
        if (mid < double(nums[i + 1] - nums[i]) / 2) return false;
    }
    return true;
}

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }

    sort(nums.begin(), nums.end());

    double l = 0.0;
    double r = double(k);

    double delta = pow(10, -9);

    while (l <= r) {
        double mid = l + (r - l) / 2;
        if (can(nums, mid, k)) {
            r = mid - delta;
        } else {
            l = mid + delta;
        }
    }
    cout << l << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
