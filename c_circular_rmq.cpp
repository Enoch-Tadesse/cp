#include <bits/stdc++.h>
using namespace std;

struct Segment {
    int n;
    vector<long long> tree, lazy;
    Segment(const vector<int>& nums) {
        n = nums.size();
        tree.assign(4*n, LLONG_MAX);
        lazy.assign(4*n, 0);
        build(0, 0, n-1, nums);
    }
    void build(int pos, int l, int r, const vector<int>& nums) {
        if (l == r) {
            tree[pos] = nums[l];
            return;
        }
        int mid = (l+r)/2;
        build(pos*2+1, l, mid, nums);
        build(pos*2+2, mid+1, r, nums);
        tree[pos] = min(tree[pos*2+1], tree[pos*2+2]);
    }
    void push(int pos, int l, int r) {
        if (lazy[pos] != 0) {
            tree[pos] += lazy[pos];
            if (l != r) {
                lazy[pos*2+1] += lazy[pos];
                lazy[pos*2+2] += lazy[pos];
            }
            lazy[pos] = 0;
        }
    }
    void update(int pos, int l, int r, int L, int R, long long val) {
        push(pos, l, r);
        if (r < L || l > R) return;
        if (l >= L && r <= R) {
            lazy[pos] += val;
            push(pos, l, r);
            return;
        }
        int mid = (l+r)/2;
        update(pos*2+1, l, mid, L, R, val);
        update(pos*2+2, mid+1, r, L, R, val);
        tree[pos] = min(tree[pos*2+1], tree[pos*2+2]);
    }
    long long query(int pos, int l, int r, int L, int R) {
        push(pos, l, r);
        if (r < L || l > R) return LLONG_MAX;
        if (l >= L && r <= R) return tree[pos];
        int mid = (l+r)/2;
        return min(query(pos*2+1, l, mid, L, R), query(pos*2+2, mid+1, r, L, R));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i=0;i<n;i++) cin >> nums[i];
    int m;
    cin >> m;
    Segment seg(nums);
    while (m--) {
        vector<long long> op;
        string line;
        getline(cin >> ws, line);
        stringstream ss(line);
        long long x;
        while (ss >> x) op.push_back(x);
        int l = op[0], r = op[1];
        if (op.size() == 3) {
            long long val = op[2];
            if (l <= r) seg.update(0, 0, n-1, l, r, val);
            else {
                seg.update(0, 0, n-1, l, n-1, val);
                seg.update(0, 0, n-1, 0, r, val);
            }
        } else {
            if (l <= r) cout << seg.query(0, 0, n-1, l, r) << "\n";
            else cout << min(seg.query(0, 0, n-1, l, n-1), seg.query(0, 0, n-1, 0, r)) << "\n";
        }
    }
}
