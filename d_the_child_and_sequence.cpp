#include <bits/stdc++.h>
using namespace std;

typedef vector<long long> vl;
typedef long long ll;

typedef vector<ll> vl;

struct Node {
    ll sum;
    ll maxVal;
    Node(ll s = 0, ll m = LLONG_MIN) : sum(s), maxVal(m) {}
};

class SegmentTree {
    int n;
    vector<Node> tree;
    vl nums;

    int left(int p) { return (p << 1) + 1; }
    int right(int p) { return (p << 1) + 2; }

    void build(int p, int l, int r) {
        if (l == r) {
            tree[p] = Node(nums[l], nums[l]);
            return;
        }
        int mid = l + (r - l) / 2;
        build(left(p), l, mid);
        build(right(p), mid + 1, r);
        pull(p);
    }

    void pull(int p) {
        tree[p].sum = tree[left(p)].sum + tree[right(p)].sum;
        tree[p].maxVal = max(tree[left(p)].maxVal, tree[right(p)].maxVal);
    }

    ll querySum(int p, int l, int r, int L, int R) {
        if (l > R || r < L) return 0;
        if (L <= l && r <= R) return tree[p].sum;
        int mid = l + (r - l) / 2;
        return querySum(left(p), l, mid, L, R) +
               querySum(right(p), mid + 1, r, L, R);
    }

    void updatePoint(int p, int l, int r, int idx, ll val) {
        if (l == r) {
            tree[p] = Node(val, val);
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) updatePoint(left(p), l, mid, idx, val);
        else updatePoint(right(p), mid + 1, r, idx, val);
        pull(p);
    }

    void modRange(int p, int l, int r, int L, int R, ll modder) {
        if (l > R || r < L || tree[p].maxVal < modder) return;
        if (l == r) {
            tree[p].sum %= modder;
            tree[p].maxVal = tree[p].sum;
            return;
        }
        int mid = l + (r - l) / 2;
        modRange(left(p), l, mid, L, R, modder);
        modRange(right(p), mid + 1, r, L, R, modder);
        pull(p);
    }

public:
    SegmentTree(const vl &a) : nums(a) {
        n = nums.size();
        tree.assign(4 * n, Node());
        build(0, 0, n - 1);
    }

    ll querySum(int L, int R) { return querySum(0, 0, n - 1, L, R); }
    void updatePoint(int idx, ll val) { updatePoint(0, 0, n - 1, idx, val); }
    void modRange(int L, int R, ll modder) { modRange(0, 0, n - 1, L, R, modder); }
};

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

void solve() {
    int n, m;
    cin >> n >> m;
    vector<ll> arr(n);
    for (ll& x : arr) cin >> x;
    SegmentTree* seg = new SegmentTree(arr);
    loop(_, m) {
        ll kind;
        cin >> kind;
        ll l, r, mod, val, idx;
        switch (kind) {
            case 1:
                cin >> l >> r;
				l--; r--;
                print(seg->querySum(l, r));
				break;
            case 2:
                cin >> l >> r >> mod;
				l--; r--;
                seg->modRange(l, r, mod);
				break;
            case 3:
                cin >> idx >> val;
				idx--;
                seg->updatePoint(idx, val);
				break;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
