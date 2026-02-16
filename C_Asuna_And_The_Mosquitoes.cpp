#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

using ll = long long;

void solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    ll odds = 0;
    ll total = 0;
    for (int num : nums) {
        odds += num & 1;
        total += num;
    }
    if (odds == n || odds == 0) {
        cout << getMax(nums) << "\n";
        return;
    }
    cout << total - odds + 1 << "\n";
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
