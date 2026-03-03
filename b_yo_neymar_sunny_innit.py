
#include <bits/stdc++.h>

#include <cstdint>
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
            tree[p].val = min(tree[left(p)].val, tree[right(p)].val);
        }

        ll queryRange(int p, int l, int r, int L, int R) {
            if (l > R || r < L) return LLONG_MAX;
            if (L <= l && r <= R) return tree[p].val;
            int mid = l + (r - l) / 2;
            return min(queryRange(left(p), l, mid, L, R),
                       queryRange(right(p), mid + 1, r, L, R));
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
            tree[p].val = min(tree[left(p)].val, tree[right(p)].val);
        }

    public:
        SegmentTree(const vl& a)
            : nums(a) {
            n = nums.size();
            tree.assign(4 * n, Node());
            build(0, 0, n - 1);
        }

        ll query(int L, int R) { return queryRange(0, 0, n - 1, L, R); }
        void updatePoint(int idx, ll val) {
            updatePoint(0, 0, n - 1, idx, val);
        }
};

int getLeft(int p, int vl, SegmentTree& seg) {
    if (p <= 0) return -1;
    if (seg.query(0, p - 1) > vl) return -1;
    int l = 0, r = p;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        if (seg.query(mid, p - 1) > vl)
            r = mid;
        else
            l = mid;
    }
    return l;
}

int getRight(int p, int vl, int n, SegmentTree& seg) {
    if (p >= n - 1) return n;
    if (seg.query(p + 1, n - 1) > vl) return n;
    int l = p, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r + 1) / 2;
        if (seg.query(p + 1, mid) > vl)
            l = mid;
        else
            r = mid;
    }
    return r;
}

int32_t main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        ll n;
        cin >> n;
        vl nums(n);
        for (int i = 0; i < n; i++) cin >> nums[i];

        SegmentTree seg(nums);
        vl ans(n + 2, 0), ans2(n + 2, 0);

        for (int i = 0; i < n; i++) {
            ll l1 = getLeft(i, nums[i], seg);
            ll r1 = getRight(i, nums[i], n, seg);

            ll x = (i - l1) * (r1 - i) * nums[i];

            if (l1 >= 0) ans[0] += x, ans[l1] -= x;
            if (r1 < n) ans[r1 + 1] += x, ans[n] -= x;

            x = (i - l1 - 1) * (r1 - i) * nums[i];
            if (l1 + 1 <= i) ans[l1 + 1] += x, ans[i] -= x;

            x = (i - l1) * (r1 - i - 1) * nums[i];
            if (i + 1 <= r1) ans[i + 1] += x, ans[r1] -= x;

            if (l1 >= 0) {
                ll l2 = getLeft(l1, nums[i], seg);
                ans2[l1] += 1LL * (i - l2 - 1) * (r1 - i) * nums[i];
            }
            if (r1 < n) {
                ll r2 = getRight(r1, nums[i], n, seg);
                ans2[r1] += 1LL * (i - l1) * (r2 - i - 1) * nums[i];
            }
        }

        for (int i = 0; i < n; i++) ans[i + 1] += ans[i];

        for (int i = 0; i < n; i++) cout << ans[i] + ans2[i] << " ";
        cout << "\n";
    }

    return 0;
}
