---
date: 1970-01-01T00:00:00Z
---

# Python Design Patterns Principles of Good Design

## 2

### Design Thinking in Programming

When you first start programming, it may seem difficult, but with practice, programming becomes intuitive. As you work on real-world projects and build more complex components, you’ll encounter new challenges. It's not just programming that can be challenging, but design thinking—how to structure, organize, and make components work together effectively. Good design thinking ensures that components are robust, maintainable, and scalable. This is where design patterns come in.

### What Are Design Patterns?

Design patterns are repeatable solutions to common problems in software design. Over time, developers have discovered best practices that address recurring issues, and these practices have been distilled into patterns that can be applied to different problems in various contexts. These patterns are not one-time solutions for specific use cases; they are adaptable and applicable to a variety of scenarios where the underlying problem is similar.

Design patterns help prevent reinventing the wheel by providing proven solutions. They allow developers to leverage the collective knowledge of experienced engineers and avoid the need to solve common problems from scratch. These patterns are based on principles that have been refined over decades of software development.

### Key Software Design Principles (SOLID)

The SOLID principles are foundational concepts for creating well-designed, maintainable code. These principles apply across different programming languages, such as Python, Java, or other object-oriented languages.

#### 1. **Single Responsibility Principle (SRP)**

A component or object should have only one reason to change, meaning it should be responsible for only one task. This principle helps avoid complex, bloated objects and ensures that the component has a clear, focused purpose.

#### 2. **Open/Closed Principle (OCP)**

Code should be open for extension but closed for modification. This means you can extend functionality without changing the existing code. Instead of rewriting code to accommodate new requirements, you extend it to handle new use cases.

#### 3. **Liskov Substitution Principle (LSP)**

Derived classes should be interchangeable with their base class without affecting the behavior of the system. Clients using a base class should be able to substitute any derived class without noticing a difference in behavior, ensuring consistency in the class hierarchy.

#### 4. **Interface Segregation Principle (ISP)**

An interface should be as specific as needed and not force clients to implement unnecessary methods. This principle ensures that interfaces are focused, with only the methods that clients actually need, avoiding overly broad or unwieldy contracts.

#### 5. **Dependency Inversion Principle (DIP)**

Higher-level components should not depend on lower-level components. Instead, both should depend on abstractions. This principle encourages decoupling, where components depend on interfaces or abstract classes rather than concrete implementations. This improves flexibility and maintainability.

### Conclusion

By following these principles and leveraging design patterns, developers can create software that is more maintainable, extensible, and robust. Design patterns and principles like SOLID guide developers to structure their code in a way that anticipates change and adapts to new requirements efficiently.

## 3
### Single Responsibility Principle (SRP)

The **Single Responsibility Principle (SRP)** states that a class or component should have only one responsibility. A class should focus on a single task or purpose and should not try to represent multiple entities or perform different functions. This ensures that the class remains focused, easy to understand, and maintainable.

For example, imagine a class that both handles user requests and connects to a database. If you need to change the way the class connects to the database, it could inadvertently affect how the class handles user requests because both responsibilities are mixed together. This makes the class harder to maintain and extend. By separating concerns and focusing on one responsibility per class, each class becomes more manageable and changes become more localized.

The SRP can also apply to components made up of multiple classes or services exposed through APIs. The component should not try to handle too many responsibilities; it should only handle one well-defined task.

### Open/Closed Principle (OCP)

The **Open/Closed Principle (OCP)** asserts that code should be **open for extension** but **closed for modification**. Once a class or component is written and tested, it should not require frequent changes to accommodate new functionality. Instead of modifying existing code, new functionality should be added by extending the code, such as creating new classes or components.

For example, once you have a class in place, you should not need to change its implementation to add new features. Instead, you should extend the class or create new derived classes that implement the new behavior. This can be achieved through inheritance, delegation, or composition.

#### Extending vs. Modifying Code

- **Extending code**: Create new classes or components that build on the existing functionality, often through inheritance or delegation. This avoids altering the original class and its logic.
  
- **Modifying code**: Involves changing the existing class, adding new variables, or altering methods, which can introduce errors and reduce maintainability.

For example, in an inheritance hierarchy, the base class provides the structure and common functionality, while derived classes implement specialized behavior. If new features are needed, you extend the base class with new derived classes instead of modifying the base class itself.

#### Techniques to Achieve OCP

1. **Inheritance**: Create a base class with abstract methods, and derive subclasses to implement specific functionality. This way, new behavior can be added without changing the original class.

2. **Delegation**: Rather than changing the original class, create new components that handle the new functionality. The original class can delegate responsibilities to these new components. A common approach is for the original class to fire events that trigger actions in the new components, a pattern seen in the **Observer** and **Chain of Responsibility** design patterns.

3. **Composition**: Use pluggable components, allowing new functionality to be added by substituting or composing new classes into the existing code. For example, the **Strategy** design pattern uses composition to specify different behaviors based on inputs, without modifying the original class.

By using these techniques—inheritance, delegation, and composition—you can extend your code and add new features without altering the existing code, maintaining flexibility and reducing the risk of errors.

## 4
### Liskov Substitution Principle (LSP)

The **Liskov Substitution Principle (LSP)** asserts that derived classes must be completely substitutable for their base classes without altering the expected behavior. This principle specifically applies to classes and inheritance hierarchies.

