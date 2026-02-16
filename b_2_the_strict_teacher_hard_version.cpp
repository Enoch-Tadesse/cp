#include <bits/stdc++.h>

#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;

ll bisect_right(vector<ll>& nums, ll target) {
    ll l = 0;
    ll r = nums.size() - 1;
    while (l <= r) {
        ll mid = l + (r - l) / 2;
        if (nums[mid] <= target)
            l = mid + 1;
        else
            r = mid - 1;
    }
    return l;
}
ll bisect_left(vector<ll>& nums, ll target) {
    ll l = 0;
    ll r = nums.size() - 1;
    while (l <= r) {
        ll mid = l + (r - l) / 2;
        if (nums[mid] >= target)
            r = mid - 1;
        else
            l = mid + 1;
    }
    return l;
}

void solve() {
    ll n, m, s;
    cin >> n >> m >> s;
    vector<ll> teach(m);
    for (auto& x : teach) {
        cin >> x;
    }
    vector<ll> studs(s);

    for (auto& x : studs) {
        cin >> x;
    }
    sort(teach.begin(), teach.end());
    for (int i = 0; i < s; i++) {
        ll x = studs[i];
        ll right = bisect_right(teach, x);
        if (right == m) {
            cout << n - teach[m - 1] << endl;
            continue;
        }
        if (right == 0) {
            cout << teach[right] - 1 << endl;
            continue;
        }
        ll rnum = teach[right];
        cout << (rnum - teach[right - 1]) / 2 << endl;
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
