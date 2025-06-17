---
date: 1970-01-01T00:00:00Z
---

# Python Design Patterns Working with Behavioral Design Patterns

## 2
### Strategy Pattern

**Behavioral Design Patterns** focus on the communication between components and how they interact with the external world. The Strategy pattern is one such behavioral design pattern that allows for the specification of different strategies to achieve the same objective. 

### Key Concepts
- **Strategy**: A family of algorithms that achieve the same goal but with different approaches.
- **Interchangeability**: Each algorithm implements the same interface, making them interchangeable.
- **Objective**: The goal or outcome remains constant, but the method of achieving it varies based on the chosen strategy.

### Example: Sorting
Sorting is a common example of the strategy pattern. Sorting involves determining the order of objects, which requires establishing a precedence between them. With the strategy pattern:
- Different strategies define how to compare two objects, such as sorting by score or name.
- The sorting order can vary (ascending or descending).
- In programming languages like Java, a **Comparator** is used to specify the sorting logic. In Python, this is achieved with the **key** argument.

The **strategy pattern** in sorting doesn't define how the entire sorting process works, but focuses on just one step: how to compare two objects.

### Sorting Variations
- **Lexicographical/Alphabetical Order**: Sorting strings in order.
- **Reverse Lexicographical Order**: Sorting in reverse order.
- **Case-sensitive or Case-insensitive**: Sorting strings with or without considering case.

Each sorting variation can be considered a different strategy. You can pass these strategies as objects to the sorting function to determine how the objects will be ordered.

### Algorithm Structure
- The strategy pattern uses **composition**: the algorithm is passed as a member variable or input argument, not inheritance.
- All strategy objects implement the same interface, ensuring they are interchangeable.
  
### Visual Representation of the Strategy Pattern
1. The **client** interacts with an interface.
2. The client provides **context** (strategy) for one step of the process.
3. The interface uses the provided strategy to execute the action, which may have multiple underlying implementations.

### Example: Transportation Strategy
In a real-world scenario, consider needing to go to the airport. The transportation method (bus, car, taxi) is the strategy. Each mode of transportation is a concrete strategy to achieve the same objective: getting to the airport.

**Workflow**:  
- **Client** selects a **transportation method**.
- The **strategy** (chosen transportation) is applied to reach the goal.

### Characteristics of the Strategy Pattern
- **Composition** is used instead of inheritance.
- **Algorithm objects** implement the same interface, ensuring they can be interchanged.
- The **client** specifies the strategy, which is plugged into a larger action.

## 3
### Strategy Pattern - Demo Examples

#### Simple Example: Basic Calculation Strategies

In this example, we define four different strategies for performing basic calculations on two numbers: addition, subtraction, multiplication, and division. Each operation is represented by a custom function, which forms the strategy for performing the calculation.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

Next, we define a `calculate` function that takes two input arguments and a strategy function as an argument. The strategy function determines which calculation is performed.

```python
def calculate(a, b, strategy_fn):
    return strategy_fn(a, b)
```

We can now call `calculate` with different strategy functions to perform various calculations.

```python
# Addition
calculate(10, 20, add)  # Output: 30

# Multiplication
calculate(10, 20, multiply)  # Output: 200
```

We can also define new strategies by adding more custom functions. For example, to calculate the power of a number:

```python
import math

def power_of(a, b):
    return math.pow(a, b)

calculate(10, 2, power_of)  # Output: 100
```

This approach allows us to easily extend and use different strategies to achieve the same goal of performing a calculation.

#### Advanced Example: Using Strategy with Python's Built-in `sorted` Function

Now, let's explore how the strategy pattern is used with Python's built-in `sorted` function. We'll start with a list of student names:

```python
students_list = ['Bob', 'Alice', 'Zubin', 'Samuel', 'Nina']
```

By default, the `sorted` function sorts strings in lexicographical order:

