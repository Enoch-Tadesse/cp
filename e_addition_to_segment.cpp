#include <bits/stdc++.h>
using namespace std;

#define loop_from(i, s, n) for (int i = s; i < n; i++)
#define loop(i, n) for (int i = 0; i < n; i++)
#define MOD 1'000'000'007
#define pb push_back()
#define pob pop_back()
#define int long long
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
    return accumulate(v.begin(), v.end(), decltype(*v.begin() + 0)(0));
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

class Segment {
    private:
        vll tree, lazy;
        vll nums;
        ll n;

        void build(ll pos, ll l, ll r) {
            if (l == r) {
                tree[pos] = nums[l];
                return;
            }
            ll mid = l + (r - l) / 2;
            build(left(pos), l, mid);
            build(right(pos), mid + 1, r);
            tree[pos] = tree[left(pos)] + tree[right(pos)];
        }

        void updateHelper(ll pos, ll l, ll r, ll val, ll L, ll R) {
            push(pos, l, r);
            if (l > R || r < L) return;
            if (l >= L && r <= R) {
                lazy[pos] += val;
                push(pos, l, r);
                return;
            }
            ll mid = l + (r - l) / 2;
            updateHelper(left(pos), l, mid, val, L, R);
            updateHelper(right(pos), mid + 1, r, val, L, R);
            tree[pos] = tree[left(pos)] + tree[right(pos)];
        }

        ll queryHelper(ll pos, ll l, ll r, ll L, ll R) {
            push(pos, l, r);
            if (l > R || r < L) return -1;
            if (l >= L && r <= R) return tree[pos];
            ll mid = l + (r - l) / 2;
            ll x = queryHelper(left(pos), l, mid, L, R);
            ll y = queryHelper(right(pos), mid + 1, r, L, R);
            if (x != -1) return x;
            return y;
        }

    public:
        Segment(vll nums) {
            this->nums = nums;
            n = nums.size();
            tree.assign(4 * n, 0);
            lazy.assign(4 * n, 0);
            build(0, 0, n - 1);
        }

        ll left(ll pos) { return (pos << 1) + 1; }
        ll right(ll pos) { return (pos << 1) + 2; }

        void update(ll l, ll r, ll val) {
            updateHelper(0, 0, n - 1, val, l, r);
        }

        ll query(ll idx) { return queryHelper(0, 0, n - 1, idx, idx); }

        void push(ll pos, ll l, ll r) {
            if (lazy[pos] != 0) {
                tree[pos] += lazy[pos] * (r - l + 1);
                if (l < r) {
                    lazy[left(pos)] += lazy[pos];
                    lazy[right(pos)] += lazy[pos];
                }
                lazy[pos] = 0;
            }
        }
};



void solve() {
	ll n, m; cin >> n >> m;
	ll t,l,r,v;
	vll nums(n, 0);
	Segment seg(nums);
	loop(_, m) {
		cin >> t;
		if(t == 1) {
			cin >> l >> r >> v;
			r--;
			seg.update(l, r, v);
		}else {
			cin >> l;
			print(seg.query(l));
		}

	}
}


int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
	
    loop_from(_, 0, t) { solve(); }
}
