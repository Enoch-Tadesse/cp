#include <bits/stdc++.h>

#include <algorithm>
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

class SegmentTree {
    private:
        vector<ll> st;
        int n;

        int left(int x) { return (x << 1) + 1; }
        int right(int x) { return (x << 1) + 2; }

        void updateHelper(int pos, int index, int l, int r) {
            if (l == r) {
                st[pos]++;
                return;
            }
            int mid = l + (r - l) / 2;
            if (index <= mid)
                updateHelper(left(pos), index, l, mid);
            else
                updateHelper(right(pos), index, mid + 1, r);

            st[pos] = st[left(pos)] + st[right(pos)];
        }

        ll queryHelper(int pos, int l, int r, int L, int R) {
            if (l > R || r < L) return 0;
            if (l >= L && r <= R) return st[pos];
            int mid = l + (r - l) / 2;
            return queryHelper(left(pos), l, mid, L, R) +
                   queryHelper(right(pos), mid + 1, r, L, R);
        }

    public:
        SegmentTree(int n) {
            this->n = n;
            st.assign(4 * n, 0);
        }

        void update(int index) { updateHelper(0, index, 0, n - 1); }
        ll query(int index) { return queryHelper(0, 0, n - 1, 0, index); }
};

void solve() {
    ll n;
    cin >> n;
    unordered_set<ll> nums;
    ll l, r;

    vector<pair<ll, ll>> swaps;
    for (int i = 0; i < n; i++) {
        cin >> l >> r;
        nums.insert(l);
        nums.insert(r);
        swaps.push_back({l, r});
    };

    vector<ll> arr(nums.begin(), nums.end());
    sort(arr.begin(), arr.end());
    unordered_map<ll, ll> index;
    for (int i = 0; i < arr.size(); i++) index[arr[i]] = i;

    for (auto& [l, r] : swaps) {
        ll temp = arr[index[l]];
        arr[index[l]] = arr[index[r]];
        arr[index[r]] = temp;
    }

    show(arr);
    reverse(arr.begin(), arr.end());
    // SegmentTree* sg = new SegmentTree(arr.size());
    SegmentTree sg(arr.size());
    ll counter = 0;
    for (int i = 0; i < arr.size(); i++) {
        counter += sg.query(index[arr[i]] - 1);
        print(sg.query(index[arr[i]] - 1));
        sg.update(index[arr[i]]);
    }
    print(counter);
    // 2 4 3 1
    // 1 3 2 4
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