```python
sorted(students_list)  # Output: ['Alice', 'Bob', 'Nina', 'Samuel', 'Zubin']
```

We can change the sorting strategy by using the `key` argument. For instance, to sort by the length of the names, we can specify the `len` function as the strategy:

```python
sorted(students_list, key=len)  # Output: ['Bob', 'Nina', 'Alice', 'Zubin', 'Samuel']
```

Next, consider a list of student dictionaries, where each dictionary contains a student's name and score:

```python
students_dict = [
    {'name': 'Bob', 'score': 10},
    {'name': 'Nina', 'score': 40},
    {'name': 'Zubin', 'score': 90},
    {'name': 'Samuel', 'score': 70},
    {'name': 'Alice', 'score': 80}
]
```

If we try to sort the list directly, the default sorting strategy won't work since dictionaries need a specified key for sorting:

```python
sorted(students_dict)  # Error: Cannot compare dictionaries
```

To sort the dictionaries by the student's name, we define a custom strategy function:

```python
def get_name(student):
    return student['name']

sorted(students_dict, key=get_name)  
# Output: [{'name': 'Alice', 'score': 80}, {'name': 'Bob', 'score': 10}, {'name': 'Nina', 'score': 40}, {'name': 'Samuel', 'score': 70}, {'name': 'Zubin', 'score': 90}]
```

Alternatively, we can sort the dictionaries by the student's score:

```python
def get_score(student):
    return student['score']

sorted(students_dict, key=get_score)  
# Output: [{'name': 'Bob', 'score': 10}, {'name': 'Nina', 'score': 40}, {'name': 'Samuel', 'score': 70}, {'name': 'Alice', 'score': 80}, {'name': 'Zubin', 'score': 90}]
```

This demonstrates how the strategy pattern is used in sorting, allowing us to specify custom sorting logic (the strategy) using functions like `get_name` or `get_score`.

## 4
### Chain-of-Responsibility Pattern

The **Chain-of-Responsibility** pattern is a behavioral design pattern that allows a request to be passed along a chain of handlers until one of them is capable of processing it. This pattern decouples the sender of the request from the receiver, allowing multiple handlers to take care of different kinds of requests in a flexible way.

#### Key Principles
1. **Single Responsibility**: Each handler in the chain has a single responsibility — it only handles one kind of request.
2. **Request Propagation**: If a handler is unable to process the request, it passes the request to the next handler in the chain.
3. **Flexibility**: Handlers can be added or modified without affecting the client that is issuing the request.

#### How It Works
Imagine a scenario where multiple components listen for events, such as a button click in a user interface. There could be different responses based on the context when the button is clicked. The **Chain-of-Responsibility** pattern allows these events to be handled by different components, each responsible for handling a particular type of event or action.

The **request** flows through a series of **handlers**, and each handler determines whether it can process the request. If a handler can't handle the request, it passes it along to the next handler in the chain.

For example, in a user interface, a button click event might need to be processed differently depending on various factors like whether the user is logged in, the current state of the app, or the type of button clicked. Instead of a single handler dealing with all these cases, different handlers can be set up to manage different conditions.

#### Components of the Chain
1. **Handler Interface**: Defines the method that all handlers must implement (e.g., `handle_request()` or `execute()`).
2. **Concrete Handlers**: Implement the handler interface and perform specific actions for a particular type of request.
3. **Chain**: The sequence of handlers where each handler may pass the request along the chain if it cannot handle it.

#### Example Workflow
1. **Client** sends a request.
2. **HandlerOne** receives the request and determines if it can handle it:
   - If yes, it processes the request and returns the result.
   - If not, it passes the request to **HandlerTwo**.
3. **HandlerTwo** checks if it can handle the request:
   - If yes, it processes the request and returns the result.
   - If not, it passes the request to **HandlerThree**.
4. **HandlerThree** continues the same process and either handles the request or passes it along further down the chain (e.g., to **HandlerFour**).

