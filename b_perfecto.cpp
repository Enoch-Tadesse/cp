#include <bits/stdc++.h>
#include <cmath>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

typedef long long ll;

bool isPerfect(long long num) {
    ll s = sqrt(num);
    return s * s == num;
}

void solve() {
    int n;
    cin >> n;
    long long total = (1LL * n * (n + 1)) / 2;

    if (n == 1 || isPerfect(total)) {
        cout << -1 << endl;
        return;
    }

    long long pre = 0;
    int i = 1;
    while (i < n + 1) {
        pre += i;
        if (isPerfect(pre)) {
            cout << i + 1 << " " << i << " ";
            pre += i + 1;
            i += 2;
        } else {
            cout << i << " ";
            i += 1;
        }
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
