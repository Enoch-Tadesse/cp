#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
    int n;
    cin >> n;
    vector<int> arr(n);
    int count = 0;
    for (int &x : arr) {
        cin >> x;
        count += x;
    }
    if (count == n){
        cout << "YES\n";
        return;
    }
    for (int i = 1; i < n; i++) {
        if (arr[i] == arr[i - 1] && arr[i] == 0) {
            cout << "YES\n";
            return;
        }
    }
    cout << "NO\n";
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
