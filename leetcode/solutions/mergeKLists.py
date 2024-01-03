class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        nodes = [l for l in lists]
        min_index = min(range(len(nodes)),
                        key=lambda i: nodes[i].val
                        if nodes[i] != None
                        else 100000)
        head = nodes[min_index]
        tail = nodes[min_index]
        if head == None:
            return head
        nodes[min_index] = nodes[min_index].next
        if nodes[min_index] == None:
            nodes.pop(min_index)
        while nodes != len(nodes) * [None]:
            min_index = min(range(len(nodes)),
                            key=lambda i: nodes[i].val
                            if nodes[i] != None
                            else 100000)
            tail.next = nodes[min_index]
            tail = tail.next
            nodes[min_index] = nodes[min_index].next
            if nodes[min_index] == None:
                nodes.pop(min_index)
        return head
