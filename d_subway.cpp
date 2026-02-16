#include <bits/stdc++.h>

#include <algorithm>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
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
    ll n;
    cin >> n;
    umap<ll, vector<pair<ll, ll>>> adj;
    ll a, b;
    loop(_, n) {
        cin >> a >> b;
        a--;
        b--;
        adj[a].push_back({b, 1});
        adj[b].push_back({a, 1});
    }

    vector<bool> visited(n, false);
    vll path;

    function<bool(int, int)> detect = [&](int curr, int par) {
        if (visited[curr]) return true;
        visited[curr] = true;
        for (auto [x, _] : adj[curr]) {
            if (x == par) continue;

            path.push_back(x);
            if (detect(x, curr)) return true;
            path.pop_back();
        }

        return false;
    };

    path.push_back(0);
    detect(0, -1);
    reverse(all(path));
    while (path[0] != path.back()) path.pop_back();
    path.pop_back();

    auto dijkstra = [&](vll src, umap<ll, vector<pair<ll, ll>>>& adj) {
        umap<ll, ll> par;
        priority_queue<pair<ll, ll>, vector<pair<ll, ll>>,
                       greater<pair<ll, ll>>>
            heap;
        vll dist(n, LLONG_MAX);

        for (ll x : src) {
            dist[x] = 0;
            heap.push({0, x});
        }

        while (!heap.empty()) {
            auto [cw, cc] = heap.top();
            heap.pop();
            if (cw > dist[cc]) continue;

            for (auto& [nei, wei] : adj[cc]) {
                if (cw + wei < dist[nei]) {
                    dist[nei] = cw + wei;
                    heap.push({dist[nei], nei});
                }
            }
        }
        return dist;
    };

    vll ans = dijkstra(path, adj);
	show(ans);
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