When you create an inheritance hierarchy, the **base class** defines a contract, specifying the behaviors and functions that derived classes should implement. According to LSP, you should be able to substitute an object of the base class with an object of any derived class without affecting the system’s behavior. 

For example, in an animal hierarchy with a `giveBirth` method, different derived classes (e.g., mammals, birds) can implement `giveBirth` differently (e.g., live birth vs. laying eggs), but the core idea of **birth** should remain the same. The derived class may change how the birth occurs, but it should not change the fundamental behavior defined by the base class. The derived class should not introduce entirely different functionality (e.g., locomotion or intelligence) in place of birth.

### Interface Segregation Principle (ISP)

The **Interface Segregation Principle (ISP)** states that clients should not be forced to implement methods they do not need. When designing software components, especially when defining interfaces, you should avoid creating large, unwieldy interfaces that combine unrelated behaviors. Instead, the interface should be small, modular, and cohesive, exposing only the methods relevant to a particular client or use case.

For example, if a service provides multiple unrelated functionalities, it is better to break these into smaller interfaces rather than combining them into one large interface. This ensures that clients are only required to implement the methods they need, avoiding unnecessary complexity and maintaining clean, maintainable code.

### Dependency Inversion Principle (DIP)

The **Dependency Inversion Principle (DIP)** emphasizes that high-level modules should not depend on low-level modules; both should depend on abstractions (e.g., interfaces or abstract base classes). It has two key aspects:

1. **Depend on abstractions, not implementations**: Clients should interact with interfaces, not concrete classes. For example, if a data structure like a stack is implemented using a list, you should interact with the stack interface and not the specific list implementation. This allows the implementation to change without affecting the clients.

2. **High-level modules should not depend on low-level modules**: In a typical scenario, higher-level components (e.g., a document editor) should not directly depend on lower-level components (e.g., a page renderer). Instead, both should depend on shared abstractions. For example, the `Document` interface should not directly reference the `Page` interface; the `Page` interface can reference `Document`, but not vice versa.

This principle ensures that the system is modular, flexible, and easier to maintain. By depending on abstractions, the system becomes more adaptable to changes in implementation while maintaining compatibility.

### Working with Abstractions

In the context of DIP, **abstractions** are typically implemented using abstract base classes or interfaces. These define a contract without specifying how the behavior is implemented. A **pure abstract base class** contains only method definitions, with no implementations, and acts as a true interface. For instance, in a shape hierarchy, an abstract `Shape` class might define methods like `calculateArea` and `calculatePerimeter`. Concrete classes like `Circle`, `Rectangle`, or `Triangle` would then implement these methods according to their specific requirements.

By programming to interfaces (abstractions) rather than implementations, you can swap out one concrete implementation for another without affecting the client code, ensuring that the system remains flexible and extensible.

### The Importance of Abstraction

An **interface** is the "surface" or contract exposed to the external world, outlining how a component interacts with others. The **implementation** refers to the internal details of how the component works—its actual code and logic. The Dependency Inversion Principle ensures that clients only depend on the interface (the surface), not the implementation (the internal details), allowing for easier updates and maintenance.

For example, when building a word processor, you might define a `Document` interface and a `Page` interface, each implemented by concrete classes. These interfaces can reference each other, but the implementation details of `Document` should not directly reference `Page`. This way, you can change the implementation of `Document` or `Page` independently without affecting each other, as long as they adhere to their interfaces.

By following the Dependency Inversion Principle, you ensure that high-level modules, like the document editor, do not depend on low-level modules, like page formatting, but both depend on abstractions. This allows for greater flexibility and scalability in your software architecture.

## 5
### Principle of Least Knowledge (Demeter's Law)

The **Principle of Least Knowledge**, also known as **Demeter's Law**, suggests that components in a software system should have minimal knowledge about other components. A component (class, function, etc.) should only communicate with **direct friends**, not with "friends of friends" or other distant components. The key idea is that each component should only interact with components that it directly depends on.

- **Friends**: These are components that are directly related to the current component and are safe to interact with. These might include:
  - **Method parameters**: Objects passed into methods that you need to interact with.
  - **Instantiated objects**: Objects created within a method or class and used locally.
  - **Global variables**: Common utilities or constants shared across the system.
  
The goal of this principle is to **reduce coupling** between components, which leads to a more maintainable, scalable, and flexible system. By adhering to this principle, your components are less dependent on each other and are therefore easier to modify or replace without causing disruptions elsewhere in the system.

### Hollywood Principle

The **Hollywood Principle** is encapsulated by the phrase: **"Don’t call us, we’ll call you."** This principle encourages high-level components (which are more abstract or general-purpose) to control the flow of execution and notify low-level components (which are more specific or granular) when necessary. This is a form of **inversion of control**.

In more detail:
- Low-level components can depend on high-level components but should **not call** high-level components directly.
- High-level components should **notify** low-level components of any changes or actions via **events or messages**.

This principle encourages **event-driven programming** and promotes loose coupling between components. It is often implemented using **event listeners**, where low-level components register themselves to be notified of specific events in the high-level component.

#### Example: Word Processor Design

In the context of a word processor:
- **Document** (high-level component) and **Page** (low-level component) can communicate.
- **Page** should not call or directly invoke functions in the **Document** class to check for changes or updates.
- Instead, the **Document** can notify the **Page** whenever a change happens (e.g., margin changes) through events or messages. 
  - The **Page** registers as an event listener, and whenever the **Document** changes, it sends a notification to all registered **Page** instances, which then adjust their layout accordingly.

