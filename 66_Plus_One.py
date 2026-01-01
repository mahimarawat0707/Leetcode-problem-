class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsStr = ""
        outList = []
        for element in digits:
            digitsStr += str(element)

        digitsStr = str(int(digitsStr) + 1)

        for element in digitsStr:
            outList.append(int(element))
        
        return outList
