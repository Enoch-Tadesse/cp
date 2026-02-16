#include <bits/stdc++.h>

#include <functional>
#include <utility>
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
    string v;
    ll x, y;
    vll par(n + 1);
    vll lazy(n + 1, 0);
    for (int i = 1; i <= n; i++) par[i] = i;

    function<pair<ll, ll>(int)> find = [&](int x) {
        ll l = lazy[x];  // lazy for current x
        if (par[x] != x) {
            auto [p, z] = find(par[x]);
            par[x] = p;
            l += z;  // apply every ancestoral lazy
        } else
            return make_pair(x, l);
        lazy[x] = l - lazy[par[x]];
        return make_pair(par[x], l);
    };

    function<void(int, int)> merge = [&](int x, int y) {
        auto [px, _] = find(x);
        auto [py, __] = find(y);
        if (px == py) return;
        // lazy[px] and lazy[py] will be zero, don't worry
        par[px] = py;
        lazy[px] -= lazy[py];
    };

    loop(_, m) {
        cin >> v;
        if (v == "add") {
            cin >> x >> y;
            auto [px, _] = find(x);
            // add it to lazy of parent
            lazy[px] += y;
        } else if (v == "join") {
            cin >> x >> y;
            merge(x, y);
        } else {
            cin >> x;
            find(x);  // apply the lazy part
            print(find(x).second);
        }
    }
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
