class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode(0,-1) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key%len(self.arr)
        curr = self.arr[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            
            curr = curr.next

        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key%len(self.arr)
        curr = self.arr[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        index = key%len(self.arr)
        curr = self.arr[index]

        while curr.next:
            if curr.next.key == key:
                temp = curr.next.next
                curr.next = temp
                return
            
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)