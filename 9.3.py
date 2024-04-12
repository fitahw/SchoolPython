class PowerIterator:
    def __init__(self, maxPower):
        self.maxPower = maxPower
        self.curPower = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curPower > self.maxPower:
            raise StopIteration
        else:
            power = 2 ** self.curPower
            self.curPower += 1
            return power

iterator = PowerIterator(10)
for num in iterator:
    print(num)