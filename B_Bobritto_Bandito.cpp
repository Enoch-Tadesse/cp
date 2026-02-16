#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n, m, l, r;
    cin >> n >> m >> l >> r;
    int left = max(l, 0 - m);
    int right = min(r, m - abs(left));
    cout << left << " " << right << "\n";
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
