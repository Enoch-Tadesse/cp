#include <bits/stdc++.h>

#include <algorithm>
#include <climits>
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
    ll n, m;
    cin >> n >> m;
    umap<ll, ll> par;
    umap<ll, ll> _min;
    umap<ll, ll> _max;
    umap<ll, ll> size;

    for (int i = 1; i <= n; i++) {
        par[i] = i;
        _min[i] = i;
        _max[i] = i;
        size[i] = 1;
    }

    function<ll(ll)> find = [&](ll x) {
        if (par[x] != x) par[x] = find(par[x]);
        return par[x];
    };

    function<bool(ll, ll)> merge = [&](ll x, ll y) {
        ll px = find(x);
        ll py = find(y);
        if (px == py) return false;
        par[py] = px;
        _min[px] = min(_min[px], _min[py]);
        _max[px] = max(_max[px], _max[py]);
        size[px] += size[py];
        return true;
    };

    ll a, b;
    loop(_, m) {
        cin >> a >> b;
        merge(a, b);
    }

    set<ll> groups;
    for (int i = 1; i <= n; i++) {
        groups.insert(find(i));
    }

    ll ans = 0;

    for (ll g : groups) {
        if (find(g) != g) continue;
        if (_max[g] - _min[g] + 1 != size[g]) {
            for (int j = _min[g] + 1; j < _max[g]; j++) {
                if (merge(j, g)) ans++;
            }
        }
    }
    print(ans);

    // if (help.size() <= 1) {
    //     print(0);
    //     return;
    // }
    //
    // sort(all(help), [](const tuple<ll, ll, ll>& a, const tuple<ll, ll, ll>&
    // b) {
    //     if (get<0>(a) != get<0>(b)) return get<0>(a) < get<0>(b);
    //     return get<1>(a) > get<1>(b);
    // });
    //
    // ll ans = 1;
    //
    // ll L = get<0>(help[0]);
    // ll R = get<1>(help[0]);
    //
    // for (int i = 1; i < help.size(); i++) {
    //     ll start = get<0>(help[i]);
    //     if (start < R) {
    //         R = max(R, get<1>(help[i]));
    //     } else {
    //         ans++;
    //         R = get<1>(help[i]);
    //     }
    // }
    // print(ans);
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
