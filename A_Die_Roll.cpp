#include <bits/stdc++.h>
#include <numeric>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int y, w;
    cin >> y >> w;
    int prob = (6 - max(y, w) + 1);
    if (prob == 0) {
        cout << "0/1\n";
    }
    int great = gcd(prob, 6);
    cout << prob / great << "/" << 6 / great << "\n";
}
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
