class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        sub = list(s)
        seq = list(t)

        subLength = len(sub)
        seqLength = len(seq)

        k = 0

        if(subLength == 0):
            return True
        if(seqLength == 0):
            return False
        if(subLength < 0 or subLength > 100 or seqLength < 0 or seqLength > 10000):
            return False

        for l in range(subLength):

            if(k >= seqLength):
                return False
            while(sub[l] != seq[k] and k < (seqLength - 1)):
                k +=1
            if(sub[l] == seq[k]):
                k+=1
            else:
                return False

        return True
