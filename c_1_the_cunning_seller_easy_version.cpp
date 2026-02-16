#include <bits/stdc++.h>
using namespace std;

#define loop(i, s, n) for (int i = s; i < n; i++)
#define MOD 1'000'000'007
#define nl '\n'
#define print(x) cout << x << endl
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

vector<ll> powers;
ll calculate(ll x) {
    if (x == 0) return 3;
    return powers[x + 1] + x * powers[x - 1];
}
void solve() {
    ll n;
    cin >> n;
    ll counter = 0;

    while (n > 0) {
        ll times =
            upper_bound(powers.begin(), powers.end(), n) - powers.begin() - 1;
        counter += calculate(times);
        n -= powers[times];
    }
	print(counter);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll v = 1;
    while (v <= MOD) {
        powers.push_back(v);
        v *= 3;
    }
    int t = 1;
    cin >> t;
    loop(_, 0, t) { solve(); }
}
