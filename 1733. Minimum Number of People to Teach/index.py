from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        person_langs = [set(langs) for langs in languages]

        broken = set()
        for u, v in friendships:
            if person_langs[u-1].isdisjoint(person_langs[v-1]):
                broken.add(u-1)
                broken.add(v-1)

        if not broken:
            return 0

        res = float('inf')
        for lang in range(1, n+1):
            cnt = 0
            for person in broken:
                if lang not in person_langs[person]:
                    cnt += 1
            res = min(res, cnt)

        return res
