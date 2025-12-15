import heapq

class Twitter(object):
    def __init__(self):
        self.timestamp = 0
        self.user_tweets = {}
        self.user_follows = {}
    
    def postTweet(self, userId, tweetId):
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))
    
    def getNewsFeed(self, userId):
        heap = []
        if userId in self.user_tweets:
            heap.extend(self.user_tweets[userId][-10:])
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                if followeeId in self.user_tweets:
                    heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed
    
    def follow(self, followerId, followeeId):
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)