If a handler successfully processes the request, it stops the propagation, and no further handlers are called.

#### Code Example

Here’s a basic example of how the Chain-of-Responsibility pattern might be implemented:

```python
class Handler:
    def set_next(self, handler):
        self._next_handler = handler
    
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class HandlerOne(Handler):
    def handle(self, request):
        if request == "Handle by One":
            return "Handled by Handler One"
        else:
            return super().handle(request)

class HandlerTwo(Handler):
    def handle(self, request):
        if request == "Handle by Two":
            return "Handled by Handler Two"
        else:
            return super().handle(request)

class HandlerThree(Handler):
    def handle(self, request):
        if request == "Handle by Three":
            return "Handled by Handler Three"
        else:
            return super().handle(request)

# Client Code
handler1 = HandlerOne()
handler2 = HandlerTwo()
handler3 = HandlerThree()

# Build the chain of responsibility
handler1.set_next(handler2)
handler2.set_next(handler3)

# Client sends the request
request = "Handle by Two"
response = handler1.handle(request)
print(response)  # Output: Handled by Handler Two
```

#### Real-World Example: Event Handling in UI
In graphical user interface (UI) frameworks, events like button clicks can trigger a chain of event handlers that may perform different actions based on the current context. For example, in a GUI:
- One handler might handle a button click when the user is logged in.
- Another handler might handle the click when the user is not logged in.
- A different handler could handle clicks depending on the button's state (enabled/disabled).

This pattern allows for a clean separation of concerns because each handler is responsible for only one condition or type of event.

#### Benefits of Chain-of-Responsibility
1. **Separation of Concerns**: Each handler is focused on handling only one type of request, ensuring that the design adheres to the Single Responsibility Principle.
2. **Dynamic Assignment**: New handlers can be added to the chain without affecting existing handlers or the client.
3. **Flexibility**: The request can be processed by different handlers based on the context, making it easy to extend and maintain.

#### When to Use the Chain-of-Responsibility Pattern
- When multiple objects can handle a request, but the handler is not known in advance.
- When you want to decouple the sender and receiver of a request.
- When the logic for handling requests can vary based on context (such as event-driven systems).

In summary, the **Chain-of-Responsibility** pattern provides a clean and flexible way to manage requests in a system, ensuring that each handler is responsible for a specific part of the processing, leading to better modularity and maintainability.

## 5
In this demo, we explore a Python implementation of the Chain of Responsibility design pattern, a behavioral pattern where a series of handlers process a request in a pipeline. Each handler only knows how to handle a specific operation, and if it can't handle the request, it passes it along to the next handler in the chain.

### Step-by-Step Implementation

1. **Abstract Base Class: `Operation`**
   - This class serves as the base for all handlers. It defines an abstract method `calculate` that must be implemented by each subclass to handle specific operations.
   - Each handler is initialized with a successor, which is the next handler in the chain (or `None` if it is the last handler).
   
```python
from abc import abstractmethod

class Operation:
    def __init__(self, successor=None):
        self._successor = successor
    
    @abstractmethod
    def calculate(self, operation):
        pass
```

2. **Handler Classes**
   - Each handler class, such as `Exponent`, `Modulus`, and `FloorDivision`, inherits from the `Operation` base class and implements the `calculate` method to handle specific operations.

   **Exponent Operation:**
   - This handler checks if the operation is exponentiation (using the `**` operator). If so, it performs the calculation; if not, it passes the operation to the next handler (if any).
   
```python
class Exponent(Operation):
    def calculate(self, operation):
        chars = operation.split()
        if chars[1] == '**':
            print('Exponent!')
            return int(chars[0]) ** int(chars[2])
        elif self._successor is not None:
            print('Exponent unable to handle operation, passing on to successor')
            return self._successor.calculate(operation)
        else:
            print("Operation not supported")
            return None
```

   **Modulus Operation:**
   - This handler checks for modulus (using the `%` operator). If it matches, it performs the modulus operation. If not, it passes it on to the next handler.
   
