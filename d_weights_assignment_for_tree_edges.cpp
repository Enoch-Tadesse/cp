#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    vector<int> perm(n);
    for (int &x : perm) {
        cin >> x;
    }
    if (nums[perm[0] - 1] != perm[0]) {
        cout << -1 << endl;
        return;
    }
    vector<int> dist(n, -1);
	vector<int> ans(n, -1);
    dist[perm[0] - 1] = 0;
	ans[perm[0] - 1] = 0;
    for (int i = 1; i < n; i++) {
        int par = nums[perm[i] - 1];

        if (dist[par - 1] == -1) {
            cout << -1 << endl;
            return;
        }
        ans[perm[i] - 1] = (i - dist[par - 1]);
        dist[perm[i] - 1] = i;
    }
    for (int x : ans) {
        cout << x << " ";
    }
    cout << endl;
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
