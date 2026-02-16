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

class Two_SAT {
        ll n;
        ll vers;
        vll n_vertices;
        vll stack;
        vll comp;
        vector<bool> visited;
        umap<ll, vll> adj;
        umap<ll, vll> radj;

        void dfs1(ll curr) {
            visited[curr] = true;
            for (ll x : adj[curr]) {
                if (!visited[x]) dfs1(x);
            }
            stack.push_back(curr);
        }

        void dfs2(ll curr, ll id) {
            comp[curr] = id;
            for (ll x : radj[curr]) {
                if (comp[x] == -1) dfs2(x, id);
            }
        }

    public:
        vector<bool> ass;
        Two_SAT(ll n)
            : n(n),
              vers(2 * n) {
            visited.assign(vers, false);
            n_vertices.assign(n, false);
            ass.assign(n, false);
        }

        bool solver() {
            for (int i = 0; i < vers; i++) {
                if (!visited[i]) dfs1(i);
            }

            comp.assign(vers, -1);
            ll id = 0;

            while (!stack.empty()) {
                ll curr = stack.back();
                stack.pop_back();
                if (comp[curr] == -1) dfs2(curr, id++);
            }

            for (int i = 0; i < vers; i += 2) {
                if (comp[i] == comp[i + 1]) return false;
                ass[i / 2] = comp[i] > comp[i + 1];
            }

            return true;
        }

        void add_comp(ll a, bool na, ll b, bool nb) {
            a = 2 * a ^ na;
            b = 2 * b ^ nb;
            ll neg_a = a ^ 1;
            ll neg_b = b ^ 1;

            adj[neg_a].push_back(b);
            adj[neg_b].push_back(a);

            radj[a].push_back(neg_b);
            radj[b].push_back(neg_a);
        }
};

void solve() {
    ll n, a, b;
    cin >> n >> a >> b;
    umap<ll, ll> index;
    vector<ll> nums(n);
    ll i = 0;
    for (ll& x : nums) {
        cin >> x;
        index[x] = i;
        i++;
    }
    if (n & 1) {
        print("NO");
        return;
    }

    Two_SAT sat(n);

for (int i = 0; i < n; i++) {
    ll num = nums[i];
    bool ok = false;

    if (index.count(a - num)) {
        int j = index[a - num];
		if (i < j) {
			sat.add_comp(i, false, j, false); // same group
			sat.add_comp(i, true, j, true);   // same group
		}
        ok = true;
    }

    if (index.count(b - num)) {
        int j = index[b - num];
		if (i < j) {
			sat.add_comp(i, false, j, true);  // different groups
			sat.add_comp(i, true, j, false);  // different groups
		}
        ok = true;
    }

    if (!ok) {
        print("NO");
        return;
    }
}
    if (!sat.solver()) {
        print("NO");
        return;
    }
    cout << "YES" << nl;
    for (int i = 0; i < n; i++) {
        if (sat.ass[i])
            cout << "1 ";
        else
            cout << "0 ";
    }
    cout << nl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    loop_from(_, 0, t) { solve(); }
}
