class Solution(object):
    def isHappy(self, n: int) -> bool:
        n = str(n)
        nums_encountered = [n]
        while True:
            num = 0
            for i in range(len(n)):
                num += int(n[i]) * int(n[i])
            if str(num).endswith("1"):
                return True
            else:
                n = str(num)
                if n in nums_encountered:
                    return False
                else:
                    nums_encountered.append(n)

def main():
    n = 19
    sol = Solution()
    print(sol.isHappy(n=n))

if __name__ == "__main__":
    main()
            