#include <bits/stdc++.h>
#include <ios>
#include <limits>
using namespace std;
template <typename T> T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}

void solve() {
    string word;
    cin.clear();
    // cin.ignore();
    getline(cin, word);

    cout << word[0];
    for (int i = 1; i < word.size(); i++) {
        if (word[i] == ' ') {
            cout << word[i + 1];
        }
    }

    cout << "\n";
}
int main() {

    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);

    int t = 1;
    cin >> t;
    cin.ignore(1);
    // char x;
    // cin >> x;
    while (t--) {
        solve();
    }
}
