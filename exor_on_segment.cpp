#include <bits/stdc++.h>

#include <array>
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

class Segment {
    private:
        vll lazy;
        vector<array<ll, 30>> tree;
        vll nums;
        ll n;

        void build(ll pos, ll l, ll r) {
            if (l == r) {
                for (int b = 0; b < 30; ++b) tree[pos][b] = (nums[l] >> b) & 1;
                return;
            }
            ll mid = l + (r - l) / 2;
            build(left(pos), l, mid);
            build(right(pos), mid + 1, r);
            pull(pos);
        }

        void push(int pos, int l, int r) {
            if (lazy[pos] != 0) {
                int len = r - l + 1;
                for (int b = 0; b < 30; b++) {
                    if ((lazy[pos] >> b) & 1) {
                        tree[pos][b] = len - tree[pos][b];
                    }
                }
                if (l < r) {
                    lazy[left(pos)] ^= lazy[pos];
                    lazy[right(pos)] ^= lazy[pos];
                }
                lazy[pos] = 0;
            }
        }

        void pull(ll pos) {
            for (int b = 0; b < 30; b++) {
                tree[pos][b] = tree[left(pos)][b] + tree[right(pos)][b];
            }
        }

        void updateHelper(ll pos, ll l, ll r, ll val, ll L, ll R) {
            push(pos, l, r);
            if (l > R || r < L) return;
            if (l >= L && r <= R) {
                lazy[pos] ^= val;
                push(pos, l, r);
                return;
            }
            ll mid = l + (r - l) / 2;
            updateHelper(left(pos), l, mid, val, L, R);
            updateHelper(right(pos), mid + 1, r, val, L, R);
            pull(pos);
        }

        ll queryHelper(ll pos, ll l, ll r, ll L, ll R) {
            push(pos, l, r);
            if (l > R || r < L) return 0;
            if (l >= L && r <= R) {
                ll res = 0;
                for (int i = 0; i < 30; i++) {
                    res += tree[pos][i] * (1LL << i);
                }
                return res;
            }
            ll mid = l + (r - l) / 2;
            ll x = queryHelper(left(pos), l, mid, L, R);
            ll y = queryHelper(right(pos), mid + 1, r, L, R);
            return x + y;
        }

    public:
        Segment(vll nums) {
            this->nums = nums;
            n = nums.size();
            tree.assign(4 * n, array<ll, 30>{});
            lazy.assign(4 * n, 0);
            build(0, 0, n - 1);
        }

        ll left(ll pos) { return (pos << 1) + 1; }
        ll right(ll pos) { return (pos << 1) + 2; }

        void update(ll l, ll r, ll val) {
            updateHelper(0, 0, n - 1, val, l, r);
        }

        ll query(ll l, ll r) { return queryHelper(0, 0, n - 1, l, r); }
};

void solve() {
    ll n;
    cin >> n;
    vll nums(n);
    for (ll& x : nums) cin >> x;
    ll q;
    cin >> q;

    Segment seg(nums);

    loop(_, q) {
        ll t;
        cin >> t;
        if (t == 1) {
            ll l, r;
            cin >> l >> r;
            cout << seg.query(l - 1, r - 1) << nl;
        } else {
            ll l, r, x;
            cin >> l >> r >> x;
            seg.update(l - 1, r - 1, x);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    loop_from(_, 0, t) { solve(); }
}
