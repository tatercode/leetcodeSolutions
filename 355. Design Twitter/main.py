from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.posted = 0
        self.posts = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posted -= 1
        if userId in self.posts:
            self.posts[userId].append([tweetId, self.posted])
        else:
            self.posts[userId] = [[tweetId, self.posted]]

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        if userId not in self.follows:
            self.follows[userId] = set()

        self.follows[userId].add(userId)

        for followeeId in self.follows[userId]:
            if followeeId in self.posts:
                index = len(self.posts[followeeId]) - 1
                tweetId, count = self.posts[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                # Push that next post from following
                tweetId, count = self.posts[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set()
            self.follows[followerId].add(followeeId)
        
        print(self.follows)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId in self.follows and followeeId 
            in self.follows[followerId]):
            self.follows[followerId].remove(followeeId)

def main():
    twit = Twitter()
    func_list = ["Twitter", "postTweet", "getNewsFeed", "follow",
                "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    ids = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    ans:List = [None]
    for i in range(1, len(func_list)):
        if func_list[i] == "postTweet":
            twit.postTweet(ids[i][0], ids[i][1])
            ans.append(None)
        elif func_list[i] == "getNewsFeed":
            heap = twit.getNewsFeed(ids[i][0])
            ans.append(heap)
        elif func_list[i] == "follow":
            twit.follow(ids[i][0], ids[i][1])
            ans.append(None)
        else:
            twit.unfollow(ids[i][0], ids[i][1])
            ans.append(None)

    print(ans)

if __name__ == "__main__":
    main()
