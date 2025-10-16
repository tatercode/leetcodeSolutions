#include <iostream>
#include "../datastructs/linkedList/linkedList.cpp"

class Solution {
  public:
    LinkedList::ListNode* reverseList(LinkedList::ListNode* head) {
      using ListNode = LinkedList::ListNode;

      ListNode* tmp = nullptr;
      ListNode* prev = nullptr;
      ListNode* cur = head;

      while (cur != nullptr) {
        tmp = cur->next;
        cur->next = prev;
        prev = cur;
        cur = tmp;
      }

      return prev;
    }
};

void printList(LinkedList::ListNode* head) {
  LinkedList::ListNode* current = head;
    std::cout << "List: ";
    while (current != nullptr) {
        std::cout << current->val << " -> ";
        current = current->next;
    }
    std::cout << "nullptr" << std::endl;
}

int main () {
  // Create an instance of our LinkedList.
  LinkedList myList;

  myList.append(10);
  myList.append(20);
  myList.append(30);
  myList.append(5);
  myList.append(200);

  printList(myList.head);

  Solution sol = Solution();

  LinkedList::ListNode* newHead = sol.reverseList(myList.head);
  std::cout << "After reversing list" << std::endl;

  printList(newHead);


  return 0;
}
