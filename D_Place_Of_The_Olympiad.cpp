#include <bits/stdc++.h>
#include <cmath>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

bool can(long long guess, long long c, long long r, long long k) {
    long long bench = c / (guess + 1);
    long long rem = c % (guess + 1);
    return ((bench * guess + rem) * r) >= k;
}

void solve() {
    long long r, c, k;
    cin >> r >> c >> k;
    long long left = 1;
    long long right = c;
    while (left <= right) {
        long long guess = left + (right - left) / 2;
        if (can(guess, c, r, k)) {
            right = guess - 1;
            ;
        } else {
            left = guess + 1;
        }
    }
    cout << left << endl;
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
