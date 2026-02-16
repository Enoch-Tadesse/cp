#include <bits/stdc++.h>

#include <set>
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

umap<ll, ll> par;

int find(int x) {
    if (par[x] != x) par[x] = find(par[x]);
    return par[x];
};

bool uni_merge(int x, int y) {
    int px = find(x);
    int py = find(y);
    if (px == py) return false;
    par[px] = py;
    return true;
};

vector<pair<ll, ll>> output;

vector<int> merge_array(const vector<int>& left, const vector<int>& right) {
    vector<int> ans;
    ans.reserve(left.size() + right.size());

    int i = 0, j = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            if (uni_merge(left[i], right[j]))
                output.push_back({left[i], right[j]});
            ans.push_back(left[i++]);
        } else {
            if (!left.empty() && left[0] < right[j]) {
                if (!left.empty() && uni_merge(left[0], right[j]))
                    output.push_back({left[0], right[j]});
            }
            ans.push_back(right[j++]);
        }
    }

    while (i < (int)left.size()) ans.push_back(left[i++]);

    while (j < (int)right.size()) {
        if (!left.empty() && left[0] < right[j]) {
            if (!left.empty() && uni_merge(left[0], right[j]))
                output.push_back({left[0], right[j]});
        }
        ans.push_back(right[j++]);
    }

    return ans;
}

vector<int> merge_sort(const vector<int>& arr, int l, int r) {
    if (l == r) return {arr[l]};

    int mid = (l + r) / 2;
    vector<int> left = merge_sort(arr, l, mid);
    vector<int> right = merge_sort(arr, mid + 1, r);

    return merge_array(left, right);
}

void solve() {
    ll n;
    cin >> n;
    vector<int> nums(n);
    par.clear();
    output.clear();
    for (int& x : nums) {
        cin >> x;
    }
    for (int i = 1; i < n + 1; i++) par[i] = i;
    vector<int> test = merge_sort(nums, 0, n - 1);
    set<ll> verdict;
    for (int i = 1; i < n + 1; i++) {
        verdict.insert(find(i));
    }
    if (verdict.size() > 1) {
        print("NO");
        return;
    }
    print("YES");
    for (auto& [a, b] : output) {
        cout << a << " " << b << nl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    loop_from(_, 0, t) { solve(); }
}
