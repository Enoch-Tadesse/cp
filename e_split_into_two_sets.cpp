#include <bits/stdc++.h>

#include <unordered_map>
#include <vector>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

#define forsn(i, s, n) for (int i = s; i < int(n); i++)

ll counter(ll i, vector<vector<ll>> &adj, vector<bool> &seen) {
    seen[i] = true;
    for (auto ele : adj[i]) {
        if (!seen[ele]) {
            return counter(ele, adj, seen) + 1;
        }
    }
    return 1;
}

void solve() {
    ll n;
    cin >> n;
    vector<vector<ll>> adj(n + 1);
    bool can = true;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        if (a == b) {
            can = false;
        }
        adj[a].push_back(b);
        adj[b].push_back(a);
        if (adj[a].size() > 2 || adj[b].size() > 2) can = false;
    }
    if (!can) {
        cout << "NO" << endl;
        return;
    }
    vector<bool> seen(n + 1, false);
    for (int i = 1; i < n + 1; i++) {
        if (!seen[i]) {
            if (counter(i, adj, seen) % 2) {
                cout << "NO" << endl;
                return;
            }
        }
    }
    cout << "YES" << endl;
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
