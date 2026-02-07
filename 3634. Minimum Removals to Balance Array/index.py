#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        int ans = 0;

        for (int i = 0; i < n; i++) {
            long long max_val = min(2000000000LL, 1LL * k * nums[i]);

            int j = upper_bound(nums.begin(), nums.end(), max_val) - nums.begin();
            j--;  // move to last valid index

            ans = max(ans, j - i + 1);
        }

        return n - ans;
    }
};
