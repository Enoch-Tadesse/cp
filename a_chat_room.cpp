#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
    string key = "hello";
    string word;
    cin >> word;
    int inner = 0;
    int i = 0;
    while (i < key.size()) {
        while ((inner < word.size()) && (word[inner] != key[i])) {
            inner += 1;
        }
        inner += 1;
        if (inner > word.size()) {
            break;
        }
        i += 1;
    }
    if (i == key.size()) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    while (t--) {
        solve();
    }
}
