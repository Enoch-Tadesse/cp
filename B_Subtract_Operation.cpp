#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }

    set<int> seen;
    sort(nums.begin(), nums.end());

    for (auto num : nums) {
        if (seen.find(num - k) != seen.end()) {
            cout << "YES\n";
            return;
            break;
        }
        seen.insert(num);
    }
    cout << "NO\n";
    return;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
