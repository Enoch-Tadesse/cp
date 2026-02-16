#include <bits/stdc++.h>

#include <algorithm>
#include <climits>
#include <utility>
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

ll calculate(vector<ll>& nums) {
    ll n = nums.size();
    vector<ll> pre = {0};
    for (int i = 0; i < n; i++) {
        pre.push_back(max(pre[pre.size() - 1], nums[i]));
    }
    vector<ll> suf = {LLONG_MAX};
    for (int i = n - 1; i >= 0; i--) {
        suf.push_back(min(suf[suf.size() - 1], nums[i]));
    }
    reverse(all(suf));
    ll counter = 0;
    for (int i = 0; i <= n - 1; i++) {
        counter += int(pre[i] < nums[i] && nums[i] < suf[i + 1]);
    }
    return counter;
}

void solve() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; i++) cin >> p[i];

    vector<int> pref_max(n), suf_min(n);
    pref_max[0] = p[0];
    for (int i = 1; i < n; i++) pref_max[i] = max(pref_max[i-1], p[i]);
    suf_min[n-1] = p[n-1];
    for (int i = n-2; i >= 0; i--) suf_min[i] = min(suf_min[i+1], p[i]);

    auto good_count = [&](const vector<int>& arr) -> int {
        int cnt = 0;
        int n = arr.size();
        int cur_max = INT_MIN;
        vector<int> suf_min(n+1, INT_MAX);
        for (int i = n-1; i >= 0; i--) suf_min[i] = min(suf_min[i+1], arr[i]);
		for (int i = 0; i < n; i++) {
            if (cur_max < arr[i] && arr[i] < suf_min[i+1]) cnt++;
            cur_max = max(cur_max, arr[i]);
        }
        return cnt;
    };

    int max_f = 0;

    // check if already sorted
    bool sorted = true;
    for (int i = 1; i < n; i++) if (p[i] < p[i-1]) sorted = false;
    if (sorted) {
        cout << n - 2 << '\n';
        return;
    }

    // initial bad indices
    vector<int> bad;
    int cur_max = INT_MIN;
    for (int i = 0; i < n; i++) {
        int right_min = (i == n-1 ? INT_MAX : suf_min[i+1]);
        if (!(cur_max < p[i] && p[i] < right_min)) bad.push_back(i);
        cur_max = max(cur_max, p[i]);
    }

    max_f = 0;
    vector<int> candidates = bad;
    for (int idx : bad) {
        if (idx > 0) candidates.push_back(idx-1);
        if (idx < n-1) candidates.push_back(idx+1);
    }

    sort(candidates.begin(), candidates.end());
    candidates.erase(unique(candidates.begin(), candidates.end()), candidates.end());

    for (int i : candidates) {
        for (int j : candidates) {
            if (i >= j) continue;
            swap(p[i], p[j]);
            max_f = max(max_f, good_count(p));
            swap(p[i], p[j]);
        }
    }

    cout << max_f << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    cin >> t;
    loop_from(_, 0, t) { solve(); }
}
