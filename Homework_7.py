class PowerIterable:
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit

    def __iter__(self):
        def generator():
            for i in range(self.limit):
                yield self.number ** i
        return generator()

powers = PowerIterable(2, 5)

for val in powers:
    print(val)