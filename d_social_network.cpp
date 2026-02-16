#include <bits/stdc++.h>
#include <unordered_set>
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

ll find(ll curr, umap<ll, ll>& par, umap<ll, ll>& counts) {
    if (curr != par[curr]) {
        par[curr] = find(par[curr], par, counts);
    }
    return par[curr];
}

bool dsu(ll x, ll y, umap<ll, ll>& counts, umap<ll, ll>& par) {
    auto rx = find(x, par, counts);
    auto ry = find(y, par, counts);
    if (rx == ry) {
        return false;
    }
    par[ry] = rx;
    counts[rx] += counts[ry];
    return true;
}

void solve() {
    ll n, k;
    cin >> n >> k;
    ll u, v;
    umap<ll, ll> par;
    umap<ll, ll> counts;
    for (int i = 1; i <= n; i++) {
        par[i] = i;
        counts[i] = 1;
    }
    ll curr = 0;
    loop(_, k) {
        cin >> u >> v;
        if (!dsu(u, v,  counts, par)) {
			curr ++;
		}
		unordered_set<ll> seen;
		for (int i = 1; i <=n; i++) {
			seen.insert(find(i, par, counts));
		}
		vector<ll> size;
		for(auto x: seen) {
			size.push_back(counts[x]);
		}
		sort(size.rbegin(), size.rend());
		ll ans = 0;
		for (int i = 0; i <= curr; i++) {
			ans += size[i];
		}
		print(ans - 1);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
