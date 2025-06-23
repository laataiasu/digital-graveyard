---
date: 2001-01-01
---

# Python Design Patterns Working with Structural Design Patterns

## 2
### Adapter Pattern

#### Structural Design Patterns Overview

Structural design patterns deal with how classes and components are composed to form complex structures. These patterns focus on the relationships between components and how they interact with each other. In contrast to behavioral patterns, which focus on interactions with external systems, structural patterns are about organizing and composing the components of your system.

#### Inheritance and Composition in Structural Patterns

In structural design, inheritance is often used to express relationships between components. You can have:

1. **Inheritance Hierarchy of Classes**: A base class with derived classes.
2. **Inheritance Hierarchy of Interfaces**: A base interface with more general or specialized derived interfaces that clients can use.

While structural class-creation patterns focus on using inheritance, structural object-patterns focus on composing objects to achieve new functionality. This enables the creation of more complex systems by combining simpler components in meaningful ways.

#### Adapter Pattern Overview

The **Adapter pattern** is a structural object-pattern. It doesn’t focus on how objects relate to each other, but rather on how their interfaces are composed to allow them to interact.

An adapter serves as an intermediary between two incompatible interfaces, allowing them to work together. The Adapter pattern can:

- Expose the right interface to different clients based on context.
- Allow legacy components to interact with new clients by converting an old interface to the expected one.

#### Real-World Use Case: Exposing Different Interfaces

Imagine you have an object with multiple ways to interact with a user—via email, phone, or text message. Depending on the client, you may want to expose only a subset of these communication methods. 

- **Client 1** might need email and phone communication.
- **Client 2** might need email and text communication.

An adapter can expose the appropriate interface to each client, hiding the complexity and allowing the system to adapt to different needs.

#### Legacy System Integration

Another common use case for the adapter pattern is integrating legacy systems with new ones. Over time, systems evolve, and new clients might not be compatible with older code due to different interfaces. An adapter can convert the legacy interface to a format expected by modern clients.

For example, if a legacy component uses a different interface, an adapter can translate the old interface into one that the new system understands, making it possible for both old and new systems to work together seamlessly.

#### Adapter Pattern Example: Simple Visualization

- **Client**: Used to working with the `Shape` interface, which has a `display()` method to render shapes.
- **Legacy Rectangle**: Uses a `show()` method instead of `display()`.

Without an adapter, the client would need to know when to call `show()` for the legacy rectangle, which is poor design. Instead, we create an adapter:

1. The **adapter** class implements the `display()` method.
2. The adapter delegates the call to `show()` in the legacy rectangle.

This allows the client to continue using the `display()` method, even when interacting with a legacy system that uses a different interface.

#### Generalized Adapter Example

- **New Application**: Expects the `Wrapper` interface with a `doThis()` method.
- **Legacy Component**: Implements a `doThat()` method, which is incompatible with the new application.

To make these work together, an adapter is used:

1. The adapter implements the `Wrapper` interface and the `doThis()` method.
2. The adapter internally calls the legacy `doThat()` method to perform the actual work.

This allows the new application to work with the legacy component without needing to know about the interface mismatch.

## 3
### Adapter Pattern Hands-on Demo

#### Legacy Code Example

1. **LegacyRectangle Class**:  
   Represents a rectangle with an area calculation method and a draw method.

   ```python
   class LegacyRectangle:
       def __init__(self, length, breadth):
           self.__length = length
           self.__breadth = breadth

       def area_calculation(self):
           return self.__length * self.__breadth

       def draw(self):
           print("This draws a legacy rectangle to screen")
   ```

2. **LegacySquare Class**:  
   Represents a square with its own area calculation and drawing methods.

   ```python
   class LegacySquare:
       def __init__(self, side):
           self.__side = side

       def area(self):
           return self.__side * self.__side

       def draw_me(self):
           print("This draws a legacy square to screen")
   ```

3. **Using LegacyRectangle**:

   ```python
   l_rectangle = LegacyRectangle(5, 6)
   print(l_rectangle.area_calculation())  # Output: 30
   l_rectangle.draw()  # Output: This draws a legacy rectangle to screen
   ```

4. **Using LegacySquare**:

   ```python
   l_square = LegacySquare(5)
   print(l_square.area())  # Output: 25
   l_square.draw_me()  # Output: This draws a legacy square to screen
   ```

#### The Problem: Different Interfaces for Similar Objects

The `LegacyRectangle` and `LegacySquare` classes have different interfaces (methods) for calculating area and drawing shapes, which can confuse clients that need to work with both.

#### Solution: Common Interface with the Shape Class

To provide a common interface, we introduce a `Shape` base class:

```python
class Shape:
    def __init__(self, shape_type):
        self.__shape_type = shape_type

    def get_area(self):
        pass

    def render(self):
        pass
```

Any shape (like `Circle`, `Rectangle`, or `Square`) can inherit from `Shape` and implement its own area calculation and rendering methods.

#### Example of Circle Class:

```python
import math

class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, 'Circle')
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def render(self):
        print("This draws a circle to screen")
```

#### Using the Common Interface

1. **Custom Functions for Shapes**:

   - To render any shape:

   ```python
   def render_shape(shape):
       shape.render()
   ```

   - To calculate the area of any shape:

   ```python
   def calculate_area(shape):
       return shape.get_area()
   ```

#### Applying the Adapter Pattern

To work with legacy components (`LegacyRectangle` and `LegacySquare`), we create adapters that implement the `Shape` interface, allowing clients to use these components through a common interface.

1. **Adapter for LegacyRectangle**:

   ```python
   class RectangleAdapter(Shape):
       def __init__(self, legacy_rectangle):
           self.legacy_rectangle = legacy_rectangle

       def get_area(self):
           return self.legacy_rectangle.area_calculation()

       def render(self):
           self.legacy_rectangle.draw()
   ```

