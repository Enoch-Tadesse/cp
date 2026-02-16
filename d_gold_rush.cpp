#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool dfs(ll curr, ll target) {
	if (curr == target) {
		return true;
	}
	if (curr % 3 != 0) {
		return false;
	}
	ll num = curr / 3;
	if (dfs(curr - num, target) || dfs(num, target)) {
		return true;
	}
	return false;
}

void solve() {
	ll n , m;
	cin >> n >> m;
	if (m > n) {
		cout << "NO\n";
		return;
	}
	if (m == n) {
		cout << "YES\n";
		return;
	}
	if (dfs(n , m)) cout << "YES\n";
	else cout << "NO\n";
}

int main() {
	int t;
	cin >> t;
	while (t--)
		solve();
}


