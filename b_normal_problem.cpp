#include <bits/stdc++.h>
using namespace std;
template <typename T>
T getMax(const std::vector<T> &nums) {
    return *max_element(nums.begin(), nums.end());
}
typedef long long ll;

void solve() {
	vector<char> words;
	string s;
	cin >> s;
	words.assign(s.begin(), s.end());
	for (int i = words.size()-1; i >=0; i-- ) {
		if (words[i] == 'q') cout << 'p';
		else if (words[i] == 'p') cout << 'q';
		else  cout << 'w';
	}
    cout << endl;
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
