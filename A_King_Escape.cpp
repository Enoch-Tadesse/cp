#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

set<pair<int, int>> visited;

bool traverse(int n, int ax, int ay, int qx, int qy, int bx, int by) {
    if (ax == bx && ay == by) {
        return true;
    }
    for (int nr = max(ax - 1, 1); nr <= min(n, ax + 1); nr++) {
        for (int nc = max(ay - 1, 1); nc <= min(n, ay + 1); nc++) {
            if (visited.find({nr, nc}) != visited.end()) {
                continue;
            }
            if (nr == ax && nc == ay) {
                continue;
            }
            if (nc == qy || nr == qx || nr - nc == qx - qy ||
                nr + nc == qx + qy) {
                continue;
            }
            visited.insert({nr, nc});
            if (traverse(n, nr, nc, qx, qy, bx, by)) {
                return true;
            }
        }
    }
    return false;
}

void solve() {
    int n, qx, qy, ax, ay, bx, by;
    cin >> n;
    cin >> qx >> qy;
    cin >> ax >> ay;
    cin >> bx >> by;

    set<int> occ_cols;
    occ_cols.insert(qx - qy);
    occ_cols.insert(qx + qy);
    if (traverse(n, ax, ay, qx, qy, bx, by)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}
int main() {

    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
