#include <bits/stdc++.h>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
#define nl '\n'
#define print(x) cout << (x) << endl
#define show(v)                         \
    for (auto& x : v) cout << x << " "; \
    cout << endl
#define debug(i) cout << #i << ": " << i << endl

#define infi numeric_limits<ll>::max()
#define ninfi numeric_limits<ll>::min()
#define infd numeric_limits<ld>::infinity()
#define ninfd -numeric_limits<ld>::infinity()

typedef long long ll;
typedef long double ld;
typedef vector<ll> vll;

template <typename T>
using vec = vector<T>;

template <typename Container>
auto csum(const Container& v) -> decltype(*v.begin() + 0) {
    return accumulate(v.begin(), v.end(), decltype (*v.begin() + 0)(0));
}

template <typename Container>
auto cmax(const Container& c) -> decltype(*c.begin()) {
    return *max_element(c.begin(), c.end());
}

template <typename Container>
auto cmin(const Container& c) -> decltype(*c.begin()) {
    return *min_element(c.begin(), c.end());
}

template <typename Container, typename Key>
bool exist(const Container& c, const Key& k) {
    return c.find(k) != c.end();
}

template <typename Map>
auto keys(const Map& m) {
    using KeyType = typename Map::key_type;
    vector<KeyType> res;
    res.reserve(m.size());
    for (const auto& [k, _] : m) res.push_back(k);
    return res;
}

template <typename Map>
auto values(const Map& m) {
    using ValueType = typename Map::mapped_type;
    vector<ValueType> res;
    res.reserve(m.size());
    for (const auto& [_, v] : m) res.push_back(v);
    return res;
}

template <typename Map>
auto items(const Map& m) {
    using PairType = typename Map::value_type;
    vector<PairType> res;
    res.reserve(m.size());
    for (const auto& p : m) res.push_back(p);
    return res;
}

template <typename K, typename V>
using umap = unordered_map<K, V>;

bool dfs(vll& colors, umap<ll, vll>& adj, ll curr, ll par) {
    if (colors[curr] != -1) {
        return colors[curr] == 1 - colors[par];
    }
    colors[curr] = 1 - colors[par];
    for (ll& nei : adj[curr]) {
        if (!dfs(colors, adj, nei, curr)) return false;
    }
    return true;
}

void solve() {
    ll n, m;
    cin >> n >> m;
    ll u, v;
    umap<ll, vll> adj;
    loop(_, m) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vll colors(n + 1, -1);
    colors[0] = 0;
	for (int i = 1; i < n + 1; i++) {
		if (colors[i] != -1) continue;
		if (!dfs(colors, adj, i, 0)){
			print(-1);
			return;
		}
	}
    vll ones, zeros;
    for (int i = 1; i < n + 1; i++) {
        if (colors[i] == 1)
            ones.push_back(i);
        else
            zeros.push_back(i);
    }
    cout << zeros.size() << nl;
    show(zeros);

    cout << ones.size() << nl;
    show(ones);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