2. **Adapter for LegacySquare**:

   ```python
   class SquareAdapter(Shape):
       def __init__(self, legacy_square):
           self.legacy_square = legacy_square

       def get_area(self):
           return self.legacy_square.area()

       def render(self):
           self.legacy_square.draw_me()
   ```

#### Final Integration Example:

```python
# Legacy components
legacy_rectangle = LegacyRectangle(5, 6)
legacy_square = LegacySquare(5)

# Adapting legacy components to Shape interface
rectangle = RectangleAdapter(legacy_rectangle)
square = SquareAdapter(legacy_square)

# Use custom functions with the adapted objects
print(calculate_area(rectangle))  # Output: 30
render_shape(rectangle)  # Output: This draws a legacy rectangle to screen

print(calculate_area(square))  # Output: 25
render_shape(square)  # Output: This draws a legacy square to screen
```

With this approach, both `LegacyRectangle` and `LegacySquare` can be used through the common `Shape` interface, making it easier for clients to work with these objects consistently.

## 4
### Extending the Shape Hierarchy with Legacy Adapters

In this demo, the third team that has set up a clean `Shape` hierarchy with `Circle`, `Rectangle`, and `Square` objects realizes they need to integrate legacy components that don't conform to the common interface they’ve established. This includes legacy components like `LegacyRectangle` and `LegacySquare`, which don't have the `get_area()` and `render()` methods that clients expect. 

To solve this problem, they use **adapter classes** to bridge the gap between the legacy code and the new `Shape` interface.

#### LegacyRectangle and LegacySquare Problem

- The `render_shape` function expects any shape object to have a `render()` method, but `LegacyRectangle` only has a `draw()` method.
- Similarly, the `calculate_area` function expects objects to have a `get_area()` method, but `LegacySquare` only has a method called `area()`.

#### Solution: Adapters

1. **LegacyRectangleAdapter**:  
   This adapter converts the interface of `LegacyRectangle` to the `Shape` interface.

   ```python
   class LegacyRectangleAdapter(Shape):
       def __init__(self, legacy_rectangle):
           Shape.__init__(self, 'Rectangle')
           self.__legacy_rectangle = legacy_rectangle

       def get_area(self):
           return self.__legacy_rectangle.area_calculation()  # Delegates to LegacyRectangle's area_calculation

       def render(self):
           self.__legacy_rectangle.draw()  # Delegates to LegacyRectangle's draw method
   ```

2. **LegacySquareAdapter**:  
   Similarly, this adapter converts the `LegacySquare` interface to the `Shape` interface.

   ```python
   class LegacySquareAdapter(Shape):
       def __init__(self, legacy_square):
           Shape.__init__(self, 'Square')
           self.__legacy_square = legacy_square

       def get_area(self):
           return self.__legacy_square.area()  # Delegates to LegacySquare's area method

       def render(self):
           self.__legacy_square.draw_me()  # Delegates to LegacySquare's draw_me method
   ```

#### Using Adapters in Practice

Now that the adapters are in place, the third team can work with legacy objects using the new common interface.

1. **Adapting Legacy Components**:

   ```python
   # Create LegacyRectangle and LegacySquare instances
   legacy_rectangle = LegacyRectangle(5, 6)
   legacy_square = LegacySquare(5)

   # Create adapters for these legacy objects
   rectangle_adapter = LegacyRectangleAdapter(legacy_rectangle)
   square_adapter = LegacySquareAdapter(legacy_square)
   ```

2. **Calculating Area and Rendering Shapes**:

   With the adapters, clients can now pass these legacy shapes into existing functions like `calculate_area()` and `render_shape()`.

   ```python
   # Calculate area for the rectangle using the adapter
   print(calculate_area(rectangle_adapter))  # Output: 30

   # Render the rectangle using the adapter
   render_shape(rectangle_adapter)  # Output: This draws a legacy rectangle to screen

   # Calculate area for the square using the adapter
   print(calculate_area(square_adapter))  # Output: 25

   # Render the square using the adapter
   render_shape(square_adapter)  # Output: This draws a legacy square to screen
   ```

#### Benefits of Using the Adapter Pattern

1. **Non-intrusive**:  
   The original `LegacyRectangle` and `LegacySquare` classes are not modified. The adapter pattern allows for integration of legacy code without changing the legacy systems.

2. **Uniform Interface**:  
   The clients now interact with the `Shape` interface for all shapes (including legacy ones). This makes the code cleaner and easier to maintain since all shapes can be handled uniformly.

3. **Reusability**:  
   Once the adapter is written, the legacy components can be reused without needing any modifications to the clients or the core system.

By using the adapter pattern, the third team was able to extend their shape hierarchy to include legacy components (`LegacyRectangle` and `LegacySquare`) without disrupting the structure of their existing code. This made it easy to integrate older codebases with newer systems, ensuring a smooth workflow for all clients.

## 5
### Decorator Design Pattern

The **Decorator** pattern is a structural design pattern that allows you to dynamically add responsibilities or behaviors to an object at runtime. This pattern is particularly useful when you want to extend the functionality of an object without modifying its core structure or using static inheritance.

#### Key Characteristics of the Decorator Pattern:

1. **Dynamic Behavior Addition**: The decorator pattern allows you to add new behavior or responsibilities to objects dynamically, during runtime, rather than at compile time. This is particularly useful when you don't know ahead of time what behavior you'll need for a specific object.

2. **Chained Relationships**: The pattern enables a chained, layered approach where you "wrap" an object with additional functionalities. Each decorator adds specific functionality and wraps the base object or the previous decorator in the chain.

3. **Alternative to Inheritance**: While inheritance can provide a way to add functionality, it is static and cannot be changed dynamically. The decorator, on the other hand, offers a flexible and dynamic way to extend the behavior of objects without altering the original class or creating a complex inheritance hierarchy.