This mechanism ensures that:
- The **Document** controls the flow and notifies the **Page** when necessary (following the Hollywood Principle).
- The **Page** can act independently without needing to constantly check the **Document**, ensuring loose coupling.

### The Relationship with Dependency Inversion Principle (DIP)

The **Hollywood Principle** is closely related to the **Dependency Inversion Principle** (DIP), which suggests that high-level modules should not depend on low-level modules but both should depend on abstractions. In the case of the Hollywood Principle:
- The **Page** (low-level component) depends on the **Document** (high-level component) to be notified of changes.
- However, the **Page** does not actively invoke methods on the **Document**. Instead, it listens for events, allowing the **Document** to drive changes.

By combining **DIP** and the **Hollywood Principle**, you ensure that the system is designed in such a way that the high-level components dictate the flow, while low-level components remain flexible and reactive to changes without tight coupling.

### Benefits of the Hollywood Principle
- **Loose Coupling**: The low-level component is decoupled from the high-level component because it does not need to call the high-level component directly. It only responds to notifications or events.
- **Flexibility**: The system can evolve more easily. High-level components can change their implementation without affecting the low-level components, as long as the event-based communication mechanism remains intact.
- **Reactivity**: Low-level components can react to changes in high-level components asynchronously, which is especially useful in systems where changes happen over time or asynchronously, like in UI frameworks or event-driven architectures.

