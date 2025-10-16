// Defines a class for a singly-linked list.
class LinkedList {
  public:
    struct ListNode {
        int val; 
        ListNode *next; 
        ListNode() : val(0), next(nullptr) {}
        ListNode(int x) : val(x), next(nullptr) {}
        ListNode(int x, ListNode *next) : val(x), next(next) {}
    };
    ListNode* head;

    LinkedList() : head(nullptr) {};

    void append(int val) {
      ListNode* node = new ListNode(val);

      if (head == nullptr) {
        head = node;
        return;
      }
      ListNode* tmp = head;
      
      while (tmp->next != nullptr) {
        tmp = tmp->next;
      }

      tmp->next = node;
      return;
    };
};
