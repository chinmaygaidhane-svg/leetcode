class Solution(object):
    def reverseList(self, head):
        prev = None

        def nodes(curr):
            while curr:
                nxt = curr.next
                yield curr
                curr = nxt

        for curr in nodes(head):
            curr.next = prev
            prev = curr

        return prev