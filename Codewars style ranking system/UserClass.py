# TODO:
# MULTIPROMOTION:   fix case of multiple promotion, better if with new
#                   methods. For example, in user.inc_progress() call a
#                   self.promotion(self, points) that manage a promotion

# NOTE: This class works for the basic 5 tests in codewars, but not for the
#       final 200+ random test case (see TODO multipromotion)


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

    def inc_progress(self, rankActivity):
        if rankActivity is None or not self.isValidRank(rankActivity):
            raise Exception("Err: in inc_progress(self, rankActivity), "
                            "rankActivity is not a valid rank")
        totalProgress = self.progress + self.calculatePointsFrom(rankActivity)

        if totalProgress >= 100:  # promotion
            if self.isValidRank(self.rank + 1):
                self.rank += 1
                self.progress = 0
            else:
                if self.rank == -1:
                    self.rank += 2
                    self.progress = 0
                elif self.rank == 8:
                    self.progress = 100
                else:
                    raise Exception("Undefined behaviour during promotion")
        else:  # no promorion
            self.setProgress(totalProgress)
