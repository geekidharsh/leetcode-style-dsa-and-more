# Design a Leaderboard class, which has 3 functions:

# addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
# top(K): Return the score sum of the top K players.
# reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

# approach: 
# using a simple sorted approach to get top k scores
# can also be solved by heap to better optimize by using a priority queue for top k

class Leaderboard:

    def __init__(self):
        self.scoreboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scoreboard:
            self.scoreboard[playerId] = 0
        self.scoreboard[playerId] += score


    def top(self, K: int) -> int:
        all_scores = list(self.scoreboard.values())
        all_scores.sort(reverse=True)
        topK = 0
        for i in range(0, K):
            topK += all_scores[i]
        return topK

    def reset(self, playerId: int) -> None:
        del self.scoreboard[playerId]



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)