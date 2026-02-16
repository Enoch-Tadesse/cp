#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n, x;
    cin >> n >> x;
    vector<int> nums(n);
    for (int &x : nums) {
        cin >> x;
    }
    sort(nums.begin(), nums.end());
    int counter = 0;
    int l = n - 1;
    for (int r = n - 1; r > -1; r --){
        if ((l - r + 1) * nums[r] < x){
            continue;
        } 
        counter += 1;
        l = r - 1;
    }
    cout << counter << "\n";
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
