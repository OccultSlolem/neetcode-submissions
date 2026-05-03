class LinkedList:
    
    def __init__(self):
        self.arr = []

    def indexOutOfBounds(self, index) -> bool:
        return index > (len(self.arr) - 1)

    
    def get(self, index: int) -> int:
        if self.indexOutOfBounds(index): return -1
        return self.arr[index]
        

    def insertHead(self, val: int) -> None:
        self.arr.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.arr.append(val)
        

    def remove(self, index: int) -> bool:
        if self.indexOutOfBounds(index): return False
        pre_snip = self.arr[0 : index]
        post_snip = self.arr[index + 1 : len(self.arr)]
        self.arr = pre_snip + post_snip
        return True
        

    def getValues(self) -> List[int]:
        return self.arr
        
