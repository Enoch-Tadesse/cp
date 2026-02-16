#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n;
    cin >> n;

    string a;
    cin >> a;

    string b;
    cin >> b;

    int count1 = 0, count2 = 0;

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            count1 += int(a[i] == '0');
            count2 += int(b[i] == '0');
        } else {
            count2 += int(a[i] == '0');
            count1 += int(b[i] == '0');
        }
    }
    // cout << count1 << " " << count2 << " " << n << endl;
    // if (2 * count1 >= n && 2 * count2 >= n) {

    if (count1 >= (n + 1) / 2 && count2 >= n / 2)
        std::cout << "YES\n";
    else {
        std::cout << "NO\n";
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