#### Real-World Example: Java IO Streams

A classic example of the decorator pattern in use is Java's **InputStream** and **OutputStream** classes. These classes serve as abstract representations of data streams in Java, and decorators are used to extend the functionality of these streams in various ways, like buffering, encryption, or compression.

##### Problem Statement:
Java needs to support many types of data input (e.g., files, network connections, keyboard input, etc.), and each input can have various extensions or modifications (e.g., encrypted files, compressed files). How can Java efficiently manage all these variations without creating a vast number of subclasses?

##### Solution: Using the Decorator Pattern

Java uses the decorator pattern to allow the chaining of different `InputStream` or `OutputStream` objects, each adding specific functionality. These decorators all implement the same abstract base class (e.g., `InputStream`), which ensures that they can be used interchangeably.

##### Example of a Decorator Chain:

1. **Base Stream**: A basic `FileInputStream` class is used to read data from a file.

2. **Buffered Stream**: If we want to optimize reading from the file by buffering the contents, we use the `BufferedInputStream` decorator. This decorator wraps around the `FileInputStream` and adds buffering functionality.

3. **GZIP Compression**: If the file is compressed, the `GZIPInputStream` decorator can be applied to the `BufferedInputStream`. It adds the ability to handle GZIP-compressed data.

4. **Object Representation**: Finally, if you want to deserialize the GZIP-compressed file into objects, you can wrap the `GZIPInputStream` in an `ObjectInputStream` decorator.

Each of these decorators adds a specific functionality while conforming to the same `InputStream` interface, which ensures that they can be used in a unified way by clients.

#### The Chain in Action:

Imagine we have a file that needs to be read with the following steps:
1. Read from a file.
2. Buffer the file for efficient reading.
3. Decompress it if it's in GZIP format.
4. Convert the decompressed data into objects.

Using decorators, you would create a chain of `InputStream` objects as follows:

- **FileInputStream** → **BufferedInputStream** → **GZIPInputStream** → **ObjectInputStream**

Each object in the chain is a decorator that extends the functionality of the previous one. The client code interacts with the outermost decorator (`ObjectInputStream`), and does not need to worry about how the file is buffered, compressed, or transformed into objects.

#### Visualizing the Decorator Pattern:

In the example above, you can imagine each layer of the decorator pattern as a "wrapper" around the previous one:

- The **FileInputStream** is the innermost object, representing the basic file read operation.
- The **BufferedInputStream** adds the ability to buffer the file content as it’s read.
- The **GZIPInputStream** allows for decompression of GZIP files.
- The **ObjectInputStream** finally transforms the decompressed data into Java objects.

These decorators work together to form a chain of functionality, and the client interacts with the outermost decorator (`ObjectInputStream`), unaware of the individual layers inside.

#### When to Use the Decorator Pattern:

- **Flexible Behavior**: When you want to add or modify the behavior of an object at runtime.
- **Avoiding Inheritance Complexity**: When inheritance would lead to a complex, rigid class hierarchy. Decorators allow for more modular and flexible code.
- **Extending Functionality**: When you have a base object but need to extend its functionality in various ways without creating subclasses for every combination of behaviors.

#### Conclusion:
The **Decorator** pattern is an incredibly powerful tool for adding responsibilities or behaviors to objects at runtime, providing a flexible and modular approach to extending functionality. Its use of chained decorators ensures that new features can be added dynamically without altering the original object or class. In real-world applications like Java I/O, this pattern helps manage a variety of input and output types in a clean and extendable way.

## 6
In this demo, we see a common scenario where we initially start with simple inheritance to handle different text formatting options, but this quickly becomes problematic due to the limitations of static inheritance. We’ll discuss how the **Decorator Pattern** can solve this problem by allowing us to dynamically add new responsibilities (like bold, italic, underline) to the text objects without the need for complex inheritance structures.

### Initial Approach: Using Inheritance

We begin by creating a `PlainText` class that represents a simple text message. This class has a `render()` method that simply returns the plain text.

```python
class PlainText:
    def __init__(self, text):
        self.__text = text

    def render(self):
        return self.__text
```

This is fine when we only need to display simple text, but as our word processor grows in complexity, we need to add new behaviors (like bold or italic), which seems to suggest the need for inheritance.

### Adding New Behaviors with Inheritance

Next, we create derived classes like `BoldText` and `ItalicText` to format the text. The `BoldText` class inherits from `PlainText` and overrides the `render()` method to return the text wrapped in `<b>` tags for bold formatting.

```python
class BoldText(PlainText):
    def __init__(self, text):
        PlainText.__init__(self, text)

    def render(self):
        return "<b>{}</b>".format(super().render())
```

Similarly, we create an `ItalicText` class that wraps the `PlainText` text in `<i>` tags for italics.

```python
class ItalicText(PlainText):
    def __init__(self, text):
        PlainText.__init__(self, text)

    def render(self):
        return "<i>{}</i>".format(super().render())
```

With this approach, we can create instances like `BoldText` and `ItalicText`:

```python
my_text = BoldText("python")
print(my_text.render())  # Output: <b>python</b>

my_text = ItalicText("python")
print(my_text.render())  # Output: <i>python</i>
```

We even manage to combine behaviors, such as `BoldItalicText`, to apply both bold and italic formatting.

```python
class BoldItalicText(PlainText):
    def __init__(self, text):
        PlainText.__init__(self, text)

    def render(self):
        return "<b><i>{}</i></b>".format(super().render())
```

### The Problem with Static Inheritance

At first, this approach seems fine, but as we continue adding new formatting features, we start to run into a problem. For example, to support underline functionality, we would need to create additional classes like `UnderlineText`, `BoldUnderlineText`, `ItalicUnderlineText`, and so on. This results in an **explosion of classes** because every new combination of formatting requires a new subclass.

