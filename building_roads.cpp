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


umap<ll, ll> par;

umap<ll, ll> r;
ll find(ll x) {
    if (par[x] != x) {
        par[x] = find(par[x]);
    }
    return par[x];
}

void un(ll x, ll y) {
    ll rootx = find(x);
    ll rooty = find(y);

    if (rootx == rooty) return;
    if (r[rootx] > r[rooty])
        par[rooty] = rootx;
    else if (r[rootx] < r[rooty])
        par[rootx] = rooty;
    else {
        par[rootx] = rooty;
        r[rooty] += 1;
    }
}
void solve() {
    ll n, q;
    cin >> n >> q;
    loop_from(i, 1, n + 1) {
        par[i] = i;
        r[i] = 0;
    }
    ll a, b;
    loop(_, q) {
        cin >> a >> b;
        un(a, b);
    }
    unordered_set<ll> seen;
    for (ll i = 1; i < n + 1; i++) {
        seen.insert(find(i));
    }
    cout << seen.size()  - 1<< nl;
    vll nums;
    for (ll x : seen) nums.push_back(x);
    for (int i = 1; i < nums.size(); i++) {
        cout << nums[i] << " " << nums[i - 1] << nl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
