#include <bits/stdc++.h>

#include <climits>
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

typedef long long ll;
typedef vector<ll> vl;

struct Node {
        ll val;
        Node(ll v = 0)
            : val(v) {}
};

class SegmentTree {
        int n;
        vector<Node> tree;

        int left(int p) { return (p << 1) + 1; }
        int right(int p) { return (p << 1) + 2; }

        ll queryRange(int p, int l, int r, int L, int R) {
            if (l > R || r < L) return 0;
            if (L <= l && r <= R) return tree[p].val;
            int mid = l + (r - l) / 2;
            return queryRange(left(p), l, mid, L, R) +
                   queryRange(right(p), mid + 1, r, L, R);
        }

        void updatePoint(int p, int l, int r, int idx, ll val) {
            if (l == r) {
                tree[p] = Node(val);
                return;
            }
            int mid = l + (r - l) / 2;
            if (idx <= mid)
                updatePoint(left(p), l, mid, idx, val);
            else
                updatePoint(right(p), mid + 1, r, idx, val);
            tree[p].val = tree[left(p)].val + tree[right(p)].val;
        }

    public:
        SegmentTree(ll n)
            : n(n) {
            tree.assign(4 * n, Node());
        }

        ll queryRange(int L, int R) { return queryRange(0, 0, n - 1, L, R); }
        void updatePoint(int idx, ll val) {
            updatePoint(0, 0, n - 1, idx, val);
        }
};

void solve() {
    ll n;
    cin >> n;
    vector<ll> nums(n);
    for (ll& x : nums) {
        cin >> x;
    }
    SegmentTree seg(n);
    for (int i = 0; i < n; ++i) {
        cout << seg.queryRange(nums[i] - 1, n - 1) << " ";
        seg.updatePoint(nums[i] - 1, 1);
    }
    cout << nl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
