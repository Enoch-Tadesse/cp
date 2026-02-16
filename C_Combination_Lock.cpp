#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n;
    cin >> n;
    if (!(n % 2)) {
        cout << -1 << "\n";
        return;
    }
    for (int i = 0; i < n; i++) {
        if (2 * i + 1 == n) {
            cout << n << " ";
            continue;
        }
        cout << (2 * i + 1) % n << " ";
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
