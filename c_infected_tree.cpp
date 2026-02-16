#include <bits/stdc++.h>

#include <climits>
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
#define all(x) (x).begin(), (x).end()

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

static mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
#define RAND(a, b) uniform_int_distribution<long long>(a, b)(rng)
ll big = RAND(1, 1e9);

ll dfs(ll curr, ll par, umap<ll, vll>& adj, ll depth) {
    if (adj[curr].size() == 1 && adj[curr][0] == par) {
        return depth;
    }
    ll ans = LLONG_MAX;
    for (auto nei : adj[curr]) {
        if (nei == par) continue;
        ans = min(ans, dfs(nei, curr, adj, depth + 1));
    }
    return ans;
}

ll dfs2(ll curr, ll par, umap<ll, vll>& adj, ll depth, ll target) {
    if (adj[curr].size() == 1 && adj[curr][0] == par) {
        return int(depth == target);
    }

    bool turn = 0;
    vector<ll> pos = {0, 0};

    for (auto nei : adj[curr]) {
        if (nei == par) continue;
        ll x = dfs2(nei, curr, adj, depth + 1, target);
        pos[turn] = (long long)x + (long long)adj[curr].size();
        turn ^= 1;
    }
    if (pos[0] != 0 && pos[1] != 0) {
		if (curr != 1) return 1;
		return min(pos[0] , pos[1]) + 1;
    } else if (pos[0] != 0) {
        return pos[0] + adj[curr].size() - 1 + int(curr == 1);
    } else if (pos[1] != 0) {
        return pos[1] + adj[curr].size() - 1 + int(curr == 1);
    }
    return 0 + int(curr == 1);
}

void solve() {
    ll n;
    cin >> n;
    ll u, v;
    umap<ll, vll> adj;
    loop(_, n - 1) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    ll shal = dfs(1, -1, adj, 0);
    ll x = dfs2(1, -1, adj, 0, shal);
    print(n - x + 1);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    loop_from(_, 0, t) { solve(); }
}
