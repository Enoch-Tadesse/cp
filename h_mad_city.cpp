#include <bits/stdc++.h>

#include <algorithm>
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

void dijkstra(ll src, vll& best, umap<ll, vector<pair<ll, ll>>>& adj) {
    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>>
        heap;

    best[src] = 0;
    heap.push({0, src});

    while (!heap.empty()) {
        auto [cw, cc] = heap.top();
        heap.pop();
        if (cw > best[cc]) continue;

        for (auto& [nei, wei] : adj[cc]) {
            if (cw + wei < best[nei]) {
                best[nei] = cw + wei;
                heap.push({best[nei], nei});
            }
        }
    }

    return;
    // if (!par.count(dest)) return vll{-1};

    // vll path;
    // ll curr = dest;
    // while (curr != par[curr]) {
    //     path.push_back(curr);
    //     curr = par[curr];
    // }
    // path.push_back(src);
    // reverse(path.begin(), path.end());
    //
    // return path;
};

bool cycle(ll curr, ll par, set<ll>& seen, umap<ll, vector<pair<ll, ll>>>& adj,
           vll& path) {
    if (seen.count(curr)) {
        path.push_back(curr);
        return true;
    }
    seen.insert(curr);

    for (auto [ele, wei] : adj[curr]) {
        if (ele == par) continue;
        path.push_back(curr);
        if (cycle(ele, curr, seen, adj, path)) return true;
    }
    return false;
}

void solve() {
    ll n, m, v;
    cin >> n >> m >> v;

    ll a, b;
    umap<ll, vector<pair<ll, ll>>> adj;
    loop(_, n) {
        cin >> a >> b;
        adj[a].push_back({b, 1});
        adj[b].push_back({a, 1});
    }

    vll valeru(n + 1, LLONG_MAX);
    vll maleru(n + 1, LLONG_MAX);

    dijkstra(v, valeru, adj);
    dijkstra(m, maleru, adj);

    vll path;
    set<ll> seen;
    cycle(v, -1, seen, adj, path);
    // print(path.back());
    reverse(all(path));
    while (path.back() != path[0]) {
        path.pop_back();
    }

    for (ll ele : path) {
        if (valeru[ele] < maleru[ele]) {
            print("YES");
            return;
        }
    }
    print("NO");
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    loop_from(_, 0, t) { solve(); }
}
