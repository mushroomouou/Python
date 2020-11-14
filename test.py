class Solution:
    def myAtoi(self, s: str) -> int:
        result: int = 1
        eleindex: int = 0
        s = s.lstrip()
        if s == "":
            return 0
        if s[0] == "-" and len(s) != 1:
            result = -result
            s = s[1:]
        if not s[0].isdigit():
            return 0
        for elem in s:
            if not elem.isdigit():
                break
            eleindex += 1
        result = result * int(s[:eleindex])
        if result < -(2 ** 31):
            return -(2 ** 31)
        if result > (2 ** 31 - 1):
            return 2 ** 31 - 1

        return result
sul = Solution()
print("结果是:{}".format(sul.myAtoi(s="-42")))