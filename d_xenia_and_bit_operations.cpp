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

class Node {
    public:
        ll val = 0;
        ll depth = 0;
        Node() {}
};

class SegmentTree {
    private:
        vector<Node> st;
        ll n;
        vector<ll> nums;

        ll left(ll x) { return (x << 1) + 1; }
        ll right(ll x) { return (x << 1) + 2; }

        void build(ll p, ll l, ll r) {
            if (l == r) {
                st[p].depth = 0;
                st[p].val = nums[l];
                return;
            }

            ll mid = l + (r - l) / 2;
            build(left(p), l, mid);
            build(right(p), mid + 1, r);

            if (st[left(p)].depth == 0) {
                st[p].depth = 1;
                st[p].val = st[left(p)].val | st[right(p)].val;
            } else {
                st[p].depth = 0;
                st[p].val = st[left(p)].val ^ st[right(p)].val;
            }
            return;
        }

        void updateHelper(ll p, ll index, ll val, ll l, ll r) {
            if (l == r) {
                st[p].val = val;
                return;
            }
            ll mid = l + (r - l) / 2;
            if (index <= mid)
                updateHelper(left(p), index, val, l, mid);
            else
                updateHelper(right(p), index, val, mid + 1, r);

            if (st[p].depth == 0) {
                st[p].val = st[left(p)].val ^ st[right(p)].val;
            } else {
                st[p].val = st[left(p)].val | st[right(p)].val;
            }
            return;
        }

    public:
        SegmentTree(vector<ll> nums) {
            this->nums = nums;
            n = (ll)nums.size();
            st.assign(4 * n, Node());
            build(0, 0, n - 1);
        }

        void deb() {
            for (auto some : st) cout << some.val << " ";
            cout << nl;
        }

        ll update(ll index, ll val) {
            updateHelper(0, index, val, 0, n - 1);
            return st[0].val;
        }
};

void solve() {
    ll n, q;
    cin >> n >> q;
    vector<ll> nums((1 << n));
    for (ll& num : nums) cin >> num;
    SegmentTree* sg = new SegmentTree(nums);
    loop(_, q) {
        ll idx, val;
        cin >> idx >> val;
        idx--;
        cout << sg->update(idx, val) << nl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
