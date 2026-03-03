#include <bits/stdc++.h>

#include <climits>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
#define pb push_back()
#define pob pop_back()
#define int long long
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
    umap<ll, vector<tuple<ll, ll>>> adj;
    loop(_, m) {
        ll a, b, w;
        cin >> a >> b >> w;
        a--;
        b--;
        adj[a].push_back({b, w});
        adj[b].push_back({a, w});
    }

    vll toin(n);
    vll toout(n);
    ll timer = 0;
    ll LOG = ceil(log2(n)) + 1;
    vector<vector<ll>> up(n, vector<ll>(LOG, -1));
    vector<vector<ll>> mx(n, vector<ll>(LOG, LLONG_MAX));

    function<void(ll, ll, ll)> dfs = [&](ll c, ll p, ll w) {
        up[c][0] = p;
        mx[c][0] = w;
        toin[c] = ++timer;
        for (int i = 1; i < LOG; i++) {
            if (up[c][i - 1] != -1) {
                up[c][i] = up[up[c][i - 1]][i - 1];
                mx[c][i] = min(mx[up[c][i - 1]][i - 1], mx[c][i - 1]);
            }
        }
        for (auto& [x, nw] : adj[c]) {
            if (x != p) dfs(x, c, nw);
        }
        toout[c] = ++timer;
    };
    ll root = 0;
    dfs(root, -1, 0);

    function<bool(ll, ll)> isAncestor = [&](ll u, ll v) {
        return (toin[u] < toin[v] && toout[u] > toout[v]);
    };

    function<ll(ll, ll)> get_min = [&](ll u, ll anc) {
        ll res = LLONG_MAX;

        for (int i = LOG - 1; i >= 0; --i) {
            if (up[u][i] != -1 && !isAncestor(up[u][i], anc)) {
                res = min(res, mx[u][i]);
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

    ll q;
    cin >> q;
    loop(_, q) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;

        ll L = lca(a, b);
        ll mx_edge = min(get_min(a, L), get_min(b, L));
        print(mx_edge);
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
