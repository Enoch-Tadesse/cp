#include <bits/stdc++.h>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    int n;
    cin >> n;
    string word;
    cin >> word;
    int inc = 1;
    int i = 0;
    while (i < word.size()) {
        cout << word[i];
        i += inc;
        inc += 1;
    }
    cout << endl;
}
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
