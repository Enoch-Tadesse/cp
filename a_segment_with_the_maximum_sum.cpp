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

class Node {
    public:
        ll val;
        ll lmax;
        ll rmax;
        ll total;
        ll mmax;
        Node(ll v)
            : val(v),
              lmax(max(v, 0LL)),
              rmax(max(v, 0LL)),
              total(v),
              mmax(max(v, 0LL)) {}
};

class SegmentTree {
        ll n;
        vector<Node> tree;
        vll nums;

    public:
        SegmentTree(ll n, vll nums) {
            this->n = n;
            this->nums = nums;
            this->tree.assign(4 * n, Node(0));
            build(0, 0, n - 1);
        }

        Node pull(Node left, Node right) {
            Node curr = Node(0);
            curr.total = left.total + right.total;
            curr.rmax = max(right.total + left.rmax, right.rmax);
            curr.lmax = max(left.total + right.lmax, left.lmax);
            curr.mmax = max({left.mmax, right.mmax, left.rmax + right.lmax});
            return curr;
        }

        void build(ll node, ll l, ll r) {
            if (l == r) {
                tree[node] = Node(nums[l]);
                return;
            }
            ll mid = l + (r - l) / 2;
            build(node * 2 + 1, l, mid);
            build(node * 2 + 2, mid + 1, r);
            tree[node] = pull(tree[node * 2 + 1], tree[node * 2 + 2]);
        }

        Node query(ll node, ll l, ll r, ll L, ll R) {
            if (l > R || r < L) return Node(0);
            if (l >= L && r <= R) return tree[node];
            ll mid = l + (r - l) / 2;
            Node left = query(node * 2 + 1, l, mid, L, R);
            Node right = query(node * 2 + 2, mid + 1, r, L, R);
            return pull(left, right);
        }

        void update(ll node, ll l, ll r, ll pos, ll val) {
            if (l == r) {
                nums[pos] = val;
                tree[node] = Node(val);
                return;
            }
            ll mid = l + (r - l) / 2;
            if (pos <= mid)
                update(node * 2 + 1, l, mid, pos, val);
            else
                update(node * 2 + 2, mid + 1, r, pos, val);
            Node left = tree[node * 2 + 1];
            Node right = tree[node * 2 + 2];
            tree[node] = pull(left, right);
        }
};

void solve() {
    ll n, k;
    cin >> n >> k;
    vector<ll> nums(n);
    for (ll& x : nums) {
        cin >> x;
    }
    SegmentTree seg(n, nums);
    ll i, val;
    Node curr = seg.query(0, 0, n - 1, 0, n - 1);
    print(curr.mmax);

    loop(_, k) {
        cin >> i >> val;
        seg.update(0, 0, n - 1, i, val);
        curr = seg.query(0, 0, n - 1, 0, n - 1);
        print(curr.mmax);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
