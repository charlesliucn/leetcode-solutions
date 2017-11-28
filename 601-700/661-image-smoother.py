from copy import deepcopy

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        nrow = len(M)
        ncol = len(M[0]) if nrow else 0
        res = deepcopy(M)
        for x in range(nrow):
            for y in range(ncol):
                neighbors = [
                    M[i][j]
                    for i in (x-1, x, x+1)
                    for j in (y-1, y, y+1)
                    if 0 <= i < nrow and 0 <= j < ncol
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res