```python
class Modulus(Operation):
    def calculate(self, operation):
        chars = operation.split()
        if chars[1] == '%':
            print('Modulus!')
            return int(chars[0]) % int(chars[2])
        elif self._successor is not None:
            print('Modulus unable to handle operation, passing on to successor')
            return self._successor.calculate(operation)
        else:
            print("Operation not supported")
            return None
```

   **FloorDivision Operation:**
   - This handler performs floor division (`//`). If it can't handle the operation, it passes it to the successor.
   
```python
class FloorDivision(Operation):
    def calculate(self, operation):
        chars = operation.split()
        if chars[1] == '//':
            print('FloorDivision!')
            return int(chars[0]) // int(chars[2])
        elif self._successor is not None:
            print('FloorDivision unable to handle operation, passing on to successor')
            return self._successor.calculate(operation)
        else:
            print("Operation not supported")
            return None
```

3. **Setting Up the Chain of Responsibility:**
   - We create a chain of handlers where each operation is linked to the next one.
   
```python
operation3 = FloorDivision()
operation2 = Modulus(operation3)
operation1 = Exponent(operation2)
```

   - Here, `operation1` is the exponent operation, `operation2` is the modulus, and `operation3` is the floor division. The chain starts with `operation1`, which will check for the exponent operation. If it can't handle it, it passes the request to `operation2`, and so on.

4. **Testing the Chain:**
   - We perform calculations by passing strings representing operations (e.g., `"8**3"`, `"8%3"`, and `"8//3"`) to the `calculate` method of `operation1`. The request is passed through the chain until the appropriate handler processes it.

```python
print(operation1.calculate("8**3"))  # Exponent handled
print(operation1.calculate("8%3"))   # Modulus handled
print(operation1.calculate("8//3"))  # FloorDivision handled
print(operation1.calculate("8/3"))   # Unsupported operation
```

5. **Output:**
   - For each operation, the correct handler performs the calculation and returns the result. If an operation is not supported by any handler, it outputs `"Operation not supported"`.

```text
Exponent!
512
Exponent unable to handle operation, passing on to successor
Modulus!
2
Exponent unable to handle operation, passing on to successor
Modulus unable to handle operation, passing on to successor
FloorDivision!
2
Exponent unable to handle operation, passing on to successor
Modulus unable to handle operation, passing on to successor
FloorDivision unable to handle operation, passing on to successor
Operation not supported
```

### Conclusion:
This implementation demonstrates how the Chain of Responsibility pattern allows for flexible handling of different operations, where each handler is focused on a single responsibility and can pass an unsupported request along the chain. This approach promotes clean, maintainable code with clear separation of concerns.

## 6
The Observer pattern is a behavioral design pattern that allows for a one-to-many relationship between objects. When the state of a high-level object (subject) changes, all its dependent objects (observers) are automatically notified and updated without the high-level object needing to know anything about them. This pattern is widely used in systems where certain changes in one part of a system must be reflected across multiple other parts, especially in cases like event-driven programming or UI frameworks.

Here’s how it works:

- **Subject**: This is the high-level object that contains the state or behavior that the observers need to be aware of. It maintains a list of observers and notifies them when there’s a state change.
  
- **Observer**: These are the objects that listen for changes in the subject. They are updated automatically whenever the subject changes its state.
  
- **Notification**: When the subject’s state changes, it sends notifications to all registered observers, updating them with the latest information. The observers can then react accordingly.

### Example Breakdown:
1. **Auction Scenario**: Imagine an auction system where the auctioneer is the **subject** (the high-level object), and the bidders are the **observers** (the low-level objects).
   - The auctioneer sets the current bid price and notifies all observers (the bidders).
   - Each bidder is notified of changes, like the new highest bid, and can decide whether to bid higher.
   - The key point is that the bidders do not need to ask the auctioneer for updates. Instead, the auctioneer pushes the updates to all bidders (observers).

