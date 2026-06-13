class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for w in words:
            x=0
            for c in w:
                x+=weights[ord(c)-97]
            x=x%26
            x=abs(x-26)
            res+=chr(x+97-1)
        return res