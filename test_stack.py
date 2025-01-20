import unittest
from stack import Stack



class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()


    def test_push_tolist(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.to_list(), [20, 10])
        self.stack.push(5)
        self.assertEqual(self.stack.to_list(), [5, 20, 10])


    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)    # Test pop with no values

        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)  # Test pop with one value

        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)  # Test pop with multiple values


    def test_peek(self):
        self.assertEqual(self.stack.peek(), None)    # Test peek with no values

        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)  # Test peek with one value

        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)  # Test peek with multiple values


    def test_isempty(self):
        self.assertEqual(self.stack.is_empty(), True)    # Test is_empty with no values

        self.stack.push(10)
        self.assertEqual(self.stack.is_empty(), False)  # Test is_empty with one value

        self.stack.push(20)
        self.assertEqual(self.stack.is_empty(), False)  # Test is_empty with multiple values


    def test_size(self):
        self.assertEqual(self.stack.size(), 0)    # Test size with no values

        self.stack.push(10)
        self.assertEqual(self.stack.size(), 1)  # Test size with one value

        self.stack.push(20)
        self.assertEqual(self.stack.size(), 2)  # Test size with multiple values


    def test_clear(self):
        self.stack.push(10)
        self.stack.clear()
        self.assertEqual(self.stack.to_list(), [])  # Test size with one value

        self.stack.push(20)
        self.stack.push(10)
        self.stack.clear()
        self.assertEqual(self.stack.to_list(), [])  # Test size with multiple values

        self.assertEqual(self.stack.size(), 0) # Ensure clearing also resets stack size


    def test_contains(self):
        self.assertEqual(self.stack.contains(10), False)

        self.stack.push(10)
        self.assertEqual(self.stack.contains(10), True)

        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.contains(20), True)


    def test_iterator1(self): # Testing iterator with no values
        values = []

        for value in self.stack:
            values.append(value)

        self.assertEqual(values, [])

    def test_iterator2(self): # Testing iterator with multiple values
        values = []

        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)


        for value in self.stack:
            values.append(value)

        self.assertEqual(values, [30, 20, 10])




if __name__ == "__main__":
    unittest.main()