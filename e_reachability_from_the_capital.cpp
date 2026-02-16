#include <bits/stdc++.h>

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

void markit(int start, umap<ll, vll>& adj, vll& parents) {
    queue<int> q;
    q.push(start);
    parents[start] = start;

    while (!q.empty()) {
        int curr = q.front(); q.pop();
        for (ll& nei : adj[curr]) {
            if (parents[nei] == -1) {
                parents[nei] = start;
                q.push(nei);
            }
        }
    }
}

void solve() {
    ll n, m, x;
    cin >> n >> m >> x;
    x--;

    umap<ll, vll> temp;
    umap<ll, ll> indegree;
    ll a, b;
    loop(_, m) {
        cin >> a >> b;
        a--; b--;
        temp[a].push_back(b);
        indegree[b]++;
    }

    Tarjan tar(temp, n);
    vll low = tar.low;

    // build compressed SCC adjacency list
    umap<ll, vll> adj;
    for (auto& [k, v] : temp) {
        for (ll &y : v) {
            if (low[k] != low[y]) // only keep edges between different SCCs
                adj[low[k]].push_back(low[y]);
        }
    }

    vll parents(n, -1);

    // BFS from capital
    markit(low[x], adj, parents);

    // BFS from zero-indegree SCCs not yet reached
    unordered_set<ll> scc_visited;
    for (int i = 0; i < n; i++) {
        if (parents[low[i]] == -1 && indegree[i] == 0 && !scc_visited.count(low[i])) {
            markit(low[i], adj, parents);
            scc_visited.insert(low[i]);
        }
    }

    // assign remaining unmarked nodes to their SCC id
    for (int i = 0; i < n; i++) {
        if (parents[i] == -1) parents[i] = low[i];
    }

    // count unique SCCs not connected to capital
    unordered_set<ll> seen;
    ll cnt = 0;
    for (int i = 0; i < n; i++) {
        if (parents[i] != low[x] && !seen.count(parents[i])) {
            cnt++;
            seen.insert(parents[i]);
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