### Real-World Application:
- **UI Event Handling**: In a graphical user interface, buttons, checkboxes, or sliders (the **subject**) notify listeners (observers) when an event occurs, such as a click or change in state.
- **Stock Market**: A stock market ticker (subject) can notify all subscribed users (observers) about the price changes of stocks.

### When to Use the Observer Pattern:
- **Decoupling**: When you want to decouple the object that makes changes from the objects that need to react to those changes.
- **Multiple Consumers**: When one object needs to notify multiple dependent objects without those objects needing to query the source for updates.
  
### Benefits:
- **Loose Coupling**: The subject doesn't need to know who or how many observers are present. It just knows that it can notify all registered observers. Observers can also be added or removed without modifying the subject.
- **Scalability**: As new observers are added, they are automatically notified of changes without altering the subject's code.

In summary, the Observer pattern helps implement a system where changes are communicated automatically from the central object (subject) to its dependent objects (observers) without the observers querying the subject. This is especially useful in event-driven systems, UI design, and scenarios where multiple components need to stay in sync with one another.

## 7
### Publisher Class
```python
class Publisher:
    def __init__(self, name):
        self.__name = name
        self.__subscribers = set()

    def register(self, subscriber):
        self.__subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.__subscribers.discard(subscriber)

    def publish(self, message):
        for subscriber in self.__subscribers:
            subscriber.notify(message)
```

- **`__init__(self, name)`**: Initializes the publisher with a name and an empty set of subscribers.
- **`register(self, subscriber)`**: Adds a subscriber to the list of subscribers.
- **`unregister(self, subscriber)`**: Removes a subscriber from the list of subscribers.
- **`publish(self, message)`**: Notifies all subscribers with the published message.

### Subscriber Class
```python
class Subscriber:
    def __init__(self, name):
        self.__name = name

    def notify(self, message):
        print(self.__name + ' received message: ' + message)
```

- **`__init__(self, name)`**: Initializes the subscriber with a name.
- **`notify(self, message)`**: Prints the message received by the subscriber.

### Example Usage

```python
# Creating a publisher for news
publisher = Publisher('News')

# Creating subscribers
alice = Subscriber('Alice')
betty = Subscriber('Betty')

# Registering subscribers to the publisher
publisher.register(alice)
publisher.register(betty)

# Publishing a message
publisher.publish('Today was a calm and peaceful day, nothing much happened')

# Adding a new subscriber
charles = Subscriber('Charles')
publisher.register(charles)

# Publishing another message
publisher.publish('Hurricane Dorian is going to make landfall today')

# Unregistering a subscriber
publisher.unregister(betty)

# Publishing a message after Betty has unregistered
publisher.publish('Numbers show that employment growth has been strong')
```

### Output
- Alice and Betty receive the first message when it is published.
- Alice, Betty, and Charles receive the second message.
- After Betty unregisters, only Alice and Charles receive the third message.

This demonstrates the observer pattern where the `Publisher` is the high-level object, and the `Subscriber` is the low-level object receiving notifications.

## 8
### Product Class

```python
class Product:
    PRICE = 'price'
    STOCK = 'stock'

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__price_observers = set()
        self.__stock_observers = set()

    def add_observer(self, observer_type, observer):
        if observer_type == self.PRICE:
            self.__price_observers.add(observer)
        elif observer_type == self.STOCK:
            self.__stock_observers.add(observer)

    def remove_observer(self, observer_type, observer):
        if observer_type == self.PRICE:
            self.__price_observers.discard(observer)
        elif observer_type == self.STOCK:
            self.__stock_observers.discard(observer)

    def update_price(self, price):
        self.__price = price
        self.__notify(self.PRICE)

    def update_stock(self, stock):
        self.__stock = stock
        self.__notify(self.STOCK)

    def __notify(self, observer_type):
        observers = []
        message = None

        if observer_type == self.PRICE:
            observers = self.__price_observers
            message = f'{self.__name} price updated to: {self.__price}'
        elif observer_type == self.STOCK:
            observers = self.__stock_observers
            message = f'{self.__name} now back in stock!'

        for observer in observers:
            observer.notify(message)
```

