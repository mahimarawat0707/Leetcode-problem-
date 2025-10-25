class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        num &= 0xFFFFFFFF

        hex_chars = "0123456789abcdef"
        res = []

        while num:
            nibble = num & 0xF
            res.append(hex_chars[nibble])
            num >>= 4

        return "".join(reversed(res))
