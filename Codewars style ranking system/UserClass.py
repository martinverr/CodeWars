class User:
    # class properties by default
    rank = -8
    progress = 0
    # data
    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self, rank=None, progress=None):
        if rank is not None and self.isValidRank(rank):
            self.rank = rank
        if progress is not None and self.isValidProgress(progress):
            self.progress = progress

    def __str__(self):
        return f"Rank: {self.rank}\nProgress: {self.progress}"

    @classmethod
    def isValidRank(cls, rank):
        if rank in User.ranks:
            return True
        else:
            return False

    @staticmethod
    def isValidProgress(progress):
        return True if progress >= 0 and progress <= 100 else False

    def setRank(self, rank):
        if rank is not None and self.isValidRank(rank):
            self.rank = rank
        else:
            raise Exception("Err: in User.setRank(self, rank)"
                            "passed an invalid rank")

    def setProgress(self, progress):
        if progress is not None and self.isValidProgress(progress):
            self.progress = progress
        else:
            raise Exception("Err: in User.setProgress(self, rank)"
                            "passed an invalid progress")

    def getRankDistFrom(self, rank2):
        rank1 = self.rank
        if not self.isValidRank(rank2):
            raise Exception("Err: in getRankDist(self, rank2), rank2 is not a"
                            "valid rank")
        return User.ranks.index(rank2) - User.ranks.index(rank1)

    def calculatePointsFrom(self, rank2):
        dist = self.getRankDistFrom(rank2)
        if dist == 0:
            return 3
        if dist == -1:
            return 1
        if dist < -1:
            return 0
        if dist > 0:
            return dist * dist * 10

    def promotionRanks(self, ranks):
        while ranks > 0:
            nextrank = self.rank + 1
            if self.isValidRank(nextrank):
                self.setRank(nextrank)
            else:  # possibile not valid nextrank
                if self.rank == -1:
                    self.setRank(nextrank + 1)
                elif self.rank == 8:
                    break
                else:
                    raise Exception("Undefined behaviour during promotion")
            ranks -= 1

    def promotionByProgress(self, progress):
        advanceRanks = progress//100
        progressSurplus = progress % 100
        self.promotionRanks(advanceRanks)
        if(self.rank == 8):
            self.setProgress(0)
            return
        self.setProgress(progressSurplus)

    def inc_progress(self, rankActivity):
        if rankActivity is None or not self.isValidRank(rankActivity):
            raise Exception("Err: in inc_progress(self, rankActivity), "
                            "rankActivity is not a valid rank")
        if self.rank == 8:
            return
        totalProgress = self.progress + self.calculatePointsFrom(rankActivity)

        if totalProgress >= 100:  # promotion
            self.promotionByProgress(totalProgress)
        else:  # no promorion
            self.setProgress(totalProgress)
