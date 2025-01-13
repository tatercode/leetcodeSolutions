from typing import List

# Show how many days it takes to get to higher temp

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]

        stack = []

        for i, num in enumerate(temperatures):
            if not stack:
                stack.append((num, i))
                continue

            while stack and stack[-1][0] < num:
                temp = stack.pop()
                res[temp[1]] = i - temp[1]
            stack.append((num, i))

        return res 

if __name__ == "__main__":
    sol = Solution()

    temperatures = [73,74,75,71,69,72,76,73]

    res = sol.dailyTemperatures(temperatures)

    print(res)