### Customer Class

```python
class Customer:
    def __init__(self, name):
        self.__name = name

    def notify(self, message):
        print(f'{self.__name} - {message}')
```

### Example Usage

#### Instantiate Products
```python
apple_iphone = Product('iPhone', 600)
samsung_s10 = Product('Samsung S10', 300)
```

#### Instantiate Customers
```python
alice = Customer('Alice')
betty = Customer('Betty')
charles = Customer('Charles')
```

#### Register Observers

```python
# Alice is interested in both price and stock updates for the iPhone
apple_iphone.add_observer(Product.PRICE, alice)
apple_iphone.add_observer(Product.STOCK, alice)

# Betty is interested in both price and stock updates for the Samsung S10
samsung_s10.add_observer(Product.PRICE, betty)
samsung_s10.add_observer(Product.STOCK, betty)

# Charles is interested in price updates for the iPhone and stock updates for the Samsung S10
apple_iphone.add_observer(Product.PRICE, charles)
samsung_s10.add_observer(Product.STOCK, charles)
```

#### Update Product Price and Stock

```python
# Price update for iPhone, Alice and Charles will receive a notification
apple_iphone.update_price(566)

# Stock update for iPhone, Alice will receive a notification
apple_iphone.update_stock(10)

# Price update for Samsung S10, Betty will receive a notification
samsung_s10.update_price(333)

# Stock update for Samsung S10, Betty and Charles will receive a notification
samsung_s10.update_stock(10)
```

## 9
### Command Pattern Overview

The **Command Pattern** is a behavioral design pattern that is commonly used to implement features like **undo** and **redo** in applications. The key concept behind this pattern is that all the details required to execute an operation are encapsulated within a single object, called a **command object**.

In the Command Pattern:

- A **request** is received from the client, which specifies an operation to be performed.
- The **parameters** and the **operation** itself are wrapped into a **command object**.
- The command object holds the **context**, **operation details**, and any **external parameters** required to execute the operation.

This decouples the **execution** of an operation from the **invocation** of that operation. The invocation only knows about the parameters needed to execute the command, while the command object knows how to perform the operation.

The **command abstraction** allows operations to be grouped together with the necessary functionality for **execution**, **undo**, and **redo** operations.

---

### How Command Pattern Helps with Undo/Redo

In applications such as **Excel**, **Microsoft Word**, or **online spreadsheets**, the Command Pattern is often used to implement **undo/redo functionality**. 

- Every operation that can be performed is wrapped in a command.
- A **stack** of recently executed commands is maintained.
  - Why a stack? A stack follows the **last-in, first-out (LIFO)** principle. The last command executed is the first one to be accessed when performing an undo operation.
- The **command object** knows how to:
  - Execute the operation.
  - Undo the operation.
- When the user performs an **undo**, the last command is popped from the stack, and the command is asked to undo itself.

---

### Command Pattern in Action

Let’s consider an example using a **restaurant** scenario to illustrate the Command Pattern:

- **Customer**: Places an order (command) and can also undo the order.
- **Waiter**: Receives the customer’s order and transmits it to the kitchen, also capable of canceling an order.
- **Cook**: Prepares the order and can undo it (e.g., discard or hold the prepared meal).

In this case:

- **Customer** creates a command (the order) and knows how to place and cancel the order.
- The **Waiter** helps transmit the order to the **Kitchen**, along with any necessary information (e.g., burger, shake).
- The **Cook** prepares the order, and if necessary, can undo the preparation.

In this pattern:
- **Commands** encapsulate all information required to execute an operation.
- Each component in the system knows how to execute its part and how to undo it when necessary.

