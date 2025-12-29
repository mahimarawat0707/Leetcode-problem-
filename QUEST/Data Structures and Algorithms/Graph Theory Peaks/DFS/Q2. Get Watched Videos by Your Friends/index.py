from typing import List
from collections import defaultdict, deque


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int
    ) -> List[str]:

        videos = defaultdict(int)
        q = deque([id])
        visited = set([id])

        while level > 0:
            for _ in range(len(q)):
                person = q.popleft()

                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        q.append(friend)

                        if level == 1:
                            for vid in watchedVideos[friend]:
                                videos[vid] += 1

            level -= 1

        return sorted(videos.keys(), key=lambda k: (videos[k], k))
