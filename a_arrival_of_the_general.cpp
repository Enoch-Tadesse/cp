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
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    int max_idx = 0;
    for (int i = 1; i < n; i++) {
        if (nums[i] > nums[max_idx]) {
            max_idx = i;
        }
    }
    int min_idx = n - 1;
    for (int i = n - 2; i >= 0; i--) {
        if (nums[i] < nums[min_idx]) min_idx = i;
    }
    if (min_idx == max_idx)
        cout << 0 << "\n";
    else
        cout << max_idx + n - 1 - min_idx - 1 * int(min_idx < max_idx) << "\n";
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
