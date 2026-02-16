#include <bits/stdc++.h>
#include <set>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int r, c;
    cin >> r >> c;

    vector<vector<char>> grid(r, vector<char>(c));
    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        grid[i].assign(s.begin(), s.end());
    }
    set<char> seen;
    for (int nc = 0; nc < c; nc++) {
        char _max = '0';
        for (int nr = 0; nr < r; nr++) {
            _max = max(_max, grid[nr][nc]);
        }
        for (int nr = 0; nr < r; nr++) {
            if (_max == grid[nr][nc]) {
                seen.insert(nr + 1);
            }
        }
    }
    cout << seen.size() << "\n";
}
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
