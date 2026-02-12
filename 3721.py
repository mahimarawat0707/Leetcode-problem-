class segmentTreeNode:
    def __init__(self, maxV = 0, minV = 0, lazyTag = 0):
        self.mx = maxV
        self.mn = minV
        self.tag = lazyTag

class segmentTree:
    def addTag(self, val: int, id: int) -> None:
        self.tree[id].tag += val
        self.tree[id].mx += val
        self.tree[id].mn += val

    def push(self, id: int) -> None:
        val = self.tree[id].tag
        self.addTag(val, 2 * id + 1)
        self.addTag(val, 2 * id + 2)
        self.tree[id].tag = 0

    def pull(self, id: int) -> None:
        self.tree[id].mx = max(self.tree[2 * id + 1].mx, self.tree[2 * id + 2].mx)
        self.tree[id].mn = min(self.tree[2 * id + 1].mn, self.tree[2 * id + 2].mn)

    def build(self, nums: List[int], left: int, right: int, id: int) -> None:
        if left == right:
            self.tree[id].mx = nums[left]
            self.tree[id].mn = nums[left]
            return
        mid = (left + right) >> 1
        self.build(nums, left, mid, 2 * id + 1)
        self.build(nums, mid + 1, right, 2 * id + 2)
        self.pull(id)

    def query(self, l: int, r: int, val: int, left: int, right: int, id: int) -> int:
        if self.tree[id].mx < val or self.tree[id].mn > val:
            return -1
        if left == right:
            return left
        mid = (left + right) >> 1
        self.push(id)
        if r > mid:
            res = self.query(l, r, val, mid + 1, right, 2 * id + 2)
            if res > -1:
                return res
        if l <= mid:
            return self.query(l, r, val, left, mid, 2 * id + 1)
        return -1

    def update(self, l: int, r: int, val: int, left: int, right: int, id: int) -> None:
        if l <= left and right <= r:
            self.addTag(val, id)
            return
        mid = (left + right) >> 1
        self.push(id)
        if l <= mid:
            self.update(l, r, val, left, mid, 2 * id + 1)
        if r > mid:
            self.update(l, r, val, mid + 1, right, 2 * id + 2)
        self.pull(id)
    
    def __init__(self, nums: List[int]):
        self.sz = len(nums)
        self.tree = [segmentTreeNode() for _ in range(4 * self.sz)]
        self.build(nums, 0, self.sz - 1, 0)
    
    def search(self, l: int, r: int, val: int) -> int:
        return self.query(l, r, val, 0, self.sz - 1, 0)

    def modify(self, l: int, r: int, val: int) -> None:
        self.update(l, r, val, 0, self.sz - 1, 0)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        # calculate parity prefix sum
        prefix = [0] * n
        exist = dict()
        for i in range(n):
            prefix[i] += prefix[i - 1]
            if nums[i] not in exist:
                exist[nums[i]] = deque()
                prefix[i] += (1 if nums[i] & 1 else -1)
            exist[nums[i]].append(i)

        for deq in exist.values():
            deq.append(n)

        seg = segmentTree(prefix)
        
        # find maximum length
        maxlen = 0
        for i in range(n):
            if i > 0:
                exist[nums[i - 1]].popleft()
                seg.modify(i - 1, exist[nums[i - 1]][0] - 1, (-1 if nums[i - 1] & 1 else 1))
            if i + maxlen >= n:
                break
            idx = seg.search(i + maxlen, n - 1, 0)
            if idx > -1:
                maxlen = idx - i + 1
        
        return maxlen
