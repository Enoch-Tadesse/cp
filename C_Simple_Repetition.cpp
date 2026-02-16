#include <bits/stdc++.h>
#include <cmath>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n, k;
    cin >> n >> k;
    if (k > 1) {
        if (k == 2 && n == 1) {
            cout << "YES\n";
            return;
        }
        cout << "NO\n";
        return;
    }
    if (n == 1) {
        cout << "NO\n";
        return;
    }
    if (n == 2) {
        cout << "YES\n";
        return;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
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
