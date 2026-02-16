#include <bits/stdc++.h>

#include <algorithm>
#include <cmath>
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
long long modPow(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;

    while (exp > 0) {
        if (exp % 2 == 1) {
            res = (res * base) % mod;
        }

        base = (base * base) % mod;
        exp /= 2;
    }

    return res;
}

void solve() {
    ll n, m;
    cin >> n >> m;
    ll a, b, w;
    vector<tuple<ll, ll, ll>> queries;
    umap<ll, ll> par;
    for (int i = 0; i < n; i++) par[i] = i;

    vector<tuple<ll, ll, ll>> edges;

    loop(_, m) {
        cin >> a >> b >> w;
        a--;
        b--;
        queries.push_back({a, b, w});
        edges.push_back({w, a, b});
    }

    function<int(int)> find = [&](int x) {
        if (par[x] != x) par[x] = find(par[x]);
        return par[x];
    };

    function<bool(int, int)> merge = [&](int x, int y) {
        ll px = find(x);
        ll py = find(y);
        if (px == py) return false;
        par[px] = py;
        return true;
    };

    sort(all(edges));

    ll mst = 0;
    ll root = 0;
    umap<ll, vector<tuple<ll, ll>>> adj;
    for (auto& [w, a, b] : edges) {
        if (merge(a, b)) {
            adj[a].push_back({b, w});
            adj[b].push_back({a, w});
            root = a;
            mst += w;
        }
    }

    vll toin(n);
    vll toout(n);
    ll timer = 0;
    ll LOG = ceil(log2(n)) + 1;
    vector<vector<ll>> up(n, vector<ll>(LOG, -1));
    vector<vector<ll>> mx(n, vector<ll>(LOG, 0));

    function<void(ll, ll, ll)> dfs = [&](ll c, ll p, ll w) {
        up[c][0] = p;
        mx[c][0] = w;
        toin[c] = ++timer;
        for (int i = 1; i < LOG; i++) {
            if (up[c][i - 1] != -1) {
                up[c][i] = up[up[c][i - 1]][i - 1];
                mx[c][i] = max(mx[up[c][i - 1]][i - 1], mx[c][i - 1]);
            }
        }
        for (auto& [x, nw] : adj[c]) {
            if (x != p) dfs(x, c, nw);
        }
        toout[c] = ++timer;
    };
    dfs(root, -1, 0);

    function<bool(ll, ll)> isAncestor = [&](ll u, ll v) {
        return (toin[u] < toin[v] && toout[u] > toout[v]);
    };

    function<ll(ll, ll)> get_max = [&](ll u, ll anc) {
        ll res = 0;

        for (int i = LOG - 1; i >= 0; --i) {
            if (up[u][i] != -1 && !isAncestor(up[u][i], anc)) {
                res = max(res, mx[u][i]);
                u = up[u][i];
            }
        }

        return res;
    };

    function<ll(ll, ll)> lca = [&](ll u, ll v) {
        if (isAncestor(u, v)) return u;
        if (isAncestor(v, u)) return v;

        for (int i = LOG - 1; i >= 0; --i) {
            if (up[u][i] != -1 && !isAncestor(up[u][i], v)) u = up[u][i];
        }

        return up[u][0];
    };

    for (auto& [u, v, w] : queries) {
        ll L = lca(u, v);
        ll mx_edge = max(get_max(u, L), get_max(v, L));
        print(mst - mx_edge + w);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
