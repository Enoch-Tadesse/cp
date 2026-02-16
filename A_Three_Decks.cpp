#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n, k, q;
    cin >> n >> k >> q;
    int poss = (n + k + q) / 3;
    if (poss * 3 == (n + k + q)) {
        if (poss < n || poss < k) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
        }
    } else {
        cout << "NO\n";
    }
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
