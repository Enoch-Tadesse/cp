#include <bits/stdc++.h>

#include <algorithm>
#include <cstdint>
#include <functional>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define int long long
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
    ll n;
    cin >> n;
    vector<bool> alive(n, false);
    vector<ll> nums(n);

    for (ll& x : nums) {
        cin >> x;
    }
    vector<ll> seq(n);
    for (ll& x : seq) {
        cin >> x;
        x--;
    }

    umap<ll, ll> par;
    umap<ll, ll> total;
    for (ll i = 0; i < n; i++) {
        par[i] = i;
        total[i] = 0;
    }

    ll _max = 0;

    function<ll(ll)> find = [&](ll x) {
        if (par[x] != x) par[x] = find(par[x]);
        return par[x];
    };

    function<void(ll, ll)> merge = [&](ll x, ll y) {
        ll px = find(x);
        ll py = find(y);
        if (alive[px] && alive[py]) {
            if (px == py) return;
            par[px] = py;
            total[py] += total[px];
            _max = max(_max, total[py]);
        }
    };

    vll ans = {};
    ans.push_back(0);

    for (ll i = n - 1; i > 0; i--) {
        ll x = seq[i];
        alive[x] = true;
        total[x] = nums[x];
        _max = max(_max, nums[x]);
        if (x + 1 < n) merge(x, x + 1);
        if (x - 1 >= 0) merge(x, x - 1);
        ans.push_back(_max);
    }
    reverse(all(ans));
    for (ll x : ans) print(x);
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
