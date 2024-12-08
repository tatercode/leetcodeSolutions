from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                       "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']
                       }
        res = []
        if digits == "":
            return []
        def backtrack(index, combo):
            if len(combo) == len(digits):
                res.append(combo)
                return

            cur_num = letter_dict[digits[index]]
            
            for letter in cur_num:
                backtrack(index+1, combo+letter)

        backtrack(0, "")

        return res

if __name__ == "__main__":
    sol = Solution()
    test = "23"
    res = sol.letterCombinations(test)
    print(res)
