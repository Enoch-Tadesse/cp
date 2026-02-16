#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    string num;
    cin >> num;
    int nonzeros = 0;
    int r = num.size() - 1;
    int zeros = 0;
    while (num[r] == '0') {
        zeros += 1;
        r -= 1;
    }
    int counter = 0;

    int l = 0;
    while (l < r) {
        counter += int(num[l] != '0');
        l += 1;
    }
    cout << counter + zeros << "\n";
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
