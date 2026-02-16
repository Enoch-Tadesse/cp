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

typedef long long ll;
typedef vector<ll> vl;

struct Node {
        ll val;
        Node(ll v = LLONG_MAX)
            : val(v) {}
};

class SegmentTree {
        int n;
        vector<Node> tree;
        vl nums;

        int left(int p) { return (p << 1) + 1; }
        int right(int p) { return (p << 1) + 2; }

        void build(int p, int l, int r) {
            if (l == r) {
                tree[p] = Node(nums[l]);
                return;
            }
            int mid = l + (r - l) / 2;
            build(left(p), l, mid);
            build(right(p), mid + 1, r);
            tree[p].val = tree[left(p)].val + tree[right(p)].val;
        }

        ll queryRange(int p, int l, int r, int L, int R, ll x) {
            if (l == r) {
                return l;
            }
            ll mid = l + (r - l) / 2;
            if (tree[left(p)].val >= x)
                return queryRange(left(p), l, mid, L, R, x);
            return queryRange(right(p), mid + 1, r, L, R,
                              x - tree[left(p)].val);
        }

        void updatePoint(int p, int l, int r, int idx) {
            if (l == r) {
                tree[p].val = int(!tree[p].val);
                return;
            }
            int mid = l + (r - l) / 2;
            if (idx <= mid)
                updatePoint(left(p), l, mid, idx);
            else
                updatePoint(right(p), mid + 1, r, idx);
            tree[p].val = tree[left(p)].val + tree[right(p)].val;
        }

    public:
        SegmentTree(const vl& a)
            : nums(a) {
            n = nums.size();
            tree.assign(4 * n, Node());
            build(0, 0, n - 1);
        }

        ll queryRange(int L, int R, ll val) {
            return queryRange(0, 0, n - 1, L, R, val);
        }
        void updatePoint(int idx) { updatePoint(0, 0, n - 1, idx); }
};

void solve() {
    ll n, q;
    cin >> n >> q;
    vll nums(n);
    for (ll& x : nums) cin >> x;
    ll t, x;

    SegmentTree seg(nums);

    loop(_, q) {
        cin >> t >> x;
        if (t == 1) {
            seg.updatePoint(x);
        } else {
            print(seg.queryRange(0, n - 1, x + 1));
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
