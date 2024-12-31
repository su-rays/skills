class CountDown:
    """Iterator that counts down from a given number."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        '''Returns the iterator object itself.'''
        return self
    
    def __next__(self):
        '''Returns the next value in the countdown.'''
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration

    
for num in CountDown(5):
    print(num)
        
