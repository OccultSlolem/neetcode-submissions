class MinStack:

    def __init__(self):
        self.arr = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        if val < self.min: self.min = val
        self.arr.append(val)
        

    def pop(self) -> None:
        value = self.arr.pop()
        if value == self.min:
            if not self.arr:
                self.min = float("inf")
                return
            self.min = sorted(self.arr)[0]
        

    def top(self) -> int:
        return self.arr[-1] if self.arr else None
        

    def getMin(self) -> int:
        return self.min
        