For example:
- `UnderlineText`
- `BoldUnderlineText`
- `ItalicUnderlineText`
- `BoldItalicUnderlineText`

This results in a significant amount of redundant code, making the design cumbersome and difficult to maintain.

### The Solution: Using the Decorator Pattern

The decorator pattern allows us to **dynamically add behavior to objects at runtime** instead of relying on a rigid inheritance hierarchy. Instead of creating subclasses for each combination of formatting, we can create decorators that add individual formatting features (like bold, italic, underline) and then combine them as needed.

#### Refactoring with the Decorator Pattern

Let’s now refactor the code to use the **Decorator Pattern**. We start by defining an abstract decorator class that will wrap around any `PlainText` object. Each decorator will extend the functionality of the base `PlainText` class, and we can chain them together.

```python
class TextDecorator(PlainText):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text.render()  # Delegating to the wrapped object
```

Now we can create concrete decorators for each behavior:

```python
class BoldDecorator(TextDecorator):
    def render(self):
        return "<b>{}</b>".format(super().render())

class ItalicDecorator(TextDecorator):
    def render(self):
        return "<i>{}</i>".format(super().render())

class UnderlineDecorator(TextDecorator):
    def render(self):
        return "<u>{}</u>".format(super().render())
```

These decorators add individual formatting behaviors (bold, italic, underline) to the text, and we can apply them dynamically as needed.

#### Chaining Decorators

We can now easily combine multiple decorators together by wrapping one decorator inside another. For example, to apply both bold and italic formatting to a text:

```python
plain_text = PlainText("python")

bold_text = BoldDecorator(plain_text)
italic_bold_text = ItalicDecorator(bold_text)

print(italic_bold_text.render())  # Output: <i><b>python</b></i>
```

Here, the `ItalicDecorator` is wrapping the `BoldDecorator`, which in turn wraps the `PlainText` object. This chaining allows us to apply any combination of decorators without needing to create a new class for each combination.

#### Advantages of the Decorator Pattern

- **Flexible**: You can combine different behaviors dynamically without changing the underlying classes.
- **Extensible**: New behaviors can be added easily by creating new decorators, without modifying existing code.
- **Avoids Class Explosion**: We don’t need to create subclasses for every combination of behaviors. Instead, we compose objects at runtime.

### Conclusion

The **Decorator Pattern** provides a powerful solution to the problem of adding behavior to objects at runtime. Instead of using static inheritance, decorators allow for more flexibility and avoid the need for a massive class hierarchy. In our word processor example, using decorators enables us to combine formatting behaviors like bold, italic, and underline in a clean and maintainable way.

## 7
The **Decorator Pattern** is a structural pattern that allows you to dynamically add behavior or responsibilities to objects at runtime. It is particularly useful when you need to add functionalities to objects without altering their original structure. In this scenario, we are using the decorator pattern to add text formatting (like bold, italic, and underline) to a `PlainText` object in a flexible and reusable way. Let’s walk through the steps for implementing the decorator pattern in this scenario.

### 1. Base Class: `Render`

The first step is to define an abstract base class `Render`, which will specify the contract for rendering text. This class doesn't contain any actual implementation but ensures that any subclass will have a `render()` method.

```python
class Render:
    def render(self):
        pass  # This is an abstract method
```

### 2. `PlainText`: The Core Text Object

Next, we define the `PlainText` class, which represents plain text. This class inherits from `Render` and implements the `render()` method to simply return the text string.

```python
class PlainText(Render):
    def __init__(self, text):
        self.__text = text

    def render(self):
        return self.__text
```

The `PlainText` class is a basic implementation, where the `render()` method just returns the string as is.

### 3. The Decorator: `PlainTextDecorator`

Now, we create the `PlainTextDecorator`, which serves as the base class for all decorators. The purpose of this decorator is to wrap any `Render` object (like `PlainText` or other decorators) and provide the ability to add more functionality to it.

```python
class PlainTextDecorator(Render):
    def __init__(self, render):
        self.__render = render

    def render(self):
        return self.__render.render()
```

In this `PlainTextDecorator`, we accept a `Render` object as a parameter and store it in a member variable (`__render`). In the `render()` method, we simply delegate the call to `render()` of the wrapped object.

### 4. Creating Specific Decorators

Each specific decorator will extend `PlainTextDecorator` and modify the rendering behavior. Let’s start with a **BoldTextDecorator** that adds bold formatting:

```python
class BoldTextDecorator(PlainTextDecorator):
    def __init__(self, render):
        super().__init__(render)

    def render(self):
        return "<b>{}</b>".format(super().render())
```

This `BoldTextDecorator` overrides the `render()` method and wraps the result of the `render()` method of the underlying object in `<b></b>` tags.

Similarly, we create an **ItalicTextDecorator**:

```python
class ItalicTextDecorator(PlainTextDecorator):
    def __init__(self, render):
        super().__init__(render)

    def render(self):
        return "<i>{}</i>".format(super().render())
```

This `ItalicTextDecorator` wraps the result of the `render()` method in `<i></i>` tags.

### 5. Chaining Decorators

The real power of the decorator pattern is in **composition**. You can combine different decorators in any order to apply multiple formatting styles to the same text. Here’s how you can combine the decorators:

```python
# Start with plain text
my_text = PlainText("python")

# Bold and italicize the text
my_text = BoldTextDecorator(ItalicTextDecorator(my_text))

# Render the combined text
print(my_text.render())  # Output: <b><i>python</i></b>
```

In this example:
1. `PlainText("python")` creates a plain text object.
2. `ItalicTextDecorator(my_text)` adds italic formatting.
3. `BoldTextDecorator(my_text)` adds bold formatting to the italicized text.

Each decorator wraps the previous one, applying its specific formatting, and the final result is the text displayed with both bold and italic formatting.

