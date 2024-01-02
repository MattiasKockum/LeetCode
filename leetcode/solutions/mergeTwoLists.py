class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node1 = list1
        node2 = list2
        if node1 == None:
            return node2
        if node2 == None:
            return node1
        if node1.val < node2.val:
            head = node1
            tail = node1
            node1 = node1.next
        else:
            head = node2
            tail = node2
            node2 = node2.next
        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next
        if node1 != None:
            tail.next = node1
        else:
            tail.next = node2
        return head
