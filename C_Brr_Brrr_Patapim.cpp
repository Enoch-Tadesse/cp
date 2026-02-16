#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n;
    cin >> n;
    int r = n, c = n;
    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
        }
    vector<int> seen;
    int total = 0;
    for (int i = 0; i < c; i++) {
        seen.push_back(grid[0][i]);
        total += grid[0][i];
    }
    for (int i = 1; i < r; i++) {
        seen.push_back(grid[i][c - 1]);
        total += grid[i][c - 1];
    }
    cout << ((seen.size() + 1) * (seen.size() + 1 + 1)) / 2 - total << " ";
    for (int num : seen) {
        cout << num << " ";
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
