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
        ll valid = 0;
        ll less = 0;
};

class SegmentTree {
    private:
        vector<Node> st;
        int n;

        int left(int x) { return (x << 1) + 1; }
        int right(int x) { return (x << 1) + 2; }

        void updateHelper(int pos, int index, int l, int r, ll adder) {
            if (l == r) {
                st[pos].less++;
                st[pos].valid += adder;
                return;
            }
            int mid = l + (r - l) / 2;
            if (index <= mid)
                updateHelper(left(pos), index, l, mid, adder);
            else
                updateHelper(right(pos), index, mid + 1, r, adder);
            st[pos].valid = st[left(pos)].valid + st[right(pos)].valid;
            st[pos].less = st[left(pos)].less + st[right(pos)].less;
        }

        Node queryHelper(int pos, int l, int r, int L, int R) {
            if (l > R || r < L) return Node();
            if (L <= l && r <= R) return st[pos];
            int mid = l + (r - l) / 2;
            Node leftNode = queryHelper(left(pos), l, mid, L, R);
            Node rightNode = queryHelper(right(pos), mid + 1, r, L, R);
            Node temp;
            temp.valid = leftNode.valid + rightNode.valid;
            temp.less = leftNode.less + rightNode.less;
            return temp;
        }

    public:
        SegmentTree(int n) {
            this->n = n;
            st.assign(4 * n, Node());
        }

        void update(int index, ll adder) {
            updateHelper(0, index, 0, n - 1, adder);
        }
        Node query(int index) { return queryHelper(0, 0, n - 1, 0, index); }
};

void solve() {
    ll n;
    cin >> n;
    vector<ll> nums(n);
    vector<ll> arr(n);
    loop(i, n) {
        cin >> nums[i];
        arr[i] = nums[i];
    }
    sort(arr.begin(), arr.end());
    unordered_map<ll, ll> index;
    loop(i, n) index[arr[i]] = i;

    ll counter = 0;
    SegmentTree st(n);
    for (int i = n - 1; i >= 0; i--) {
        Node node = st.query(index[nums[i]] - 1);
        counter += node.valid;
        st.update(index[nums[i]], node.less);
    }
    print(counter);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    loop_from(_, 0, t) { solve(); }
}
