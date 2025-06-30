class RingBuffer:
    def __init__(self, size):
        self._size = size
        self._buffer = [None] * size
        self._head = 0
        self._count = 0

    def read(self):
        return self._buffer
    
    def append(self, item):
        self._buffer[self._head] = item
        self._head = (self._head + 1) % self._size # Wraparound
        if self._count < self._size:
            self._count += 1 # Legger til +1 hvis bufferen ikke er full

    def __iter__(self):
        start = (self._head - self._count) % self._size # negativ % gir alltid positivt tall i python, så dette gir oss riktig startpunkt
        for i in range(self._count):
            yield self._buffer[(start + i) % self._size] # Wraparound for riktig rekkefølge. Eldst til nyest.
            

import unittest

class TestRingBuffer(unittest.TestCase):
    def test_wraparound(self):
        buffer = RingBuffer(5)
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)
        buffer.append(4)
        buffer.append(5)

        # Buffer should be full now
        self.assertEqual(buffer.read(), [1, 2, 3, 4, 5])

        buffer.append(6) # Overwrites the oldest element (1)
        elements = buffer.read()
        self.assertEqual(elements, [6, 2, 3, 4, 5])

        buffer.append(7) # Overwrites the next oldest element (2)
        elements = buffer.read()
        self.assertEqual(elements, [6, 7, 3, 4, 5])

        buffer.append(8) # Overwrites the next oldest element (3)
        elements = buffer.read()
        self.assertEqual(elements, [6, 7, 8, 4, 5])

        buffer.append(9) # Overwrites the next oldest element (4)
        elements = buffer.read()
        self.assertEqual(elements, [6, 7, 8, 9, 5])

        buffer.append(10) # Overwrites the next oldest element (5)
        elements = buffer.read()
        self.assertEqual(elements, [6, 7, 8, 9, 10])

    def test_iteration(self):
        buffer = RingBuffer(5)
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)
        buffer.append(4)
        buffer.append(5)

        # Test iteration over buffer
        elements = [item for item in buffer] # Uses __iter__ method
        self.assertEqual(elements, [1, 2, 3, 4, 5])

        buffer.append(6) # Overwrites the oldest element (1)
        elements = [item for item in buffer]
        self.assertEqual(elements, [2, 3, 4, 5, 6])

        buffer.append(7) # Overwrites the next oldest element (2)
        elements = [item for item in buffer]
        self.assertEqual(elements, [3, 4, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()


