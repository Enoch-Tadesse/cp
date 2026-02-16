#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int d, u, l;
    cin >> d >> u >> l;
    for (int i = 0; i < d; i++) {
        cout << i;
    }
    for (int i = 0; i < u; i++) {
        cout << char(65 + i);
    }
    for (int i = 0; i < l; i++) {
        cout << char(97 + i);
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
