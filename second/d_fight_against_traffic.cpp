#include <bits/stdc++.h>

#include <climits>
#include <queue>
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

template <typename K>
using uset = unordered_set<K>;

void shortest(ll p, umap<ll, uset<ll>>& adj, vll& best) {
    best[p] = 0;
    queue<ll> q;
    q.push(p);
    vector<bool> seen(best.size(), false);
    seen[p] = true;
    ll level = 1;
    while (!q.empty()) {
        ll size = q.size();
        loop(_, size) {
            ll curr = q.front();
            q.pop();
            for (ll x : adj[curr]) {
                if (seen[x]) continue;
                seen[x] = true;
                best[x] = level;
                q.push(x);
            }
        }
        level++;
    }
}

void solve() {
    ll n, m, s, t;
    cin >> n >> m >> s >> t;
    s--;
    t--;
    umap<ll, uset<ll>> adj;
    ll a, b;
    loop(_, m) {
        cin >> a >> b;
        a--;
        b--;
        adj[a].insert(b);
        adj[b].insert(a);
    }

    vll froms(n, LLONG_MAX);
    shortest(s, adj, froms);

    vll fromt(n, LLONG_MAX);
    shortest(t, adj, fromt);
    ll cnt = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (adj[i].find(j) == adj[i].end()) {
                auto d =froms[i] + fromt[j] + 1;
				d = min(d, fromt[i] + froms[j] + 1);
				if (d >= fromt[s]) cnt++;
            }
        }
    }
    print(cnt);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
