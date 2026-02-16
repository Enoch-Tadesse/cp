#include <algorithm>
#include <bits/stdc++.h>
#include <numeric>
#include <vector>

using namespace std;

template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

bool valid(int guess, int n, vector<int> &nums) {
    int total = accumulate(nums.begin(), nums.end(), 0);
    int loops = guess / 3;
    int curr = loops * total;
    int diff = guess % 3; // how many days remain
    curr += accumulate(nums.begin(), nums.begin() + diff, 0);
    return curr >= n; // return True if the curr walked is greater than n
}

void solve() {
    int n;
    cin >> n;
    vector<int> nums(3);
    for (int &x : nums) {
        cin >> x;
    }
    if (getMax(nums) > n) {
        cout << 1 << "\n";
        return;
    }

    int l = 1, r = pow(10, 9) + 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (valid(mid, n, nums))
            r = mid - 1;
        else
            l = mid + 1;
    }
    cout << l << "\n";
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