### 6. Adding More Decorators (Underline)

We can easily add another decorator, such as an **UnderlineTextDecorator**, to underline the text:

```python
class UnderlineTextDecorator(PlainTextDecorator):
    def __init__(self, render):
        super().__init__(render)

    def render(self):
        return "<u>{}</u>".format(super().render())
```

This decorator works similarly to the `BoldTextDecorator` and `ItalicTextDecorator`, but it wraps the text in `<u></u>` tags to add underlining.

Now, let’s chain the decorators again to apply both italic and underline formatting:

```python
# Start with plain text
my_text = PlainText("python")

# Italicize and underline the text
my_text = UnderlineTextDecorator(ItalicTextDecorator(my_text))

# Render the combined text
print(my_text.render())  # Output: <u><i>python</i></u>
```

### 7. Summary of Benefits of the Decorator Pattern

- **Flexibility**: You can combine decorators in any order to apply different combinations of formatting.
- **Avoids Class Explosion**: You don’t need to create new classes for every possible combination of formatting (e.g., `BoldItalicText`, `ItalicUnderlineText`, etc.). Instead, you can compose behaviors dynamically.
- **Single Responsibility**: Each decorator focuses on a single responsibility (e.g., making text bold or italic), adhering to the Single Responsibility Principle (SRP).
- **Extensibility**: It is easy to add new formatting options without modifying existing code. You can simply create new decorators.

### Conclusion

By using the **Decorator Pattern**, you can dynamically add and combine different formatting styles to text objects without the need for a complex inheritance hierarchy. This approach is highly extensible and maintainable, allowing you to create more functionality by composing decorators rather than adding numerous subclasses.

## 8
The **Facade Design Pattern** is a structural pattern that aims to simplify interactions with a complex system by providing a unified interface. It hides the complexities of a subsystem behind a single, higher-level interface, making it easier for clients to interact with the system. This pattern is especially useful when dealing with large, complicated systems composed of multiple components, as it reduces the need for clients to understand or manage all the intricacies of these components.

### Key Concepts of the Facade Pattern

- **Simplification**: A facade provides a simple interface to a set of interfaces in a subsystem. Instead of interacting directly with all the various classes or modules in the system, clients only need to communicate with the facade, which internally manages the complexity.

- **Decoupling**: The client is decoupled from the complex subsystems, reducing its need to understand or manage the inner workings of the system. This abstraction makes the system easier to use and more maintainable.

- **Unification**: A facade offers a higher-level interface that encapsulates the interactions with various components, making them accessible through a single method or class.

### How the Facade Pattern Works

Imagine a scenario where a system consists of several microservices or individual components that work together to perform a task. Normally, a client would need to interact with each of these components directly, knowing which one to call and in what order. This can be cumbersome and error-prone.

In contrast, a facade pattern provides a **single entry point** for the client. Instead of managing all the interactions themselves, the client can simply invoke a high-level method provided by the facade, which then delegates the work to the relevant subsystem components in the right sequence.

### Example in E-Commerce

A common real-world analogy is the **customer service** department in an e-commerce company. Behind the scenes, there are various complex systems handling tasks like **order fulfillment**, **billing**, and **shipping**. Each of these systems might have their own set of complexities, such as inventory management, payment processing, and delivery tracking.

When a customer faces an issue or needs assistance, they don't contact the billing team, the shipping team, or the order fulfillment team directly. Instead, they call **customer service**, which acts as the **facade**. Customer service simplifies the process for the customer by hiding all the complexity of the backend systems, offering a single point of contact.

- **Without Facade**: The customer would need to know the right team to call for billing, order status, shipping updates, etc., and they would have to understand the individual systems.
- **With Facade**: The customer only interacts with the customer service department, which takes care of interacting with the necessary systems behind the scenes.

### Benefits of the Facade Pattern

1. **Simplifies Client Interaction**: Clients don’t need to know the details of the subsystem's internal workings. They just interact with a single unified interface.
   
2. **Decouples Clients from Subsystems**: The facade pattern reduces the dependencies between the client and the subsystem, which makes the code easier to maintain and extend.

3. **Improves Code Readability and Maintainability**: By abstracting the complexities of the subsystem, the facade makes the system more intuitive and easier to work with, both for clients and developers.

4. **Facilitates Reusability**: The same facade can be reused across different clients, ensuring that clients follow a consistent approach to interacting with the system.

### Example Diagram of the Facade Pattern

Here is a conceptual breakdown of how the facade pattern works:

1. **Subsystem Components**: These represent the complex system, such as microservices or internal modules that each perform specific tasks.
   
2. **Facade**: This component provides a simple, unified interface to the subsystem. Clients interact with the facade, which handles the interactions with the subsystem behind the scenes.

3. **Client**: The client interacts with the facade instead of directly with the individual subsystem components.

The client can choose to interact directly with the subsystem, but the facade offers a much simpler and more convenient approach.

### When to Use the Facade Pattern

- **When a system is complex**: If a system has many moving parts that need to be coordinated, the facade simplifies the interface by providing a higher-level API.
  
- **When you want to decouple clients from subsystems**: Facades help in abstracting away the complexities of the subsystem, allowing the client to focus only on the essential tasks.

- **When a client needs to use only a few functionalities**: If a client only needs a subset of the functionality provided by the subsystem, the facade can provide a simplified interface that exposes only the relevant features.

### Things to Watch Out For

- **Avoid Overloading the Facade**: While the facade should simplify interactions, it shouldn’t become too large or overly complex itself. If the facade takes on too many responsibilities, it can turn into a "god object" that becomes difficult to maintain.

- **Not a One-Size-Fits-All Solution**: The facade pattern should be used to simplify interaction with subsystems, but it’s important to maintain the flexibility for clients to interact directly with the subsystem when necessary.

