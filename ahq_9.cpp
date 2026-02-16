#include <bits/stdc++.h>

#include <set>
#include <unordered_set>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
    string word;
    cin >> word;
    unordered_set<char> special = {'H', 'Q', '9'};
    for (char x : word){
        if (special.find(x) != special.end()){
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

        while (t--) {
            solve();
        }
    }
