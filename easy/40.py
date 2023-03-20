class Solution:
    def backtrack(self, index, candidates, res, target, path):
        if sum(path) == target:
            res.append(path[:])
            return
        if sum(path) > target:
            return 

        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.backtrack(i+1, candidates, res, target, path)
            path.pop()

    def sort(self, cand):
        for i in range(0, len(cand)):
            min = i
            for j in range(i, len(cand)):
                if cand[j] <= cand[min]:
                    min = j
            tmp = cand[i]
            cand[i] = cand[min]
            cand[min] = tmp
            
    def combinationSum2(self, candidates, target):
        path = []
        res = []
        self.sort(candidates)
        self.backtrack(0, candidates, res, target, path)
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
s=Solution()

s.combinationSum2(candidates, target)
