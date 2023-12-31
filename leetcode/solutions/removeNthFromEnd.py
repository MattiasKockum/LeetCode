class Solution(object):
    def removeNthFromEnd(self, head, n):
        node = head
        l = 1  # len >= 1
        while node.next != None:
            l += 1
            node = node.next
        node = head
        if l == n:
            head = head.next
        else:
            for _ in range(l - n - 1):
                node = node.next
            node.next = node.next.next
        return head
