class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(0) for i in range(10**4)] #ListNNode(0) is the dummy node

    def add(self, key: int) -> None:
        index = key%len(self.arr)

        curr = self.arr[index] #curr is currently at our dummy node

        while curr.next:
            #duplicate located
            if curr.next.key == key:
                return
            
            curr = curr.next

        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key%len(self.arr)

        curr = self.arr[index] #curr is currently at our dummy node

        while curr.next:
            #found key
            if curr.next.key == key:
                temp = curr.next.next
                curr.next = temp
                return
            
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = key%len(self.arr)

        curr = self.arr[index] #curr is currently at our dummy node

        while curr.next:
            #found key
            if curr.next.key == key:
                return True
            
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)