# Stack Data Structure in Python

A simple implementation of a stack data structure using linked nodes in Python.  
This project demonstrates basic data structure implementation, iterator support,  
and unit testing using `unittest`.

---

## Overview

The `Stack` class provides a basic implementation of a stack with a variety of operations:

- **Pushing and popping values**  
- **Peeking at the top value**  
- **Checking if the stack is empty**  
- **Getting the size of the stack**  
- **Clearing all values**  
- **Checking if a value exists in the stack**  
- **Converting the stack to a list**  

Additionally, the stack is iterable, allowing traversal through its elements  
from top to bottom using Python's `for` loop.

Each operation is tested with comprehensive unit tests to ensure correct  
functionality and proper error handling.

---

## Installation

 **Clone the Repository**  
   bash
   git clone https://github.com/superspartan6/stack.git
   cd stack

---

## Usage

Below is an example script demonstrating how to use the `Stack` class in your Python projects.

```python
from stack import Stack

# Create an instance of Stack
stack = Stack()

# Push values onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Peek at the top value without removing it
print(stack.peek())  # Expected Output: 30

# Check the size of the stack
print(stack.size())  # Expected Output: 3

# Pop values from the stack
print(stack.pop())   # Expected Output: 30
print(stack.pop())   # Expected Output: 20

# Check if the stack contains a value
print(stack.contains(10))  # Expected Output: True

# Convert the stack to a list
print(stack.to_list())  # Expected Output: [10]

# Iterate through the stack
for value in stack:
    print(value)
```

---

## Features

### Core Operations
- **Push Value:** `push(value)`  
  *Adds a value to the top of the stack.*
- **Pop Value:** `pop()`  
  *Removes and returns the value at the top of the stack.*
- **Peek at Top Value:** `peek()`  
  *Returns the top value without removing it.*
- **Check if Empty:** `is_empty()`  
  *Returns `True` if the stack is empty, `False` otherwise.*
- **Get Size:** `size()`  
  *Returns the total number of elements in the stack.*
- **Clear Stack:** `clear()`  
  *Removes all elements from the stack.*

### Additional Features
- **Check for Value:** `contains(value)`  
  *Checks if the stack contains the specified value.*
- **Convert to List:** `to_list()`  
  *Returns a standard Python list representation of the stack.*
- **Iterator Support:**  
  Implements the iterator protocol, allowing easy traversal through the stack elements.

### Unit Testing
Comprehensive tests using Python’s built-in `unittest` framework ensure all operations behave as expected. The test suite covers:

- Basic operations (push, pop, peek, is_empty, size, etc.)
- Edge cases (e.g., popping/peeking from an empty stack)
- Iteration functionality

---

## Unit Testing

This project includes comprehensive unit tests written using Python's built-in `unittest` framework. The tests cover all core and additional features of the stack, including edge cases and iterator functionality.

### Running the Tests
To run the tests, navigate to the project directory and execute the following command:
bash
python -m unittest discover

Test Coverage
The test suite verifies the following functionality:

- Push Operation: Ensures values are added correctly to the stack.
- Pop Operation: Tests value removal, including edge cases like popping from an empty stack.
- Peek Operation: Confirms the top value is returned without modification to the stack.
- Is Empty Check: Validates the behavior for both empty and non-empty stacks.
- Size Check: Verifies the reported size matches the actual number of elements.
- Clear Operation: Ensures all elements are removed and the stack is reset.
- Contains Check: Tests whether a specified value exists in the stack.
- To List Conversion: Confirms that the stack is correctly converted to a Python list.
- Iterator Functionality: Validates that the stack is iterable, yielding elements from top to bottom.



---

## Contact

For questions, suggestions, or feedback, feel free to reach out via one of the following methods:

- **Email:** [caleb.zierenberg@gmail.com](mailto:caleb.zierenberg@gmail.com)
- **GitHub:** [superspartan6](https://github.com/superspartan6)
- **LinkedIn:** [Caleb Zierenberg](https://linkedin.com/in/calebzierenberg)










