class Counter:
    def __init__(self, min: int, max: int):
        self.Min = min
        self.Max = max
    def __str__(self):
        return  f"Min: {self.Min}\nMax: {self.Max}"
    def __iter__(self):
        self.Min = 0
        return self.Min
    def __next__(self):
        self.Min += 1
        if self.Min > self.Max:
            raise StopIteration
        return self