### Conclusion

The **Facade Design Pattern** is a great way to simplify client interactions with a complex system. By offering a higher-level interface that encapsulates the complexities of subsystem components, the facade pattern improves usability, readability, and maintainability. However, it is important to avoid overloading the facade with too many responsibilities, as this can make the system harder to manage. The facade pattern strikes a balance between simplicity for the client and complexity in the subsystem, creating a clean and efficient design.

## 9
In this demo, we illustrate how the **Facade Design Pattern** simplifies interactions with a complex subsystem. The goal is to abstract away the details of a complex process, making it easier for clients to achieve their objectives without needing to deal with all the underlying complexities.

### Problem Breakdown: Tea Preparation
In this example, the **tea preparation process** is broken down into several granular steps, each represented by a class. The goal is to show how a facade can unify these steps into a simpler interface for the client.

1. **Granular Classes:**
   - **Water**: Adds water to the boiling pan.
   - **Milk**: Adds milk to the boiling pan (for milk tea).
   - **Sugar**: Adds sugar to the boiling pan (for sweet tea).
   - **TeaLeaves**: Adds tea leaves to the boiling pan.
   - **Boil**: Boils everything together for four minutes.

Each class has a method representing a specific step in the tea-making process.

```python
class Water:
    def adding_water(self):
        print("Water is added to the boiling pan")

class Milk:
    def adding_milk(self):
        print("Milk is added to the boiling pan")

class Sugar:
    def adding_sugar(self):
        print("Sugar is added to the boiling pan")

class TeaLeaves:
    def adding_tealeaves(self):
        print("Tea leaves are added to the boiling pan")

class Boil:
    def boiling(self):
        print("Boiling the mixture for 4 minutes")
```

These individual components represent the different **services** that are needed to prepare a variety of teas. Now, each service can be invoked individually, but managing all of them together can become cumbersome for the client.

### The Facade Class: Simplifying the Interface
To make it easier for clients to interact with this complex process, we create a **Facade class**. This class will provide high-level methods for preparing different kinds of tea without exposing the underlying complexity.

```python
class Tea:
    def __init__(self):
        self.__water = Water()
        self.__milk = Milk()
        self.__sugar = Sugar()
        self.__tealeaves = TeaLeaves()
        self.__boil = Boil()

    def prepare(self):
        self.__water.adding_water()
        self.__milk.adding_milk()
        self.__sugar.adding_sugar()
        self.__tealeaves.adding_tealeaves()
        self.__boil.boiling()
        print("Your tea is ready!")

    def prepare_black_tea(self):
        self.__water.adding_water()
        self.__tealeaves.adding_tealeaves()
        self.__boil.boiling()
        print("Your black tea is ready!")

    def prepare_sugarless_tea(self):
        self.__water.adding_water()
        self.__milk.adding_milk()
        self.__tealeaves.adding_tealeaves()
        self.__boil.boiling()
        print("Your sugarless tea is ready!")
```

- **`__init__()`**: Initializes the individual services (`Water`, `Milk`, `Sugar`, `TeaLeaves`, `Boil`).
- **`prepare()`**: Prepares **regular tea** (with water, milk, sugar, and tea leaves).
- **`prepare_black_tea()`**: Prepares **black tea** (without milk and sugar).
- **`prepare_sugarless_tea()`**: Prepares **sugarless tea** (without sugar).

### Client Interaction with the Facade

The **Facade** provides simple methods like `prepare()`, `prepare_black_tea()`, and `prepare_sugarless_tea()` to allow clients to specify their desired type of tea without needing to know about the individual components or how they interact.

Here’s how the client can use the `Tea` facade:

```python
morning_tea = Tea()
morning_tea.prepare()  # Prepares regular tea
morning_tea.prepare_black_tea()  # Prepares black tea
morning_tea.prepare_sugarless_tea()  # Prepares sugarless tea
```

### How the Facade Pattern Works:
- The **client** (in this case, `morning_tea`) interacts with the **facade** to achieve a specific outcome (tea preparation).
- The **facade** is responsible for managing all the internal details and interacting with the individual components (Water, Milk, Sugar, TeaLeaves, Boil) in the correct order.
- The client doesn't need to worry about the steps involved in tea preparation or the order in which the methods need to be called.

### Benefits:
- **Simplified Interface**: The client only needs to interact with the `Tea` facade, instead of calling methods on multiple classes.
- **Abstraction**: The complexity of how the tea is prepared is hidden from the client.
- **Flexibility**: Clients can still interact with individual components if they need more control, but the facade makes the process easier for common tasks.

This demo illustrates how the **Facade Design Pattern** can be used to manage a complex process (like tea preparation) by providing a simple, unified interface that hides all the underlying complexities.

## 10

In this video, we're discussing the **Proxy Design Pattern**, a structural pattern widely used in software development. The Proxy pattern introduces an intermediary object, called a **proxy**, that controls access to another object, often referred to as the **real subject**.

### What is a Proxy?
A **proxy** is essentially a **surrogate** or a **placeholder** for another object. Instead of interacting directly with the real object, the client interacts with the proxy. The proxy has the same interface as the real object, and it forwards the method calls to the real object while potentially adding additional behavior or controls (e.g., authentication, logging, or resource management).

The proxy pattern is particularly useful when:
- You want to control access to the real object, perhaps to add security checks or manage resources efficiently.
- You want to protect the client from the complexity of interacting directly with the real object.
- You need to introduce **indirection** in scenarios such as remote procedure calls, distributed systems, or heavy resource initialization.

### How the Proxy Pattern Works:
The proxy pattern involves the following components:
1. **Client**: This interacts with the **Subject** interface.
2. **Subject**: This is the interface that both the **Proxy** and the **RealSubject** implement. It defines the methods that the client can invoke (e.g., `do_something()`).
3. **Proxy**: This is the object that acts as an intermediary. The proxy typically performs additional work (e.g., checking authentication) before delegating the call to the real object.
4. **RealSubject**: This is the actual object that implements the core functionality.

