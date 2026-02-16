#include <bits/stdc++.h>

#include <climits>
#include <stack>
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

class Tarjan {
    public:
        vll low, ids;
        vector<bool> on_stack;
        ll N;
        vll stack;
        ll id = 0;
        umap<ll, vll> adj;

    public:
        Tarjan(umap<ll, vll> adj, ll n)
            : adj(adj),
              N(n) {
            on_stack.assign(N, false);
            low.assign(N, LLONG_MAX);
            ids.assign(N, -1);

            tarjan();
        }

        void dfs(ll curr) {
            on_stack[curr] = true;
            stack.push_back(curr);
            ids[curr] = id;
            low[curr] = id;
            id++;
            for (ll& nei : adj[curr]) {
                if (ids[nei] == -1) dfs(nei);
                if (on_stack[nei]) low[curr] = min(low[curr], low[nei]);
            }

            if (ids[curr] == low[curr]) {
                while (true) {
                    ll top = stack.back();
                    stack.pop_back();
                    on_stack[top] = false;
                    low[top] = low[curr];
                    if (top == curr) break;
                }
            }
        }

        void tarjan() {
            for (int i = 0; i < N; i++) {
                if (ids[i] == -1) dfs(i);
            }
        }
};

void solve() {
    ll n;
    cin >> n;
    vector<ll> costs(n);
    for (ll& x : costs) {
        cin >> x;
    }
    ll m;
    cin >> m;
    ll u, v;
    umap<ll, vll> adj;
    while (m--) {
        cin >> u >> v;
        u--;
        v--;
        adj[u].push_back(v);
    }
    Tarjan tar(adj, n);
    vll low = tar.low;
    umap<ll, vll> ans;
    for (int i = 0; i < n; i++) {
        ans[low[i]].push_back(i);
    }
    ll count = 0;
    ll ways = 1;
    for (auto [x, y] : ans) {
        ll curr = LLONG_MAX;
        ll cnt = 0;
        for (ll z : y) curr = min(curr, costs[z]);
        for (ll z : y) {
            if (costs[z] == curr) cnt++;
        }
        count += curr;
        ways = (ways * cnt) % MOD;
    }
    cout << count << " " << ways << nl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
