class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n=0
        for ch in columnTitle:
            n=n*26+(ord(ch)-64)
        return n
        