---

### Benefits of the Command Pattern

1. **Decouples** the requester of an action from the executor.
2. Provides a clean interface for **undo/redo** functionality.
3. Encapsulates all necessary details to perform an operation into a single object, ensuring a **self-contained** action.
4. Supports queuing of operations and logging for future reference.

This pattern is particularly useful when dealing with operations that need to be performed in sequence but also support undoing or redoing actions.

## 10
### Command Pattern Implementation

1. **Importing Dependencies**
   - Import ABC (abstract base class) and abstractmethod from the `abc` module.

```python
from abc import ABC, abstractmethod
```

2. **Base Command Class**
   - Define the `Command` class as an abstract base class with two abstract methods: `execute` and `undo`.

```python
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
```

3. **Concrete Command Classes**
   - Define various command classes that implement the `Command` class.

```python
class Bold(Command):
    def execute(self):
        print('Bold')

    def undo(self):
        print('Undo Bold')
```

```python
class Italic(Command):
    def execute(self):
        print('Italic')

    def undo(self):
        print('Undo Italic')
```

```python
class Underline(Command):
    def execute(self):
        print('Underline')

    def undo(self):
        print('Undo Underline')
```

```python
class Strikethrough(Command):
    def execute(self):
        print('Strikethrough')

    def undo(self):
        print('Undo Strikethrough')
```

4. **Command Stack**
   - Define a list `commands_executed` to track the executed commands (using it as a stack).

```python
commands_executed = []
```

5. **Execute Function**
   - Define a function to execute a command and add it to the `commands_executed` stack.

```python
def execute(command):
    command.execute()
    commands_executed.append(command)
```

6. **Undo Function**
   - Define a function to undo the last executed command by popping it from the stack.

```python
def undo():
    if len(commands_executed) == 0:
        print('Nothing to undo!')
        return

    command = commands_executed.pop()
    command.undo()
```

7. **Executing Commands**
   - Execute the commands in sequence and observe the `commands_executed` stack.

```python
execute(Bold())
execute(Underline())
execute(Strikethrough())
execute(Italic())
execute(Bold())
```

8. **Undoing Commands**
   - Undo the commands in reverse order of their execution.

```python
undo()  # Undo Bold
undo()  # Undo Italic
undo()  # Undo Strikethrough
undo()  # Undo Underline
undo()  # Undo Bold
```

9. **Empty Undo Stack**
   - If the stack is empty, the `undo` function will display a message indicating there is nothing to undo.

```python
undo()  # Nothing to undo!
```

10. **Test Undo After New Command**
   - Execute and undo commands again to test the functionality.

```python
execute(Italic())
undo()  # Undo Italic
```

## 11
### Iterator Pattern

1. **Introduction to the Iterator Pattern**
   - The iterator pattern is widely used to access elements in a collection, such as lists, dictionaries, or custom collections, sequentially and in the right order.
   - In Python, for loops or while loops iterate over collections like lists or dictionaries, which implement the iterator pattern.

2. **Principle Behind the Iterator Pattern**
   - The iterator pattern allows access to elements in a collection sequentially, without exposing the underlying structure of the collection.
   - Clients do not need to know how the collection is implemented or how elements are organized. They only need to use the iterator to access elements.

3. **Advantages of the Iterator Pattern**
   - Provides a consistent way to iterate over different types of collections, such as lists, tuples, or sets.
   - The iterator interface remains the same, regardless of the type of collection, enabling the same iteration code to work across different collections.

4. **Separation of Concerns**
   - The iterator pattern separates the container (the collection) from the iteration mechanism.
   - Iteration is handled by a separate abstraction, allowing clients to access collection elements without knowing the collection’s details.

