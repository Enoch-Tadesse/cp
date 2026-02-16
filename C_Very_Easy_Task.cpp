#include <bits/stdc++.h>
#include <cmath>
using namespace std;

bool valid(int x, int y, int guess, int n) {

    guess -= min(x, y); // to print the first copy
    if (guess < 0)
        return false;
    int counter =
        1 + guess / x + guess / y; // how many more I can print within the time
    return counter >= n;
}

void solve() {
    int n, x, y;
    cin >> n >> x >> y;
    int l = 0;
    int r = n * max(x, y) + 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (valid(x, y, mid, n)) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    cout << l << " ";
}
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
