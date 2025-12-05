#heap, pq, linked list, design
'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able 
to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): 
    Compose a new tweet.

getNewsFeed(userId): 
    Retrieve the 10 most recent tweet ids
    Each item in the news feed must be posted by users who the user followed or by the user itself
    Tweets must be ordered from most recent.

follow(followerId, followeeId): 
    Follower follows a followee.

unfollow(followerId, followeeId): 
    Follower unfollows a followee.


Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

'''
from collections import defaultdict

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.user_map = defaultdict(set)   # using hashset for o(1) look up
        self.tweet_map = defaultdict(list) # key -> [list]
                
        
    def postTweet(self, userId, tweetId) -> 'None':
        # Compose a new tweet.
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1
        
        

    def getNewsFeed(self, userId: 'int') -> 'List[int]':
        feed = self.tweet_map[userId]
        # not using heap, using sorting instead
        for followeeId in self.user_map[userId]:
            # extend feed to add tweets from other users
            feed.extend(self.tweetMap[followeeId])

        feed.sort(key=lambda x: -x[0])  
        return [tweetId for _, tweetId in feed[:10]]


    def follow(self, followerId: 'int', followeeId: 'int') -> 'None':
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.user_map and followeeId != followerId:
            self.user_map[followeeId].add(followerId)
    

    def unfollow(self, followerId: 'int', followeeId: 'int') -> 'None':
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.user_map:
            if followerId in self.user_map[followeeId]:
                self.user_map[followeeId].remove(followerId)

        


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.postTweet(1, 10); # User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20); # User 2 posts a new tweet with id = 20.
twitter.postTweet(1, 12); # User 1 posts a new tweet with id = 10.
twitter.postTweet(1, 14); # User 1 posts a new tweet with id = 10.
twitter.postTweet(1, 105); # User 1 posts a new tweet with id = 10.
twitter.postTweet(1, 104); # User 1 posts a new tweet with id = 10.
twitter.postTweet(1, 13); # User 1 posts a new tweet with id = 10.
print(twitter.getNewsFeed(1))