5. **Iterator Abstraction**
   - The client should interact with a `TraversalAbstraction` that allows iteration over different collections.
   - The `TraversalAbstraction` typically includes the following methods:
     - `first()`: Resets the iteration to the first element.
     - `next()`: Accesses the next element in the collection.
     - `isDone()`: Checks if the iteration is complete.

6. **Implementing Iterators for Different Collections**
   - Each collection (e.g., ListCollection, MapCollection) should implement the `TraversalAbstraction` interface.
   - Example:
     - `ListTraversal` for lists
     - `MapTraversal` for maps
   - These abstractions allow clients to use the same methods for iteration, regardless of the collection type.

### Visual Representation
- **Client** interacts with a `TraversalAbstraction` to iterate over elements of a collection.
- The `TraversalAbstraction` defines methods for iteration, such as `first()`, `next()`, and `isDone()`.
- Each collection type (e.g., ListCollection, MapCollection) implements a corresponding traversal abstraction (e.g., `ListTraversal`, `MapTraversal`).

## 12
### Participants Class Implementation Using the Iterator Pattern in Python

The **Iterator Pattern** is used to access elements in a collection sequentially, without exposing the underlying structure. The pattern allows iteration over elements like strings, numbers, or integers, regardless of whether they are stored in a list or another data structure.

#### Participants Class

```python
class Participants:
    def __init__(self):
        self.__participants = []
        self.__index = 0
```

- **`__init__` Method**: Initializes an empty list `__participants` to store participant names and sets the `__index` to 0 to track the current position during iteration.

```python
    def add_participant(self, name):
        self.__participants.append(name)
```

- **`add_participant` Method**: Adds a participant to the `__participants` list by appending the participant's name.

```python
    def __len__(self):
        return len(self.__participants)
```

- **`__len__` Method**: Returns the number of participants in the list. This method is used to get the length of the object.

```python
    def __iter__(self):
        self.__index = 0
        return self
```

- **`__iter__` Method**: Resets the `__index` to 0 and returns the current instance (`self`) as the iterator object.

```python
    def __next__(self):
        if self.__index == len(self.__participants):
            raise StopIteration
        p = self.__participants[self.__index]
        self.__index += 1
        return p
```

- **`__next__` Method**: Returns the next participant in the sequence. If the index exceeds the number of participants, it raises a `StopIteration` exception to signal the end of the iteration.

### Example Usage

1. **Creating and Adding Participants**:

```python
participants = Participants()
participants.add_participant('Lily')
participants.add_participant('James')
participants.add_participant('Harry')
participants.add_participant('Ron')
participants.add_participant('Hermione')
```

2. **Iterating Over Participants with a For Loop**:

```python
for p in participants:
    print(p)
```

- **How it Works**:
  - The `__iter__` method is called to initialize the iterator.
  - The `__next__` method is repeatedly called to get each participant until `StopIteration` is raised.

3. **Adding a New Participant and Iterating Again**:

```python
participants.add_participant('Ginny')
for p in participants:
    print(p)
```

- Ginny will be included at the end of the list.

4. **Manually Iterating with `iter()` and `next()`**:

```python
iterator = iter(participants)  # Initializes the iterator
print(next(iterator))  # Lily
print(next(iterator))  # James
print(next(iterator))  # Harry
print(next(iterator))  # Ron
print(next(iterator))  # Hermione
print(next(iterator))  # Ginny
```

5. **Handling `StopIteration`**:

If `next(iterator)` is called after reaching the last participant, a `StopIteration` exception is raised:

```python
try:
    print(next(iterator))  # Raises StopIteration
except StopIteration:
    print("End of participants list.")
```

6. **Reinitializing the Iterator**:

To restart the iteration, call the `iter()` function again:

```python
iterator = iter(participants)  # Re-initialize the iterator
print(next(iterator))  # Lily
```

### Key Points

- **`__len__`**: Defines the length of the collection.
- **`__iter__`**: Prepares the iterator (sets the starting index).
- **`__next__`**: Provides the next element and raises `StopIteration` when the sequence ends.

