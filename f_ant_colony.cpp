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

class Segment {
    private:
        ll n;
        vll nums;
        vll tree;

        ll left(ll pos) { return (pos << 1) + 1; }
        ll right(ll pos) { return (pos << 1) + 2; }

        void build(ll pos, ll l, ll r) {
            if (l == r) {
                tree[pos] = nums[l];
                return;
            }
            ll mid = l + (r - l) / 2;
            build(left(pos), l, mid);
            build(right(pos), mid + 1, r);
            tree[pos] = gcd(tree[left(pos)], tree[right(pos)]);
        }

        ll getRangeGcd(ll pos, ll l, ll r, ll L, ll R) {
            if (l > R || r < L) return 0LL;
            if (l >= L && r <= R) return tree[pos];

            ll mid = l + (r - l) / 2;
            ll x = getRangeGcd(left(pos), l, mid, L, R);
            ll y = getRangeGcd(right(pos), mid + 1, r, L, R);
            return gcd(x, y);
        }

        ll countRangeGcd(ll pos, ll l, ll r, ll val, ll L, ll R) {
            if (l > R || r < L) return 0LL;
            if (l == r) return (val % nums[l] == 0);
            if (tree[pos] > val) return 0LL;

            ll mid = l + (r - l) / 2;
            ll x = countRangeGcd(left(pos), l, mid, val, L, R);
            ll y = countRangeGcd(right(pos), mid + 1, r, val, L, R);
            return x + y;
        }

    public:
        Segment(vll nums) {
            this->nums = nums;
            n = nums.size();
            tree.assign(4 * n, 0);
            build(0, 0, n - 1);
        }

        ll query(ll l, ll r) { return getRangeGcd(0, 0, n - 1, l, r); }
};

ll count_in_range(const vector<ll>& indices, ll l, ll r) {
    return upper_bound(indices.begin(), indices.end(), r) -
           lower_bound(indices.begin(), indices.end(), l);
}

const int MAX_SIEVE = 1e5;
vector<int> primes;
vector<int> spf(MAX_SIEVE + 1);
void sieve() {
    for (int i = 2; i <= MAX_SIEVE; i++) {
        if (!spf[i]) {
            spf[i] = i;
            primes.push_back(i);
        }
        for (int p : primes) {
            if (p > spf[i] || i * p > MAX_SIEVE) break;
            spf[i * p] = p;
        }
    }
}

vector<ll> get_divisors(ll x) {
    vector<ll> factors;
    for (int p : primes) {
        if ((ll)p * p > x) break;
        if (x % p == 0) {
            factors.push_back(p);
            while (x % p == 0) x /= p;
        }
    }
    if (x > 1) factors.push_back(x);
    return factors;
}

void solve() {
    ll n;
    cin >> n;
    vll nums(n);
    umap<ll, vll> counts;
    ll i = 0;
    for (ll& x : nums) {
        cin >> x;
        counts[x].push_back(i);
        i++;
    }

    Segment seg(nums);

    ll q;
    cin >> q;
    ll l, r;
    loop(_, q) {
        cin >> l >> r;
        l--;
        r--;
        ll gcd_val = seg.query(l, r);
        ll freed = 0;
        for (auto& [num, idxs] : counts) {
            if (gcd_val % num == 0) freed += count_in_range(idxs, l, r);
        }

        print((r - l + 1) - freed);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;

    loop_from(_, 0, t) { solve(); }
}
