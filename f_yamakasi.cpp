#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
    ll n, s, x;
    cin >> n >> s >> x;
    vector<ll> pre(n + 1, 0);
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        pre[i + 1] = pre[i] + arr[i];
    }
    ll ans = 0;
    map<ll, int> freq;
    int l = 1;
    for (int r = 1; r <= n; r++) {
        if (arr[r - 1] > x) {
            l = r + 1;
            freq.clear();
        } else if (arr[r - 1] == x) {
            while (l <= r) {
                freq[pre[l - 1]]++;
                l += 1;
            }
        }
        ans += freq[pre[r] - s];
    }
    cout << ans << "\n";
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
