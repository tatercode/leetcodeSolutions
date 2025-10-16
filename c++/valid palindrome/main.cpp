#include <iostream>
#include <algorithm>                                                                                                                                     
#include <cctype>

class Solution {
  public:
    bool isValidPalindrome(std::string s) {

      std::string cleanedString = "";

      for (int i = 0; i < s.length(); i++) {
        if (std::isalnum(s[i])) {
          cleanedString.push_back(std::tolower(s[i]));
        }
      }
      int l = 0;
      int r = cleanedString.length() - 1;

      while (l <= r) {
        if (cleanedString[l] != cleanedString[r]) 
          return false;
        l += 1;
        r -= 1;
      }


      return true;
    }
};

class OptimizedSolution {
  public:
    bool isValidPalindrome(std::string s) {
      int l = 0;
      int r = s.length() - 1;

      while (l < r) {
        if (!std::isalnum(s[l])) {
          l += 1;
          continue;
        }
        if (!std::isalnum(s[r])) {
          r -= 1;
          continue;
        }

        if (std::tolower(s[l]) != std::tolower(s[r])) {
          return false;
        }
        l += 1;
        r -= 1;
      }
      return true;
    }
};

int main () {
  std::string s = "Was it a car or a cat I saw?";

  OptimizedSolution sol = OptimizedSolution();
  bool ans = sol.isValidPalindrome(s);
  std::cout << ans << std::endl;

  return 0;
}

