
#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

bool valid(int guess, int n, int size, int t[], int z[], int y[]) {
    int counter = 0;
    int whole;
    int rem;
    for (int j = 0; j < size; j++) {
        whole = t[j] * z[j] + y[j];
        counter += (guess / whole) * z[j];
        rem = guess % whole;
        counter += min(rem / t[j], z[j]);

        counter += (guess) / (t[j] + y[j] / z[j]);
    }
    return counter >= n;
}

void contribution(int time, int size, int t[], int z[], int y[]) {
    int whole, rem;
    for (int i = 0; i < size; i++) {
        int counter = 0;
        whole = t[i] * z[i] + y[i];
        counter += (time / whole) * z[i];
        rem = time % whole;
        counter += min(rem / t[i], z[i]);
        cout << counter << " ";
    }
    std::cout << "\n";
}

void solve() {
    int n, test;
    cin >> n >> test;
    int t[test], z[test], y[test];
    int i = 0;
    while (test--) {
        cin >> t[i] >> z[i] >> y[i];
        i += 1;
    }
    int l = 1, r = 1e9 + 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (valid(mid, n, i, t, z, y)) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    cout << l << "\n";

    contribution(l, i, t, z, y);
}
int main() {

    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
