
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int r, c;
    cin >> r >> c;

    vector<vector<char>> mat(r, vector<char>(c));
    for (int i = 0; i < r; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < c; j++) {
            mat[i][j] = s[j];
        }
    }

    vector<vector<bool>> poss(r, vector<bool>(c, false));

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (mat[i][j] == '0')
                break;
            poss[i][j] = true;
        }
    }

    for (int j = 0; j < c; j++) {
        for (int i = 0; i < r; i++) {
            if (mat[i][j] == '0')
                break;
            poss[i][j] = true;
        }
    }

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (mat[i][j] == '1' && !poss[i][j]) {
                cout << "NO\n";
                return;
            }
        }
    }
    cout << "YES\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
