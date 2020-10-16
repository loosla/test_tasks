# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SLinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, val):
        new_node = ListNode(val)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, val):
        new_node = ListNode(val)
        n = self.head
        if n:
            while n.next != None:
                n = n.next
            n.next = new_node
        else:
            self.head = new_node

    def add_after_elem(self, elem, val):
        new_node = ListNode(val)
        n = self.head
        if n:
            while n.next != None:
                n = n.next
                if n.val == elem:
                    new_node.next = n.next
                    n.next = new_node

    def traverse_list(self):
        if self.head:
            print(self.head.val)
            n = self.head.next
            while n != None:
                print(n.val)
                n = n.next
        else:
            print("List is empty.")


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_int = self.make_int_from_singly_linked_list(l1)
        l2_int = self.make_int_from_singly_linked_list(l2)
        res = l1_int + l2_int
        res_list = self.make_singly_linked_list_from_int(res)
        return res_list

    def make_int_from_singly_linked_list(self, l: ListNode):
        l_arr = []
        if l.head:
            noda = l.head
            while noda.next != None:
                l_arr.insert(0, str(noda.val))
                noda = noda.next
            l_arr.insert(0, str(noda.val))
        l_int = ''.join(l_arr)
        l_int = int(l_int)
        return l_int

    def make_singly_linked_list_from_int(self, val):
        res_list = SLinkedList()
        val_arr = [int(v) for v in str(val)]

        for digit in val_arr:
            new_node = ListNode(digit)
            if res_list.head == None:
                res_list.head = new_node
            else:
                n = res_list.head
                while n.next != None:
                    n = n.next
                n.next = new_node
        return res_list

    def traverse_list(self):
        if self.head:
            print(self.head.val)
            n = self.head.next
            while n != None:
                print(n.val)
                n = n.next
        else:
            print("List is empty.")
