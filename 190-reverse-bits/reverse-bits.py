class Solution:
    def reverseBits(self, n: int) -> int:
        k=bin(n)[2:]
        k=k.zfill(32)
        res=k[::-1]
        return int(res,2)       