#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

ll calculate(ll k, ll A, ll B, ll a, ll b) {
    if (A > k && B > k) return 0;

    ll ans = 0;

    if (A <= k) {
        ll maxA = (k - A) / a + 1;
        ans += maxA;
        k -= maxA * a;
    }
    if (B <= k) {
        ll maxB = (k - B) / b + 1;
        ans += maxB;
    }

    return ans;
}

void solve() {
    ll k, A, B, a, b;
    cin >> k >> A >> B >> a >> b;
    ll ans = 0;
    if (a < b) {
        cout << calculate(k, A, B, a, b) << endl;
    } else {
        cout << calculate(k, B, A, b, a) << endl;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
}
