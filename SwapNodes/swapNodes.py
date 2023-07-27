
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getListNodes(nums):
    head = ListNode(nums[0])
    curr = head

    for i in range(1, len(nums)):
        nextNode = ListNode(nums[i])
        curr.next = nextNode
        curr = nextNode
    
    return head

def visualizeNode(node):
    val = None
    next = None

    if node is None: return { "val": None, "next": None }
    if node.next is None: return { "val": node.val, "next": None }

    return { "val": node.val, "next": node.next.val }

def printListNodes(listNodes):
    head = listNodes

    while head:
        print(head.val)
        head = head.next

def nodesToList(listNodes):
    head = listNodes

    nodes = []

    while head:
        nodes.append(head.val)
        head = head.next
    
    return nodes


class Solution(object):

    def swapNodes(self, start, middle, end):
        start.next = end
        middle.next = start

    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        pre = ListNode(0)
        secondNode = head.next

        while head and head.next:
            nxt = head.next

            # assign next
            pre.next = nxt
            head.next = nxt.next
            nxt.next = head

            # assign nodes
            pre = head
            head = head.next
        
        return secondNode

listNodes = getListNodes([1,2,3,4,5,6,7,8,9,10])

listNodes = Solution().swapPairs(listNodes)

printListNodes(listNodes)




        