### Summary
1. **Principle of Least Knowledge (Demeter's Law)**: Limit the knowledge of components to only what is absolutely necessary. A component should only communicate with its direct "friends" to reduce coupling.
   
2. **Hollywood Principle**: High-level components control the flow and notify low-level components of changes. Low-level components should listen for events or messages from high-level components rather than calling high-level components directly.

Both principles aim to make software systems **loose**, **flexible**, and **maintainable** by promoting **low coupling** and **high cohesion**. These principles help in building systems that are easier to modify, extend, and debug.

## 6
In this demo, the focus is on **implementing the Single Responsibility Principle (SRP)** for better class design, which is one of the key **SOLID** principles. Let's break down the concepts discussed in the video:

### The Problem with the Original Design

The initial `Employee` class violates the **Single Responsibility Principle**. It does too many things:
- It stores details about the employee.
- It handles promotions, transfers, and updates.
- It performs database operations like saving data and updating records.

This design is problematic because the `Employee` class has multiple responsibilities, making it harder to maintain and extend. For example, if the database implementation changes (e.g., switching from MySQL to PostgreSQL), the `Employee` class would need to be updated, even though its core responsibility is just to represent an employee. Additionally, adding new responsibilities to this class could make it increasingly difficult to maintain or modify, leading to a **fragile** design.

### Applying the Single Responsibility Principle

To address these issues, we refactor the design to follow SRP, ensuring that each class has only one responsibility. This leads to more modular, maintainable, and extensible code. Here's how the design is improved:

1. **Employee Class**:
   The `Employee` class is now focused solely on representing the details of an employee. It stores the employee's ID, name, and the department to which they belong. It does not handle promotions, transfers, or database operations.

   ```python
   class Employee:
       def __init__(self, employee_id, name, department):
           self.__employee_id = employee_id
           self.__name = name
           self.__department = department

       def get_name(self):
           return self.__name

       def get_department(self):
           return self.__department
   ```

   - The `Employee` class now has only one responsibility: managing the employee's personal details (ID, name, and department).
   - The `get_name` and `get_department` methods are simple getters to access these details.

2. **Department Class**:
   The `Department` class is responsible for handling information specific to a department, such as its name, function, and the head of the department. This class doesn't need to know about employees or database operations, and it follows SRP.

   ```python
   class Department:
       def __init__(self, department_id, name, function, head):
           self.__department_id = department_id
           self.__name = name
           self.__function = function
           self.__head = head

       def get_name(self):
           return self.__name
       
       def get_head(self):
           return self.__head
   ```

   - The `Department` class is only concerned with the department's attributes. It doesn't have to handle anything unrelated to a department's role in the organization.

3. **EmployeeDatabaseOperations Class**:
   The responsibility of handling database operations (like saving, updating, promoting, or transferring employees) is moved into a separate class called `EmployeeDatabaseOperations`. This class deals with interactions between the employee data and the database, following the SRP by ensuring that the database-related logic is isolated from the core business logic (i.e., the `Employee` and `Department` classes).

   ```python
   class EmployeeDatabaseOperations:
       def promote_employee(self, employee_id):
           # code to promote employee in the database
           pass

       def transfer_employee(self, employee_id, department):
           # code to transfer employee to a new department in the database
           pass

       def save_to_database(self, employee_id, personal_details):
           # code to save employee details to the database
           pass

       def update_personal_details(self, employee_id, personal_details):
           # code to update employee details in the database
           pass
   ```

   - The `EmployeeDatabaseOperations` class is dedicated solely to database operations, allowing database changes (e.g., changing from MySQL to PostgreSQL) to be isolated to this class. If the database logic changes, the `Employee` or `Department` classes do not need to be modified.

### Benefits of Following SRP

By splitting responsibilities across different classes, we achieve several benefits:
- **Maintainability**: Each class has a clear, single responsibility, making it easier to modify or extend. For example, changing how employee details are saved (e.g., changing database types) only requires modification in the `EmployeeDatabaseOperations` class.
- **Testability**: With separate responsibilities, each class can be tested independently. The `Employee` class can be tested for its core functionality (e.g., getting employee details), while the `EmployeeDatabaseOperations` class can be tested for its database interactions.
- **Flexibility**: Changes to one area of the application (e.g., adding new database functionality or modifying department details) will have minimal impact on other parts of the system, reducing the risk of unintended side effects.

### Summary

To implement the **Single Responsibility Principle**:
1. **Identify classes that are doing too much** (e.g., the original `Employee` class).
2. **Separate concerns** by creating classes dedicated to distinct responsibilities (e.g., separating `Employee` data management, department details, and database operations).
3. This results in code that is easier to **maintain**, **extend**, and **test**, as each class has a **single responsibility** and is decoupled from other areas of the system.

By following SRP, you create a more organized and robust system, making your codebase easier to manage in the long term.

## 7
In this example, the **Single Responsibility Principle (SRP)** is applied to a system of shape objects, improving the design by separating concerns and ensuring each class is responsible for only one thing.

### The Problem with the Original Design

Initially, we have a `Shape` class and a `Rectangle` class that inherits from `Shape`. The `Shape` class has the following methods:
- **`get_type()`**: returns the shape type (e.g., "Rectangle").
- **`get_area()`**: calculates and returns the area of the shape.
- **`draw()`**: draws the shape (which means interacting with the drawing library).

The issue is with the **`draw()`** method in the `Shape` class. **Drawing** is a complex task that involves different tools and libraries depending on where the shape is being rendered (e.g., web, desktop, mobile). The `Shape` class should not be concerned with the mechanics of drawing because it's outside the scope of its responsibility. 

By including drawing functionality in the `Shape` class, the design violates the **Single Responsibility Principle**, which states that a class should have one responsibility.

### Refactoring to Follow SRP

To fix this, we separate the **drawing responsibility** from the shape classes into a **new `DrawingTool` class**. Here’s the refactor:

1. **DrawingTool Class**: This class is responsible for interfacing with the drawing library, abstracting away the complexity of drawing the shape.
   ```python
   class DrawingTool:
       def __init__(self, shape):
           self.__shape = shape

       def draw_shape(self):
           print('Interface with the drawing library to draw any shape:', self.__shape.get_type())
   ```

   - The `DrawingTool` class takes a `shape` object as a parameter and knows how to draw that shape using the appropriate library. The `draw_shape()` method will print a message (simulating the drawing process).
   
2. **Shape Class**: The `Shape` class now holds a `DrawingTool` object and delegates drawing to the `DrawingTool`, rather than directly handling drawing itself.
   ```python
   class Shape:
       def __init__(self, shape_type):
           self.__shape_type = shape_type
           self.__drawing_tool = DrawingTool(self)

       def get_type(self):
           return self.__shape_type

       def draw(self):
           self.__drawing_tool.draw_shape()

       def get_area(self):
           pass  # The child class will override this.
   ```

   - The `Shape` class only stores basic shape information (`shape_type`) and has a reference to a `DrawingTool`.
   - The `draw()` method now delegates drawing to the `DrawingTool` using `self.__drawing_tool.draw_shape()`. This way, drawing mechanics are **abstracted away**.

3. **Rectangle Class**: The `Rectangle` class derives from `Shape` and is responsible only for the attributes specific to the rectangle (like width and height), and for calculating its area.
   ```python
   class Rectangle(Shape):
       def __init__(self, width, height):
           Shape.__init__(self, "Rectangle")
           self.__width = width
           self.__height = height

       def get_area(self):
           return self.__width * self.__height
   ```

   - The `Rectangle` class no longer needs to know about how to draw itself. It only needs to implement the area calculation (`get_area`).

### Key Points After Refactoring

- **Separation of Concerns**: The `Shape` class is responsible only for managing shape-related attributes (like `shape_type`). It does not handle drawing.
- **Drawing Responsibility Is Abstracted**: The responsibility for drawing shapes is moved to the `DrawingTool` class. This class knows how to interface with drawing libraries but doesn’t concern itself with shape-specific logic.
- **Simplified Inheritance**: The `Rectangle` class and other shapes can focus solely on their geometric properties and how to compute their areas, leaving drawing concerns to the `DrawingTool`.

### Final Example in Action

Let's see how this works in code:

1. **Create a Rectangle**:
   ```python
   a = Rectangle(5, 6)
   ```

2. **Get the Shape Type**:
   ```python
   print(a.get_type())  # Output: Rectangle
   ```

3. **Calculate the Area**:
   ```python
   print(a.get_area())  # Output: 30 (5 * 6)
   ```

4. **Draw the Shape**:
   ```python
   a.draw()  # Output: Interface with the drawing library to draw any shape: Rectangle
   ```

### Benefits of This Design

- **SRP Compliance**: Each class now has a single responsibility:
  - `Shape`: Handles shape-specific information.
  - `DrawingTool`: Handles the drawing of shapes.
  - `Rectangle`: Handles specific attributes (like width and height) and area calculations.
  
- **Maintainability**: If we need to change the drawing mechanism (e.g., switching from a canvas to a 3D renderer), we only need to modify the `DrawingTool` class. The shape logic remains unaffected.
  
- **Flexibility**: New shapes (e.g., `Circle`, `Triangle`) can easily be added by inheriting from `Shape`, and they can still be drawn using the same `DrawingTool` without needing to change the drawing logic in each shape class.

### Conclusion

By following the **Single Responsibility Principle** in this example, we've created a cleaner, more modular design where each class has a well-defined responsibility. The `Shape` class manages shape attributes, the `DrawingTool` class handles drawing, and each shape class is focused on its specific properties and behaviors. This separation of concerns improves code clarity, maintainability, and flexibility.

## 8
In this demonstration, the focus is on implementing the **Open/Closed Principle (OCP)**, one of the key principles in SOLID design. The **Open/Closed Principle** states that a class should be **open for extension**, but **closed for modification**. This means that while you can extend the functionality of a class (e.g., by adding new features or capabilities), you should not have to modify the existing code to do so. In other words, your code should be designed in such a way that adding new functionality can be done without changing the existing, working parts of the codebase.

Let's break down the initial problem and refactor it step by step to comply with the Open/Closed Principle.

### Initial Design (Violation of OCP)

We begin with a basic design where we have an `Employee` class and a function `get_department()` that checks which department an employee belongs to based on a hard-coded list of department names. Here’s the initial setup:

#### Employee Class
```python
class Employee:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```
- This class only holds the name of the employee. It’s simple, but lacks the ability to associate employees with departments in a scalable way.

#### Departments as Lists
Initially, departments are just lists containing employee names:
```python
accounts = ['Bob']
marketing = ['Charles']
```

#### The `get_department` Function
This function determines the department an employee belongs to by checking their name against predefined department lists.
```python
def get_department(employee):
    if employee.get_name() in accounts:
        print('accounts')
    elif employee.get_name() in marketing:
        print('marketing')
```
The problem with this design:
- **Lack of flexibility**: If a new department is added (e.g., "Finance"), we must modify the `get_department` function to include new checks. This violates the **Open/Closed Principle** because the code needs to be **modified** each time a new department is added, rather than being able to extend the functionality without modifying the existing code.

### Refactoring for Open/Closed Principle

We can refactor this design so that it is **open for extension** (i.e., adding new departments can be done easily) but **closed for modification** (i.e., we don’t need to change existing code when adding a new department).

#### Step 1: Represent Departments as Classes

Instead of using simple lists to represent departments, we can create a `Department` class that holds employee data and functionality.

```python
class Department:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    def get_name(self):
        return self.__name

    def get_employees(self):
        return self.__employees

    def add_employee(self, employee):
        self.__employees.append(employee.get_name())
```
- The `Department` class encapsulates department-specific data like the department name and employee list.
- The `add_employee` method allows adding employees to the department.

#### Step 2: Update the `Employee` Class

Now, the `Employee` class will hold a reference to a `Department` object, rather than just a name. It will also provide a method to get the department’s name.

```python
class Employee:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department
        department.add_employee(self)

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department.get_name()
```
- The `Employee` constructor now takes a `department` object, which is used to associate the employee with a department.
- The `get_department()` method calls the `get_name()` method on the department object to retrieve the department name.

#### Step 3: Creating and Managing Departments and Employees

We can now create departments and employees without modifying the existing code. Adding a new department is as simple as creating a new `Department` object and linking employees to it.

```python
# Creating department objects
accounts = Department('Accounts')
marketing = Department('Marketing')
finance = Department('Finance')

# Creating employee objects and associating them with departments
emp_bob = Employee('Bob', accounts)
emp_charles = Employee('Charles', marketing)
emp_alice = Employee('Alice', finance)

# Retrieving employee department info
print(emp_bob.get_department())  # Output: Accounts
print(emp_charles.get_department())  # Output: Marketing
print(emp_alice.get_department())  # Output: Finance

# Retrieving list of employees in each department
print(accounts.get_employees())  # Output: ['Bob']
print(marketing.get_employees())  # Output: ['Charles']
print(finance.get_employees())  # Output: ['Alice']
```

### Key Changes:
1. **Departments as Objects**: Departments are now instances of the `Department` class. Each department can hold its own list of employees and add new ones dynamically.
2. **No Need to Modify Code for New Departments**: To add a new department, you simply create a new `Department` instance and link employees to it. No changes are needed in the `Employee` class or the department-handling logic.
3. **Open for Extension, Closed for Modification**: The system is **open for extension** because new departments can be added without modifying any existing classes. It's **closed for modification** because the existing code (e.g., the `Employee` and `Department` classes) doesn’t need to change when new departments are added.

### Conclusion

In this refactor, we applied the **Open/Closed Principle** by using object-oriented design techniques, such as **composition** (linking employees and departments), and making the system extensible without changing the existing code. By encapsulating department logic within a `Department` class, we ensured that new functionality (like adding new departments) can be introduced without altering the already implemented `Employee` or `Department` classes.

This approach makes the code more maintainable, scalable, and adherent to SOLID principles, particularly the **Open/Closed Principle**.

## 9
In this demo, the focus is on **Liskov's Substitution Principle (LSP)**, which is the "L" in the SOLID principles. The Liskov Substitution Principle states that derived classes should be replaceable with their base class without altering the correct behavior of the program. In simple terms, you should be able to substitute a derived class object wherever a base class object is used, and it should behave as expected.

### The Example Code Breakdown

1. **Base Class: `Shape`**

    ```python
    class Shape:
        def __init__(self, shape_type):
            self.__shape_type = shape_type
        def get_type(self):
            return self.__shape_type
        def draw(self):
            pass
        def get_area(self):
            pass
    ```

    The base class `Shape` has three methods:
    - `get_type`: Returns the type of shape.
    - `draw`: This is a placeholder method that should be overridden by derived classes to define how a shape is drawn.
    - `get_area`: A placeholder for calculating the area of the shape.

    **Goal**: Every derived class must override `draw` and `get_area`, but must maintain the same signature as defined in `Shape`.

2. **Derived Class: `Rectangle`**
   
    ```python
    class Rectangle(Shape):
        def __init__(self, width, height):
            Shape.__init__(self, "Rectangle")
            self.__width = width
            self.__height = height
        def draw(self):
            print("Imagine that this draws a rectangle")
        def get_area(self):
            return self.__width * self.__height
    ```

    The `Rectangle` class inherits from `Shape`. It:
    - Calls the `Shape` constructor with `"Rectangle"` as the type.
    - Implements the `draw` method to draw a rectangle.
    - Implements the `get_area` method to calculate the area of the rectangle.

    The `Rectangle` class is a **valid substitute** for `Shape` because:
    - It correctly implements the methods `draw` and `get_area` with the same signatures.
    - You can use a `Rectangle` object anywhere a `Shape` object is expected.

3. **Derived Class: `VeryComplicatedShape` (Problematic)**

    ```python
    class VeryComplicatedShape(Shape):
        def __init__(self):
            Shape.__init__(self, "VeryComplicatedShape")
        def draw(self, complicated_drawing_tool):
            if complicated_drawing_tool is None:
                raise AssertionError("Cannot draw this shape!")
            else:
                print("Imagine we use the complicated tool to draw this shape")
        def get_area(self):
            raise AssertionError("Cannot calculate the area of this shape!")
    ```

    The `VeryComplicatedShape` class does not follow LSP:
    - It **overrides** the `draw` method but **adds an additional parameter** (`complicated_drawing_tool`) that doesn't exist in the base class.
    - It **raises an error** in `get_area`, which is inconsistent with the base class's contract of calculating area.

    This class is **not a good substitute** for `Shape` because:
    - The `draw` method has a different signature, requiring a new parameter (`complicated_drawing_tool`), making it incompatible with the base class's `draw` method.
    - It raises an error in `get_area`, violating the expectation that the method should return a value (or raise a `NotImplementedError`, rather than an error).
    - Using `VeryComplicatedShape` would require special handling (e.g., checking for specific arguments in the `draw` method), which violates LSP.

4. **Derived Class: `Line`**

    ```python
    class Line(Shape):
        def __init__(self, length):
            Shape.__init__(self, "Line")
            self.__length = length
        def draw(self):
            print("Imagine that this draws a line")
        def get_area(self):
            raise AssertionError("No area for line!")
    ```

    The `Line` class is a valid (though not perfect) substitute for `Shape`:
    - It correctly implements the `draw` and `get_area` methods with the same signature as the base class.
    - However, `get_area` raises an `AssertionError` because a line has no area, which is somewhat of a design flaw but still respects the method signature.

    The `Line` class **technically conforms to LSP**, since it maintains the same method signatures. The issue here is with how the functionality behaves (i.e., it throws an error when trying to calculate area), but its behavior can still be substituted for `Shape`.

5. **Custom Function to Draw Shapes (`draw_shape`)**

    ```python
    def draw_shape(shape, complicated_drawing_tool=None):
        if isinstance(shape, VeryComplicatedShape):
            shape.draw(complicated_drawing_tool)
        else:
            shape.draw()
    ```

    This function tries to draw any shape, but because `VeryComplicatedShape` has a different method signature (`draw(complicated_drawing_tool)`), the function must check the type of the shape and handle it differently. This approach:
    - Violates **Liskov's Substitution Principle** because now the code has to know about specific shape types (e.g., `VeryComplicatedShape`), making it difficult to maintain and extend.

6. **Custom Function to Get Area (`get_area`)**

    ```python
    def get_area(shape):
        return shape.get_area()
    ```

    This function is cleaner because it works for any shape that follows the base class contract. Even though `Line` and `VeryComplicatedShape` may raise errors in `get_area`, their method signatures still conform to the base class, so the function is valid for all shapes.

### Conclusion

- **Liskov's Substitution Principle (LSP)** ensures that derived classes can be used interchangeably with their base class without breaking the behavior of the system.
- Derived classes like `Rectangle` and `Line` follow LSP because their method signatures match the base class's and they don't introduce unexpected behaviors.
- The `VeryComplicatedShape` class violates LSP by changing the method signature and introducing behavior that breaks the expectations set by the base class, such as the requirement for additional arguments and raising errors unexpectedly.
- To follow LSP, all derived classes should adhere strictly to the method signatures and contracts defined by their base classes, ensuring substitutability without surprises.

## 10
In this demo, we explore the **Interface Segregation Principle** (ISP), represented by the **I** in the **S.O.L.I.D** acronym, which states that "clients should not depend on interfaces they do not use." The principle advocates for designing interfaces that are specific, granular, and focused on the tasks they are meant to serve, rather than broad, monolithic interfaces that require clients to implement methods they don't need.

### Step-by-step breakdown:

1. **Granular Interfaces**:
   The demo starts by creating several small interfaces (represented by classes in Python) that describe individual characteristics of animals:
   - **Flying**: Defines the method `fly()`.
   - **Swimming**: Defines the method `swim()`.
   - **Feeding**: Defines the method `feed()`.
   - **Birthing**: Defines the method `birth()`.

   These interfaces allow the flexibility to assign only the relevant behaviors to specific animals without forcing them to implement unnecessary methods.

2. **Creating Custom Functions**:
   Functions like `make_fly()`, `eat_food()`, `give_birth()`, and `make_swim()` are created to call the respective methods from the relevant interfaces. For instance, `make_fly()` will call the `fly()` method on an object that implements the `Flying` interface.

3. **Inheritance and Composition**:
   Animals such as **Eagle** and **Dolphin** are defined by inheriting only the interfaces relevant to them. 
   - An **Eagle** is a flying, feeding, and birthing animal, but does not swim, so it does not inherit the `Swimming` interface.
   - A **Dolphin** can swim, feed, and give birth, but it does not fly, so it doesn't inherit from the `Flying` interface.

   This demonstrates how clients (or derived classes) should only inherit the methods they need, adhering to the ISP.

4. **Example of Misuse of ISP**:
   The **Mammal** class demonstrates a poor design by forcing all mammals to implement methods for locomotion (aerial, aquatic, terrestrial) even if they don’t need them. This violates the ISP because a flying mammal (e.g., bat) must still implement methods related to swimming or terrestrial movement, even though it will never use them. 

5. **Fixing the Design**:
   To fix this, the `Mammal` class is refactored to only include a **single method** `locomotion()`, which each subclass (like `Human`, `Bat`, and `Dolphin`) then overrides with a meaningful implementation specific to the locomotion style of that animal:
   - **Human**: Implements `locomotion()` to print "humans are bipeds."
   - **Bat**: Implements `locomotion()` to print "bats are the only mammals that can truly fly."
   - **Dolphin**: Implements `locomotion()` to print "dolphins are marine mammals."

   This refactor adheres to the Interface Segregation Principle because each class is now only concerned with the methods that are relevant to it.

### Key Takeaways:
- **Granular Interfaces**: It's crucial to avoid large, bloated interfaces that require clients to implement methods they don't need.
- **Single Responsibility**: Each interface should serve one purpose (e.g., flying, swimming, etc.).
- **Flexibility**: By having specialized interfaces, you can create flexible and maintainable code where derived classes only implement the methods that make sense for them.
- **Refactor when needed**: If you find that your interfaces are becoming overly complex and forcing unnecessary behavior on classes, refactor them into smaller, more manageable ones.

## 11
In this demo, we learn how to apply the **Dependency Inversion Principle (DIP)**, which is part of the **S.O.L.I.D** design principles. The core idea of DIP is that **high-level modules should not depend on low-level modules**; instead, both should depend on abstractions. This helps decouple components and leads to more maintainable and flexible code.

### Step-by-step breakdown of the Dependency Inversion Principle (DIP):

1. **Initial Design that Violates DIP**:
   - We start with an **Organization** class that directly manages three specific departments: **Operations**, **Finance**, and **Human Resources**. The `Organization` class contains explicit methods (`add_ops`, `add_finance`, and `add_hr`) to add each department individually.
   - This is an example of violating DIP because:
     - The `Organization` class is a **high-level module** that is tightly coupled to the **low-level modules** (the specific departments).
     - The `Organization` class needs to be updated every time a new department is added, which violates the principle that high-level modules should not depend on low-level details.

2. **Creating Department Classes**:
   - We create three concrete department classes: `Operations`, `Finance`, and `HumanResources`, each with a constructor (`__init__`) that prints a message when the department is created. These departments are then manually added to the `Organization` instance.

3. **Problems with this Approach**:
   - The `Organization` class is tightly coupled to specific department types (e.g., `Operations`, `Finance`, `HumanResources`), making the code less flexible and harder to maintain.
   - If a new department type is introduced, we would need to update the `Organization` class, violating the **open/closed principle** (a part of S.O.L.I.D, which states that classes should be open for extension but closed for modification).

4. **Refactoring to Follow DIP**:
   - The goal is to decouple the `Organization` class from specific department types. To do this, we introduce a more **abstract** concept of a `Department` class:
     - A new `Department` class is created with a name and a reference to the `Organization` to which the department belongs.
     - The `Department` class defines a `do_work()` method (as a placeholder for the department's tasks) and a `get_name()` method to return the department's name.
     - The `Department` class will serve as a base class for all departments.

5. **Updating the Organization Class**:
   - The `Organization` class is refactored to no longer be aware of specific department types. Instead, it has a general `add_department()` method to add any department (not just specific ones like operations, finance, etc.).
   - The `Organization` class now only depends on the abstract `Department` class (through the `add_department()` method), not on specific department types. This is in line with the Dependency Inversion Principle.

6. **Creating Concrete Department Subclasses**:
   - Specific department types like **Operations**, **Finance**, and **HumanResources** are now subclasses of the general `Department` class.
   - Each subclass initializes the department's name and calls the `Department` constructor with the `organization` reference.
   - Each subclass provides a custom implementation for the `do_work()` method, indicating what each department does.

7. **Working Example**:
   - We instantiate an `Organization` object, and then create department objects (like `Operations`, `Finance`, and `HumanResources`) by passing the `Organization` object to their constructors.
   - When a department is instantiated, it automatically registers itself with the `Organization` through the `add_department()` method, ensuring the department is part of the organization without the `Organization` class being aware of the specific department type.
   - This setup ensures that **both the high-level module (Organization) and low-level modules (Departments) depend on abstractions** (`Department`), following the Dependency Inversion Principle.

### Benefits of This Design:
- **Flexibility**: The `Organization` class is no longer tightly coupled to specific department types. If a new department type is introduced, we can simply create a new subclass of `Department` without modifying the `Organization` class.
- **Maintainability**: The code is easier to maintain because changes to department types no longer require changes in the high-level `Organization` class.
- **Extensibility**: The design is open for extension (new department types can be added easily) but closed for modification (we don't need to change existing code in `Organization`).

### Key Takeaways:
- **High-level modules** should not depend on **low-level modules**. Both should depend on abstractions.
- **Abstractions** allow for decoupling components, which improves flexibility, maintainability, and testability.
- **Dependency Inversion** makes the system more modular, as you can add new components (like departments) without changing the core logic of the system (the `Organization` class).

## 12
In this section, we're learning about the three main categories of design patterns: **Creational**, **Structural**, and **Behavioral**. These design patterns help solve common problems in software design and improve maintainability, flexibility, and extensibility. Let's break down each category and understand what they focus on and when to use them.

### 1. **Creational Design Patterns**
   - **Purpose**: These patterns focus on object creation, specifically how objects are instantiated and how the complexities of their creation can be abstracted from the client. The goal is to provide a flexible and efficient way to create objects while hiding the details of their construction.
   - **Key Concepts**:
     - **Abstraction of Creation**: Creational patterns hide the implementation details of object creation, making it easier for clients to work with objects without worrying about how they are created.
     - **Lazy Instantiation**: Objects can be created only when needed, saving resources and improving performance.
     - **Families of Related Objects**: These patterns allow you to create families of related objects that can be used together, avoiding tight coupling between the objects and the client.
     - **Finite Object Instances**: In cases where limited instances of a class are needed (e.g., a Singleton), creational patterns can enforce this limitation.

   - **Use Cases**: 
     - When object creation is complex or requires multiple steps.
     - When you need to ensure that only a limited number of instances of a class exist (e.g., Singleton).
     - When you want to defer object creation until the object is actually needed (lazy instantiation).

   - **Examples** of Creational Patterns:
     - **Singleton Pattern**: Ensures a class has only one instance and provides a global point of access to it.
     - **Factory Pattern**: Creates objects without specifying the exact class of the object that will be created.
     - **Abstract Factory Pattern**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

### 2. **Structural Design Patterns**
   - **Purpose**: Structural patterns deal with how classes and objects are composed to form larger structures. They focus on relationships between components and how they can be organized to create complex systems that are still easy to maintain and extend.
   - **Key Concepts**:
     - **Composition and Inheritance**: These patterns emphasize how components can be composed or extended using inheritance to create complex structures.
     - **Relationships**: They express how components or classes relate to each other and ensure that changes in one part of the system do not negatively impact others.
     - **Maintainability and Flexibility**: By defining clear relationships between components, structural patterns ensure that changes are localized and don't affect the entire system.

   - **Use Cases**:
     - When you need to organize or structure complex systems of objects.
     - When you want to simplify the relationships between objects to ensure the system remains flexible and maintainable.
     - When you need to manage interdependent objects in a way that they can evolve without breaking other parts of the system.

   - **Examples** of Structural Patterns:
     - **Adapter Pattern**: Allows incompatible interfaces to work together by providing a wrapper that translates between the interfaces.
     - **Composite Pattern**: Lets clients treat individual objects and compositions of objects uniformly. It is used when you need to represent part-whole hierarchies.
     - **Facade Pattern**: Provides a simplified interface to a complex subsystem, making it easier for clients to interact with the system.

### 3. **Behavioral Design Patterns**
   - **Purpose**: These patterns focus on the interaction and communication between objects. They define how objects interact with each other, what responsibilities they have, and how they should respond to external requests.
   - **Key Concepts**:
     - **Loose Coupling**: Behavioral patterns aim to reduce dependencies between objects, allowing them to interact without tightly coupling them together. This enables each component to be worked on independently.
     - **Communication**: These patterns define how objects should communicate with each other in a way that is consistent, predictable, and maintainable.
     - **Responsibility**: Behavioral patterns ensure that each object has a clear responsibility and performs its duties as defined by its role.

   - **Use Cases**:
     - When you want to define how objects interact and communicate with each other in a flexible way.
     - When you need to manage complex workflows or sequences of actions.
     - When interactions between objects need to be flexible or loosely coupled to prevent tight dependencies.

   - **Examples** of Behavioral Patterns:
     - **Observer Pattern**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependent objects are notified and updated automatically.
     - **Strategy Pattern**: Allows a client to choose an algorithm from a family of algorithms at runtime, encapsulating each one and making them interchangeable.
     - **Command Pattern**: Encapsulates a request as an object, allowing for parameterization of clients with queues, requests, and operations.

### Summary:
- **Creational Design Patterns**: Deal with how objects are created. They abstract away the complexity of object construction and allow for flexible, efficient creation mechanisms.
- **Structural Design Patterns**: Focus on how objects and classes are organized and how they relate to one another. They simplify the relationships between components, ensuring maintainability and flexibility.
- **Behavioral Design Patterns**: Define how objects interact with one another and ensure that these interactions are clear, flexible, and loosely coupled.

By understanding and applying these patterns, software developers can solve common design challenges in a more systematic and efficient way. Each category of pattern serves a unique purpose, addressing different aspects of software design to create robust, scalable systems.