#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int n, q;
    cin >> n >> q;
    vector<int> colors(n);
    for (int i = 0; i < n; ++i) {
        cin >> colors[i];
    }

    vector<vector<pair<int, int>>> nums(n);  // adjacency list with cost

    for (int i = 0; i < n - 1; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        --u; --v;
        nums[u].emplace_back(v, c);
        nums[v].emplace_back(u, c);
    }

    long long total = 0;
    for (int u = 0; u < n; ++u) {
        for (auto& [v, c] : nums[u]) {
            if (u < v && colors[u] != colors[v]) {
                total += c;
            }
        }
    }

    while (q--) {
        int v, ncolor;
        cin >> v >> ncolor;
        --v;

        if (colors[v] == ncolor) {
            cout << total << "\n";
            continue;
        }

        int ocolor = colors[v];
        for (auto& [nei, c] : nums[v]) {
            if (colors[nei] == ocolor) {
                total += c;
            }
            if (colors[nei] == ncolor) {
                total -= c;
            }
        }

        colors[v] = ncolor;
        cout << total << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