#### Basic Flow:
- The **Client** calls a method on the **Subject** interface, which is implemented by the **Proxy**.
- The **Proxy** performs any necessary logic (e.g., access control, logging, lazy initialization) before forwarding the request to the **RealSubject**.
- The **RealSubject** performs the actual operation.
- The result is then passed back from the **RealSubject** to the **Proxy**, which forwards it to the client.

### Real-World Example:
A **payment system** is a great real-world example of a proxy. When making a payment, the actual transaction happens within your **bank account** (the **RealSubject**). However, you don't directly interact with your bank account. Instead, you use intermediaries like **credit cards**, **debit cards**, or **mobile payment apps** as proxies. These proxies manage communication with the bank (the **RealSubject**) on your behalf, ensuring that payment is made but abstracting away the direct access to the bank.

In this context:
- **Payment** is the **Subject** interface.
- **Credit Card**, **Debit Card**, or **Mobile App** serve as proxies.
- The **RealSubject** is your **bank account**, where the actual funds are deducted from.

### Example Visualization:
- The **Client** communicates with the **Subject** interface, typically using a proxy.
- The **Proxy** checks conditions like authentication and performs any necessary operations.
- The **Proxy** then delegates the call to the **RealSubject**, which performs the actual business logic.
- Finally, the **Proxy** returns the result back to the **Client**.

[Video description begins] A workflow diagram is displayed showing the four components: **Client → Subject → Proxy → RealSubject**. The arrows indicate the flow of communication between the components. [Video description ends]

### Use Cases for the Proxy Pattern:
- **Lazy Instantiation**: The proxy can instantiate a heavy resource (like a database connection or large object) only when it's actually needed.
- **Access Control**: Proxies can enforce security by checking if the client is authorized to access the real object.
- **Remote Access**: In distributed systems, a proxy can represent an object located on a remote server, abstracting the complexity of network communication.
- **Caching**: A proxy can cache results from the real object, providing faster responses for repeated calls.

### Conclusion:
The **Proxy Design Pattern** is a powerful tool for managing and controlling access to complex or resource-intensive objects. It allows you to introduce indirection, making it easier to manage remote interactions, access control, and other responsibilities without exposing the underlying complexities of the real object.

## 11
In this demo, we explore two practical examples of the **Proxy Design Pattern**. The **Proxy Pattern** is often used when interacting with remote systems or resources, allowing an intermediary (proxy) to control access to a real object, perform checks, or provide additional logic before delegating tasks to the real object.

### Example 1: Proxy for a Soccer Player

We start with a **SoccerPlayer** class:

```python
class SoccerPlayer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def play(self):
        print("Plays for a European club")
```

This class represents a soccer player with attributes `name` and `age`, and a `play()` method that prints a simple message indicating the player plays for a European club.

Next, we create a **ProxySoccerPlayer** class that acts as a proxy for the **SoccerPlayer**. The proxy will perform a check before allowing access to the `play()` method:

```python
class ProxySoccerPlayer:
    def __init__(self, name, age):
        self.__soccer_player = SoccerPlayer(name, age)

    def play(self):
        print("Checking if the player is of the minimum age")
        if self.__soccer_player.age >= 14:
            self.__soccer_player.play()
        else:
            print("Player is underage")
```

In this proxy:
- The `ProxySoccerPlayer` checks if the player's age is at least 14 before invoking the `play()` method on the real **SoccerPlayer** object.
- If the player is too young, a message is printed instead of allowing them to play.

#### Example Usage:
For an underage player (12 years old):

```python
proxy = ProxySoccerPlayer("Adam", 12)
proxy.play()  # Output: "Player is underage"
```

For a player who meets the age requirement (20 years old):

```python
proxy = ProxySoccerPlayer("Chris", 20)
proxy.play()  # Output: "Plays for a European club"
```

### Example 2: Proxy for Payment (Debit Card)

In the second example, we model a **BankAccount** system where a **DebitCard** acts as a proxy to make payments.

1. **Payment Interface**: First, we define an abstract base class `Payment`, which both **BankAccount** and **DebitCard** will implement.

```python
class Payment:
    def pay(self, amount):
        pass
```

2. **BankAccount**: The `BankAccount` class inherits from `Payment` and implements the `pay()` method. It also checks whether sufficient funds are available to process the payment:

```python
class BankAccount(Payment):
    def __init__(self, balance):
        self.__balance = balance
        self.__card = None
        
    def set_card(self, card):
        self.__card = card

    def __has_funds(self, amount):
        print("Checking whether funds are available")
        return amount <= self.__balance

    def pay(self, amount):
        if self.__has_funds(amount):
            print(f"Bank: paying the merchant {amount}")
            self.__balance -= amount
            return True
        else:
            print("Bank: payment declined, you don't have enough funds")
            return False
```

3. **DebitCard**: The `DebitCard` class acts as a proxy for the `BankAccount`. It allows the user to make payments by delegating the payment request to the `BankAccount`.

```python
class DebitCard(Payment):
    def __init__(self, bank_account):
        self.__bank_account = bank_account
        self.__bank_account.set_card(self)

    def pay(self, amount):
        return self.__bank_account.pay(amount)
```

#### Example Usage:

- First, we create a **BankAccount** with an initial balance of $1,000:

```python
bank_account = BankAccount(1000)
```

- Then, we associate a **DebitCard** with this bank account:

```python
debit_card = DebitCard(bank_account)
```

- When making a payment of $500:

```python
debit_card.pay(500)  # Output: "Bank: paying the merchant 500"
```

- Now, if the remaining balance is $500 and a second payment of $2,000 is attempted:

