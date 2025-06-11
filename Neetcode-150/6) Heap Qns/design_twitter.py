# Design Twitter
# Overall Time Complexity:
# - postTweet: O(log n)
# - getNewsFeed: O(n log n)
# - follow/unfollow: O(1)
# Overall Space Complexity: O(u + t), where u = number of users, t = number of tweets
# Hint: Use a global max-heap to store all tweets with timestamps and track follows using a dictionary of sets

import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)  
        self.heap = []                   
        self.time = 0                    

    def postTweet(self, userId, tweetId) -> None:
        self.follows[userId].add(userId)                        
        heapq.heappush(self.heap, (-self.time, userId, tweetId))  
        self.time += 1

    def getNewsFeed(self, userId):
        feed = []
        temp = []
        i = 0
        while self.heap and i < 10:                      
            tweet = heapq.heappop(self.heap)            
            temp.append(tweet)
            if tweet[1] in self.follows[userId]:        
                feed.append(tweet[2])
                i += 1
        for tweet in temp:                               
            heapq.heappush(self.heap, tweet)            
        return feed

    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)         

    def unfollow(self, followerId, followeeId):
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId) 

# Time Complexity:
# - postTweet: 
#   - Add to set: O(1)
#   - Heap push: O(log n), where n is total tweets
# - getNewsFeed:
#   - Worst-case: O(n log n) if all tweets are scanned (inefficient)
#   - Practical with <= 10 tweets fetched: O(n), where n is number of tweets in heap
# - follow/unfollow: O(1)
# Space Complexity:
# - follows: O(N * M), where N is number of users and M is number of follow relationships
# - heap: O(n), where n is total number of tweets
# - Total: O(N * M + n)
