#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n, x;
    cin >> n >> x;
    int counter = 0;
    for (int i = 0; i < n; i++) {
        if (i == x)
            continue;
        cout << i << " ";
        counter += 1;
    }
    if (counter < n)
        cout << x << "\n";
    else
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