```python
debit_card.pay(2000)  # Output: "Bank: payment declined, you don't have enough funds"
```

### Key Takeaways:
- **Proxy** acts as an intermediary between the client and the real object, controlling access and adding additional functionality like checks or resource management.
- In the **SoccerPlayer** example, the proxy ensures that players are of the correct age before allowing them to play.
- In the **BankAccount** example, the proxy (debit card) delegates payment requests to the real bank account while enabling additional checks like balance verification.

The proxy pattern is a versatile and powerful design that helps to manage resources, provide security, and improve performance by controlling access to complex or heavy resources.

## 12
### Flyweight Design Pattern

The Flyweight design pattern is a structural pattern that optimizes the use of memory by sharing objects. It is particularly useful when dealing with a large number of objects that are lightweight and identical or similar. The goal is to reduce memory usage by sharing common states and only storing unique, mutable states.

### Key Concepts:
- **Resource Sharing:** The Flyweight pattern enables resource sharing to support large numbers of fine-grained objects.
- **Lightweight Objects:** Objects in the Flyweight pattern are small in size, and although each individual object is not memory-intensive, creating thousands of such objects can be inefficient.
  
### Practical Example: Strings in Python
- Strings, such as `"abc"` and `"abc"`, are typically identical and small, occupying only three bytes of memory. 
- Without the Flyweight pattern, each identical string could occupy separate memory locations, leading to unnecessary duplication and inefficient use of resources.
- Using the Flyweight pattern, identical strings can reference the same memory location, preventing duplication and saving memory.

### When to Use the Flyweight Pattern
- The pattern is most effective when creating thousands or millions of instances of objects that share common state.
- It is less useful when creating only a few instances, even if those objects are lightweight.

### Flyweight Pattern Structure:
1. **Flyweight Factory:** A factory that ensures shared state is maintained across objects. It checks if an object already exists and returns it, avoiding duplication.
2. **Flyweight Object:** These objects contain shareable state and expose necessary methods. The shared state is often stored in a cache.
3. **Client:** The client requests instances of Flyweight objects from the Factory and uses them.

### Example: Web Browser Image Caching
- When a user visits a website, images are downloaded and cached in the browser to reduce loading times on subsequent visits.
- If the same image is used across multiple pages, the browser reuses the image from the cache rather than downloading it again. This is an example of the Flyweight pattern in action, where the image resource is shared.

### Considerations:
- **Shallow vs. Deep Copying:** Flyweight pattern implementation requires understanding of shallow and deep copying. Shallow copies reference the same memory object, which can be overwritten by different references.
- **Immutability of Strings:** In Python, strings are immutable, which makes the Flyweight pattern easier to implement. Since strings cannot be modified, multiple references to the same string object can safely exist.

By using the Flyweight pattern, memory usage is optimized, especially when dealing with large numbers of objects that have common state.

## 13
### Flyweight Pattern Implementation for Grade Objects

The following code implements the Flyweight pattern for managing `Grade` objects. It ensures that objects with the same letter grade are reused rather than creating new instances for identical values.

#### Class Method for Reusing Grade Instances:
- **Reusing Existing Grade:**
  If a `Grade` object for a specific letter grade already exists, we print a message stating that the grade instance is being reused. This is done by checking the `__instance_dict` dictionary for the corresponding letter grade.
  
  ```python
  if letter in cls.__instance_dict:
      print('Reusing a previously created grade instance', letter)
  ```

- **Creating a New Grade:**
  If the grade for the letter hasn’t been created yet, a new `Grade` object is instantiated. The `super()` function is called to invoke the `__new__` method from the base class to create a new instance.

  ```python
  else:
      print('Creating new grade', letter)
      grade = super(Grade, cls).__new__(cls)
  ```

- **Assigning Grade Information:**
  After creating the new `Grade` object, we assign the calculated letter grade to the `__letter` member variable.

  ```python
  grade.__letter = letter
  ```

- **Storing Grade Object for Future Use:**
  The newly created `Grade` object is stored in the `__instance_dict` dictionary under the corresponding letter grade key, ensuring it can be reused later.

  ```python
  cls.__instance_dict[letter] = grade
  ```

- **Returning the Grade Object:**
  Finally, the method returns the `Grade` object, whether newly created or reused.

  ```python
  return cls.__instance_dict[letter]
  ```

#### Letter Grade Calculation:
- The `get_letter` class method is used to determine the letter grade based on a percentage score.

  ```python
  @classmethod
  def get_letter(cls, percent):
      if percent < 20:
          return 'F'
      if percent < 40:
          return 'D'
      if percent < 60:
          return 'C'
      if percent < 80:
          return 'B'
      if percent < 100:
          return 'A'
  ```

#### Student Class:
- The `Student` class takes a name and a percentage score, then instantiates a `Grade` object based on the score using the `get_grade` method.

#### Testing Flyweight Pattern:
- We create five students with different names: Adam, Bob, Charles, Dorian, and Eve.
- Adam, Charles, and Eve have the same grade (A), and Bob and Dorian share the same grade (B).
- When the `get_grade()` method is called for each student, the output will show that the same `Grade` object is reused for students with the same letter grade.

#### Output Confirmation:
- When we run the program, we observe that:
  - `Adam`, `Charles`, and `Eve` all reuse the same `Grade` object for grade A.
  - `Bob` and `Dorian` reuse the same `Grade` object for grade B.
  
  Additionally, we can confirm that the `Grade` object associated with each student is the same by comparing memory locations:

  ```python
  print(id(adam.get_grade()))  # Shows memory location for A grade
  print(id(charles.get_grade()))  # Same memory location for A grade
  print(id(eve.get_grade()))  # Same memory location for A grade
  ```

This confirms that the Flyweight pattern is effectively reusing `Grade` objects for the same letter grades.

