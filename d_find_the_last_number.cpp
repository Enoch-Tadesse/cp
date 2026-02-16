#include <bits/stdc++.h>
using namespace std;

int query(int i, int x) {
    cout << "? " << i << " " << x << endl;
    cout.flush();
    int res;
    cin >> res;
    if (res == -1) exit(0); 
    return res;
}

void solve() {
    int n;
    cin >> n;

    vector<int> candidates(n - 1);
    iota(candidates.begin(), candidates.end(), 1); 

    int last = 1; 
    for (int i = 2; i <= n - 1; ++i) {
        int res1 = query(last, n); 
        int res2 = query(i, n);

        if (res1 < res2) last = i;
    }

    set<int> used;
    for (int i = 1; i <= n - 1; ++i) used.insert(i);

    for (int i = 1; i <= n; ++i) {
        if (!used.count(i)) {
            cout << "! " << i << endl;
            cout.flush();
            return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) solve();
}
