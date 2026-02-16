#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int r, c, k;
    cin >> r >> c >> k;
    vector<vector<int>> grid(r, vector<int>(c));
    int i = 0;
    for (int nr = 0; nr < r; nr++) {
        for (int nc = 0; nc < c; nc++) {
            grid[nr][nc] = i % k + 1;
            i += 1;
        }
    }
    bool rev = false;
    for (int nr = 0; nr < r; nr++) {
        if (!(rev)) {
            for (int nc = 0; nc < c; nc++) {
                cout << grid[nr][nc] << " ";
            }
            rev = !(rev);
        } else {
            for (int nc = c - 1; nc >= 0; nc--) {
                cout << grid[nr][nc] << " ";
            }
            rev = !(rev);
        }
        cout << endl;
    }
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
