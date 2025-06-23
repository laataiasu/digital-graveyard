---
date: 2001-01-01
---

# Python Design Patterns Working with Creational Design Patterns

## 2
### Singleton Design Pattern

The **singleton pattern** ensures that a class has only one instance and provides a global point of access to that instance. It is widely used in practice for scenarios where you need exactly one object of a class, such as managing a connection to a database or a logging system.

#### Key Characteristics of the Singleton Pattern:

1. **Single Instance**: Only one instance of the class is created.
2. **Global Access**: The instance is accessible globally, meaning any part of the program that needs it will get the same instance.

#### Why Use the Singleton Pattern?

- **Resource Efficiency**: If object creation is resource-intensive, you can avoid creating multiple instances. For example, if creating a database connection is costly, a singleton ensures only one connection object is created.
- **Lazy Instantiation**: The object is created only when needed, rather than upfront, which can save resources.
- **Global Access**: A singleton provides a central point of access, which is useful for scenarios like logging or database connections where one shared instance is preferred.

#### When to Use the Singleton Pattern:

1. **Global Object**: When you need an object that should be available globally (e.g., a database connection or logger).
2. **Expensive Operations**: If creating an instance is expensive, and you want to avoid redundant instances.
3. **Lazy Instantiation**: When you want to instantiate an object only when it is required.
4. **Global Access**: When you need a single global point of access to the object, regardless of where in the program it is accessed.

#### Implementing Singleton in Python:

1. **Ensure One Instance**: The singleton class should guarantee that only one instance of the class is created.
2. **Global Access**: Provide access to the same instance across the program.

Example Flow:
- The first client accesses the singleton instance.
- Any subsequent client accessing the singleton will receive the same instance, not a new one.

#### Considerations:
- **Thread Safety**: In multi-threaded environments, you may need to ensure synchronization to prevent multiple instances from being created simultaneously. However, synchronization is not covered in this explanation.

#### Conclusion:
The singleton pattern is useful when you need exactly one instance of a class with global access, and when creating the object is a resource-intensive operation. It is especially common in managing shared resources like logging or database connections.

## 3
### Implementing a Singleton Class in Python

#### Step 1: Create the Singleton Class

In Python, you can create a singleton class by ensuring that only one instance of the class exists and that all clients use the same instance. A typical use case for a singleton is when instantiating a class is resource-intensive, and you want to control access to a scarce resource, like a logger or database connection.

Here's how we can create a simple `Logger` class as a singleton:

```python
class Logger:
    __instance = None  # Class-level variable to hold the singleton instance
    
    def __init__(self):
        # Prevent direct instantiation of the class
        raise RuntimeError('Call get_instance() instead')
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            print("No instance exists, creating a new one")
            cls.__instance = cls.__new__(cls)  # Create the object without invoking __init__
        else:
            print("A previously created instance exists, returning that same one")
        return cls.__instance
```

- `__instance`: A class-level variable that will hold the singleton instance.
- `__init__(self)`: Raises a `RuntimeError` to prevent direct instantiation using `Logger()`.
- `get_instance(cls)`: A class method that ensures only one instance is created. If the instance doesn't exist, it is created using `cls.__new__(cls)` and returned. If it already exists, the existing instance is returned.

#### Step 2: Using the Singleton Class

To use the singleton, you must always call `get_instance()` instead of directly instantiating the class.

```python
# Try to instantiate the Logger class directly (this will raise an error)
try:
    logger = Logger()
except RuntimeError as e:
    print(e)  # Outputs: Call get_instance() instead

# Correct way to instantiate and access the singleton
logger_1 = Logger.get_instance()  # First time creating the instance
logger_2 = Logger.get_instance()  # Returns the existing instance
logger_3 = Logger.get_instance()  # Again, returns the same instance
```

- The first call to `Logger.get_instance()` creates the instance.
- Subsequent calls return the same instance, ensuring a single object is used throughout the application.

#### Explanation of Key Components:

1. **`__new__(cls)`**: This method is used to create an instance of the class without calling `__init__`. By using `__new__`, we bypass the `__init__` method, which prevents the `RuntimeError` from being raised during object creation.
   
2. **`get_instance()`**: This method checks if an instance already exists (`cls.__instance`). If not, it creates a new instance; otherwise, it returns the existing instance.

#### Example Output:

```python
# Output when first calling get_instance()
No instance exists, creating a new one
<__main__.Logger object at 0x7fcd6eac5a58>

# Output when calling get_instance() again
A previously created instance exists, returning that same one
<__main__.Logger object at 0x7fcd6eac5a58>
```

Notice that the memory address (`0x7fcd6eac5a58`) remains the same for all calls to `get_instance()`, indicating that the same instance is being returned.

#### Step 3: Cleaner Implementation Using `__new__`

While the previous implementation works, it requires clients to always call `get_instance()`, which isn't as intuitive as direct instantiation. To make it more Pythonic, we can override the `__new__` method to automatically handle the singleton pattern:

```python
class Logger:
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            print("Creating a new instance")
            cls.__instance = super().__new__(cls)
        return cls.__instance
```

Now, clients can instantiate the `Logger` class directly, and the `__new__` method will ensure that only one instance is created.

```python
# Instantiate Logger normally
logger_1 = Logger()  # First time creating the instance
logger_2 = Logger()  # Returns the same instance
logger_3 = Logger()  # Again, returns the same instance
```

### Conclusion

By using the `__new__` method or the `get_instance()` approach, you can create a singleton class in Python. The key idea is to ensure that only one instance of the class is created, and all clients share the same instance.

## 4
### Elegant Implementation of Singleton Pattern in Python

The video provides an elegant solution to the singleton pattern in Python, where a `Logger` class ensures that only one instance of the class is created. Let's walk through the key points of the implementation and the logic behind it.

#### Step 1: Class Definition and `__new__` Method

In this implementation, the `Logger` class uses the `__new__` method to manage the creation of the singleton instance. The `__new__` method is responsible for creating the instance of the class, while the `__init__` method is responsible for initializing the object's attributes. Here’s the improved version of the `Logger` class:

```python
class Logger:
    __instance = None  # Class-level variable to store the singleton instance
    
    def __init__(self):
        # Instead of raising an error, we print a message indicating initialization
        print("Object initialized")

    def __new__(cls):
        # Check if the instance already exists
        if cls.__instance is None:
            print("No instance exists, creating a new one")
            # Create a new instance if it doesn't exist
            cls.__instance = super(Logger, cls).__new__(cls)
        else:
            print("A previously created instance exists, returning that same one")
        return cls.__instance
```

#### Key Changes:

1. **`__instance`**: This is a class variable used to hold the single instance of the `Logger` class. It's initialized to `None`, which means no instance has been created yet.

2. **`__init__`**: Instead of raising a `RuntimeError` as in the previous example, this `__init__` method simply prints a message indicating that an object has been initialized. This method is invoked whenever a new instance is created and initialized.

3. **`__new__(cls)`**: The `__new__` method is a class method that is responsible for creating the singleton instance. It first checks if the `__instance` variable is `None` (i.e., if no instance exists). If so, it creates a new instance using `super(Logger, cls).__new__(cls)`—which calls the `__new__` method of the base class (`object`) to create the object. If an instance already exists, it simply returns the existing instance.

#### Step 2: Using the Singleton Class

Now, when you instantiate the `Logger` class, it ensures that only one instance is created, even if you instantiate it multiple times.

```python
# Create the first instance of Logger
logger_1 = Logger()
# Output: No instance exists, creating a new one
# Output: Object initialized

# Create the second instance of Logger
logger_2 = Logger()
# Output: A previously created instance exists, returning that same one
```

Here’s the breakdown:
- **`logger_1 = Logger()`**: The first time you instantiate the `Logger`, a new instance is created, and the initialization code in `__init__` is executed.
- **`logger_2 = Logger()`**: The second time, the same instance is returned, and the initialization code in `__init__` is not run again.

You can check whether both `logger_1` and `logger_2` point to the same object using the `is` operator:

```python
print("Are they the same object?", logger_1 is logger_2)
```

Output:
```
Are they the same object? True
```

This confirms that `logger_1` and `logger_2` are the same instance of the `Logger` class.

#### Step 3: Ensuring Initialization Only Happens Once

The issue with the previous implementation is that the `__init__` method was called every time a new reference to the singleton object was created. If the initialization process is heavy or resource-intensive, you might want to ensure that it only happens once—regardless of how many times the singleton is accessed.

Here’s the revised approach to ensure that the initialization happens only once:

```python
class Logger:
    __instance = None
    
    def __init__(self):
        # No initialization here, the initialization happens only once
        pass

    def __new__(cls):
        if cls.__instance is None:
            print("No instance exists, creating a new one")
            cls.__instance = super(Logger, cls).__new__(cls)
            # Place all initialization code here (run only once)
            print("Object initialized")
        else:
            print("A previously created instance exists, returning that same one")
        return cls.__instance
```

#### Changes:
- **Removed Initialization in `__init__`**: Initialization code is no longer in `__init__`, because it's being handled explicitly within the `__new__` method the first time the object is created.
- **Manual Initialization**: Initialization (e.g., setting up variables or logging) happens only once, directly after the singleton instance is created in the `__new__` method.

Now, when you instantiate the `Logger` class multiple times, the object is initialized only once:

```python
logger_1 = Logger()  # First time creating the instance
logger_2 = Logger()  # Same instance returned, no re-initialization

print(logger_1 is logger_2)  # True
```

#### Final Conclusion:

This implementation is elegant and efficient because:
1. **Natural Instantiation**: You can instantiate `Logger` like any other Python class.
2. **Singleton Behavior**: The `__new__` method ensures that only one instance is ever created.
3. **Efficient Initialization**: The initialization occurs only once, ensuring that the expensive operations or resource allocations happen only when the singleton instance is first created.

This solution keeps the code simple and Pythonic while adhering to the singleton design pattern's principles.

## 5
### The Global Object Pattern in Python

The **Global Object Pattern** is closely related to the Singleton Pattern and is commonly used in Python. This pattern allows you to instantiate and manage global objects within a module, making those objects accessible across different parts of your application. The primary difference is that, rather than restricting instantiation via a `Singleton` class (which often forces a single instance throughout the program), it simply creates global objects at the module level, ensuring that those objects are used in a consistent and centralized way.

#### Key Concepts

1. **Global Objects**: A global object is an instance of a class that is created once and exposed as a global variable within a module. Other parts of your application can access this object by importing the module, ensuring that there is a single, shared reference to the object.

2. **Similar to Singleton**: The Global Object Pattern often behaves similarly to a Singleton. Once the global object is instantiated in the module, it is reused whenever it is accessed. However, it is not enforced through a Singleton class but rather by directly exposing the global object within the module.

3. **Module-Level Instantiation**: In Python, when you create a module (a `.py` file), any objects or variables at the module level are executed once when the module is imported, making them available throughout the application.

#### Example Implementation

Let's walk through the implementation of the **Global Object Pattern** using a simple logging system:

##### Step 1: Defining the Logger Class

We begin by defining a `Logger` class and two concrete logger classes: `ConsoleLogger` and `FileLogger`.

```python
# logger.py

DEBUG = 'debug'
INFO = 'info'
WARNING = 'warning'
ERROR = 'error'

class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger initialized: {name}")

    def log(self, message):
        print("Imagine that this logs the message to some output")

class __ConsoleLogger(Logger):
    def __init__(self, name):
        super().__init__(name)

    def log(self, message):
        print(f"Logging on the console: {message}")

class __FileLogger(Logger):
    def __init__(self, name):
        super().__init__(name)

    def log(self, message):
        print(f"Logging to a file: {message}")

# Exposing global objects
CONSOLE_LOGGER = __ConsoleLogger("console")
FILE_LOGGER = __FileLogger("file")
```

#### Explanation:
1. **Logger Class**: This is the base logger class that defines the common interface for logging. The `log()` method is a placeholder for logging logic.
2. **ConsoleLogger & FileLogger**: These are concrete implementations that log messages to the console and to a file, respectively.
3. **Global Instances**: Both the `ConsoleLogger` and `FileLogger` are instantiated once at the module level and exposed as global objects `CONSOLE_LOGGER` and `FILE_LOGGER`.

##### Step 2: Using the Logger Module

Next, you import the `logger` module and use the global logger objects.

```python
# GlobalObjectPattern.ipynb

import logger

# Accessing global objects
console_logger = logger.CONSOLE_LOGGER
file_logger = logger.FILE_LOGGER

# Using the loggers
console_logger.log("Logging to console!")
file_logger.log("Logging to file!")
```

#### Explanation:
1. **Importing the Module**: By importing the `logger` module, Python executes the code inside it. The `CONSOLE_LOGGER` and `FILE_LOGGER` objects are instantiated once and available globally within the module.
2. **Accessing Global Loggers**: Once imported, you can access `logger.CONSOLE_LOGGER` and `logger.FILE_LOGGER`, which will always refer to the same instances of the `ConsoleLogger` and `FileLogger`.
3. **Logging**: Calling `log()` on either of these global objects performs the logging operation, either to the console or a file.

##### Output:
When you run the above code, you’ll see:

```
Logger initialized: console
Logger initialized: file
Logging on the console: Logging to console!
Logging to a file: Logging to file!
```

#### Advantages of the Global Object Pattern:
- **Simplicity**: The pattern allows you to easily share state or behavior across different parts of your program without the complexity of class-based Singletons.
- **Access from Anywhere**: Since the global object is exposed at the module level, it can be accessed from any other module that imports the `logger` module, ensuring consistency.
- **Flexibility**: You can easily swap out implementations by modifying the global objects, without having to change the rest of the code.

#### Comparison with Singleton Pattern:

- Both the **Global Object Pattern** and the **Singleton Pattern** ensure there is only one instance of a class. However, the Singleton enforces this through a dedicated class, typically with a `get_instance` method or `__new__` method.
- The **Global Object Pattern**, in contrast, relies on directly exposing a single instance of the object at the module level, making it more implicit. There’s no need for special mechanisms to ensure only one instance exists because the module itself guarantees the instantiation happens once.

#### Use Cases:
- The **Global Object Pattern** is commonly used for managing resources that need to be shared globally, such as configuration settings, logging services, or database connections. It’s especially useful in Python where importing modules automatically runs the code, thus setting up the global objects.

### Conclusion:

The **Global Object Pattern** in Python is a simple yet powerful way to manage shared objects, like loggers, throughout an application. By creating and exposing these objects at the module level, you can ensure that they are accessed in a consistent and centralized way, much like a Singleton. It is particularly common in Python due to the language’s modularity and the ease with which objects can be shared across different parts of a program.

## 6
In this video, two **creational design patterns**—**Factory** and **Abstract Factory**—are discussed. These patterns share a common goal: **separating the creation of objects from their usage**. The goal is to make it easy to create objects based on certain parameters, while abstracting away the details of how those objects are created. Although similar in purpose, these two patterns have subtle differences.

### Factory Method Pattern

The **Factory Method** pattern allows a client to create an object without specifying the exact class of the object. Instead, the client calls a **factory method**, which handles the decision of which class to instantiate based on provided parameters.

**Key Concepts**:
- **Class Creation vs. Object Creation**: Factory methods deal with **class creation**, deciding which class to instantiate based on the client’s input parameters. 
- **Base Class and Derived Classes**: A factory method is often defined in a base class but implemented in derived classes, where the derived class knows how to instantiate the appropriate object.
- **Abstraction**: The client only interacts with the factory interface, passing the necessary parameters, but doesn't know or need to know which exact class will be created.

#### Example of the Factory Method Pattern:

Consider a scenario where different applications need to create different types of products (e.g., `ProductOne`, `ProductTwo`). The Factory Method allows you to create an object by passing parameters to the `makeProduct` function, which internally decides which type of product (derived class) to instantiate.

```python
class Product:
    def __init__(self, name):
        self.name = name

class ProductOne(Product):
    def __init__(self, name):
        super().__init__(name)

class ProductTwo(Product):
    def __init__(self, name):
        super().__init__(name)

class ProductFactory:
    @staticmethod
    def makeProduct(type_of_product):
        if type_of_product == 'one':
            return ProductOne('ProductOne')
        elif type_of_product == 'two':
            return ProductTwo('ProductTwo')

# Usage
product = ProductFactory.makeProduct('one')
```

Here, the client (using `ProductFactory.makeProduct()`) does not know whether it’s getting a `ProductOne` or `ProductTwo` object. The factory method decides based on the parameters provided.

### Abstract Factory Pattern

The **Abstract Factory** pattern is an extension of the Factory Method. It deals with creating objects from families of related classes. While the Factory Method focuses on creating individual objects, the Abstract Factory creates a set or family of related objects that work together. 

**Key Concepts**:
- **Families of Classes**: An abstract factory creates a set of related objects that belong to a family. For instance, you may have one family for Oracle database connections and another for MS-SQL database connections.
- **Platform Independence**: The Abstract Factory pattern is useful when you're working with multiple platforms or technologies, like different types of databases, and you need to abstract away the specific flavors of each.

#### Example of the Abstract Factory Pattern:

Imagine you are building an application that supports two types of databases—Oracle and MS-SQL. Each type of database has different "flavors" (specific database implementations), but the application should be able to work with either family without needing to worry about which specific database type it’s dealing with.

```python
class DatabaseConnection:
    def connect(self):
        raise NotImplementedError("Subclass must implement connect method.")

class OracleConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to Oracle Database"

class MS_SQLConnection(DatabaseConnection):
    def connect(self):
        return "Connecting to MS SQL Database"

class AbstractDatabaseFactory:
    def create_connection(self):
        raise NotImplementedError("Subclass must implement create_connection method.")

class OracleDatabaseFactory(AbstractDatabaseFactory):
    def create_connection(self):
        return OracleConnection()

class MS_SQLDatabaseFactory(AbstractDatabaseFactory):
    def create_connection(self):
        return MS_SQLConnection()

# Usage
def get_database_factory(platform):
    if platform == "oracle":
        return OracleDatabaseFactory()
    elif platform == "ms_sql":
        return MS_SQLDatabaseFactory()

# Client code
platform = "oracle"
database_factory = get_database_factory(platform)
connection = database_factory.create_connection()
print(connection.connect())  # "Connecting to Oracle Database"
```

Here, the **AbstractDatabaseFactory** allows the client to work with a platform-independent abstraction, such as the `AbstractDatabaseFactory` interface, while the concrete factory classes (`OracleDatabaseFactory`, `MS_SQLDatabaseFactory`) handle the creation of the appropriate database connections. The client does not need to know about the specific database connection, only that it can work with a `create_connection` method.

### Differences Between Factory Method and Abstract Factory:

1. **Focus**:
   - **Factory Method**: Focuses on creating individual objects of a particular class.
   - **Abstract Factory**: Focuses on creating families of related objects, ensuring they are designed to work together.

2. **Usage**:
   - **Factory Method**: Typically used when you need to instantiate a class from a family of classes, but the family is not necessarily interconnected.
   - **Abstract Factory**: Used when the client needs to instantiate several objects that work together as a group or family, such as in cross-platform applications.

### When to Use Each:

- **Factory Method**: Use this pattern when you have a class hierarchy and want to abstract the instantiation of objects, allowing subclasses to decide which concrete class to instantiate based on parameters.
  
- **Abstract Factory**: Use this when your system works with multiple families of related objects and you need a way to abstract the creation of these families. For example, when working with different platforms (like databases or GUIs), where each platform has a family of related objects.

### Summary:

Both **Factory Method** and **Abstract Factory** are **creational design patterns** that abstract away the instantiation process, allowing clients to create objects without knowing the specific details of how they are constructed. The Factory Method focuses on creating a single product or object, whereas the Abstract Factory focuses on creating families of related products or objects. These patterns help improve the modularity and flexibility of your code by decoupling object creation from the actual usage.

## 7
In this demo, the goal is to implement the **Factory Method** pattern in Python in its simplest form. The factory method will be responsible for creating instances of different product objects based on input parameters, and the client will not need to know the details of how those objects are created.

### Step-by-Step Breakdown of the Code:

1. **Product Base Class**:
   - A `Product` class is created with basic attributes: `name` and `price`.
   - The constructor accepts these values, and a getter method (`get_price`) is implemented to retrieve the price of the product.

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price
```

2. **Derived Product Classes**:
   - Three specific products (`MacBookAir`, `AppleIPad`, `AppleIWatch`) are defined, each inheriting from the `Product` class.
   - Each derived class has its own initialization, accepting product-specific parameters such as `memory`, `os`, or `generation`.

```python
class MacBookAir(Product):
    def __init__(self, memory, os):
        Product.__init__(self, 'MacBookAir', 1031)  # Name and price
        self.__memory = memory
        self.__os = os

class AppleIPad(Product):
    def __init__(self, generation):
        Product.__init__(self, 'AppleIPad', 529)  # Name and price
        self.__generation = generation

class AppleIWatch(Product):
    def __init__(self):
        Product.__init__(self, 'AppleIWatch', 264)  # Name and price
```

3. **Factory Class**:
   - The `ProductFactory` class is responsible for the creation of product objects.
   - The `create` static method uses a simple conditional check (`if`-`elif`) to determine which product to create based on the `item_name` parameter passed by the client.
   - The additional arguments (`*args`) allow flexibility in passing product-specific parameters.

```python
class ProductFactory:
    @staticmethod
    def create(item_name, *args):
        if item_name == 'MacBookAir':
            return MacBookAir(*args)
        elif item_name == 'AppleIPad':
            return AppleIPad(*args)
        elif item_name == 'AppleIWatch':
            return AppleIWatch()
```

4. **Client Code**:
   - The client interacts with the factory by calling `ProductFactory.create` and passing the product name along with any necessary parameters.
   - The factory then instantiates the appropriate product class and returns the product object.

```python
# Create a MacBookAir with specific arguments
air = ProductFactory.create('MacBookAir', '16GB', 'Sierra')
print(air.__dict__)  # Shows the details of the created MacBookAir

# Create an Apple iPad (2nd generation)
ipad = ProductFactory.create('AppleIPad', '2nd')
print(ipad.__dict__)  # Shows the details of the created iPad

# Create an Apple iWatch (no extra parameters needed)
iwatch = ProductFactory.create('AppleIWatch')
print(iwatch.__dict__)  # Shows the details of the created Apple iWatch
```

### Key Concepts Demonstrated:
- **Abstraction of Object Creation**: The client only interacts with the `create` method of the `ProductFactory` class and does not need to know the specifics of how each product is created. This encapsulation hides the complexity of object instantiation and allows for easy extension (e.g., adding more products).
  
- **Flexibility with Variable Arguments**: The `*args` parameter in the `create` method allows the factory to handle different numbers of input parameters for different products.

- **Product Variants**: Each product class (such as `MacBookAir`, `AppleIPad`, etc.) is responsible for holding additional properties specific to the product (like `memory`, `os`, or `generation`), which is passed in through the factory method.

### Example Outputs:
When the client creates objects using the factory method:

```python
# For MacBookAir
air = ProductFactory.create('MacBookAir', '16GB', 'Sierra')
print(air.__dict__)  # {'_Product__name': 'MacBookAir', '_Product__price': 1031, '_MacBookAir__memory': '16GB', '_MacBookAir__os': 'Sierra'}

# For AppleIPad
ipad = ProductFactory.create('AppleIPad', '2nd')
print(ipad.__dict__)  # {'_Product__name': 'AppleIPad', '_Product__price': 529, '_AppleIPad__generation': '2nd'}

# For AppleIWatch
iwatch = ProductFactory.create('AppleIWatch')
print(iwatch.__dict__)  # {'_Product__name': 'AppleIWatch', '_Product__price': 264}
```

### Summary:
The **Factory Method** pattern is demonstrated through a `ProductFactory` class that abstracts the creation of different types of products. The client code simply provides the product name and necessary parameters, and the factory method handles the rest, instantiating the correct product object. This approach allows for easy management and extension of products without exposing complex object creation logic to the client.

## 8
In this video, the focus is on how to use the **Factory Method** pattern to abstract the process of serializing a movie object into different formats, such as **JSON** and **XML**, with the goal of making the code more modular and extensible. Here's a breakdown of the steps and code involved:

### 1. **Movie Entity**:
The entity being serialized is a **Movie** class, which contains basic information about a movie: its ID, name, and director.

```python
class Movie:
    def __init__(self, movie_id, name, director):
        self.movie_id = movie_id
        self.name = name
        self.director = director
```

### 2. **Initial Implementation of MovieSerializer**:
The `MovieSerializer` class has a `serialize` method, which takes a **movie object** and a **format string** (`'JSON'` or `'XML'`). The method checks the format and serializes the movie data accordingly.

```python
class MovieSerializer:
    def serialize(self, movie, fmt):
        if fmt == 'JSON':
            movie_info = {
                'id': movie.movie_id,
                'name': movie.name,
                'director': movie.director
            }
            return json.dumps(movie_info)
        elif fmt == 'XML':
            movie_info = et.Element('movie', attrib={'id': movie.movie_id})
            name = et.SubElement(movie_info, 'name')
            name.text = movie.name
            director = et.SubElement(movie_info, 'director')
            director.text = movie.director
            return et.tostring(movie_info, encoding='unicode')
        else:
            raise ValueError(fmt)
```

### 3. **Serialization Process**:
- If the format is `'JSON'`, a Python dictionary is created and serialized using `json.dumps()`.
- If the format is `'XML'`, the `ElementTree` module is used to create an XML structure and serialize it to a string using `et.tostring()`.
- If the format is unsupported, a `ValueError` is raised.

### 4. **Example Use of the MovieSerializer**:
Once the `Movie` object is created, the `MovieSerializer` is used to serialize the movie into either JSON or XML:

```python
movie = Movie('578', 'Avengers: End Game', 'Russo brothers')
serializer = MovieSerializer()

# Serialize to JSON format
json_output = serializer.serialize(movie, 'JSON')
print(json_output)

# Serialize to XML format
xml_output = serializer.serialize(movie, 'XML')
print(xml_output)
```

The output for the two formats would look like this:

**JSON Output**:
```json
{
    "id": "578",
    "name": "Avengers: End Game",
    "director": "Russo brothers"
}
```

**XML Output**:
```xml
<movie id="578">
    <name>Avengers: End Game</name>
    <director>Russo brothers</director>
</movie>
```

### 5. **Drawbacks of the Initial Approach**:
While the initial approach works, it has some drawbacks:
- The `serialize` method contains both the logic for handling different formats, which makes it difficult to extend (e.g., adding a new format such as YAML).
- The method is long and difficult to maintain, as all serialization logic is lumped into one place.

### 6. **Refactoring the Code**:
To improve the code, the process is refactored to separate the serialization logic for each format into its own helper function. This not only improves readability but also makes the code easier to extend with new formats.

```python
class MovieSerializer:
    def serialize(self, movie, fmt):
        if fmt == 'JSON':
            return self._serialize_to_json(movie)
        elif fmt == 'XML':
            return self._serialize_to_xml(movie)
        else:
            raise ValueError(fmt)

    def _serialize_to_json(self, movie):
        movie_info = {
            'id': movie.movie_id,
            'name': movie.name,
            'director': movie.director
        }
        return json.dumps(movie_info)

    def _serialize_to_xml(self, movie):
        movie_info = et.Element('movie', attrib={'id': movie.movie_id})
        name = et.SubElement(movie_info, 'name')
        name.text = movie.name
        director = et.SubElement(movie_info, 'director')
        director.text = movie.director
        return et.tostring(movie_info, encoding='unicode')
```

### 7. **Improvement with Factory Method**:
With this refactor, the logic for serializing to different formats is now cleanly separated into dedicated methods. This makes the `MovieSerializer` class much easier to extend in the future. For example, if we wanted to add **YAML** serialization, we could simply add a new helper method, `_serialize_to_yaml`, and update the `serialize` method to check for the `'YAML'` format.

### 8. **Final Usage**:
Now, with the refactored class, the process of serialization remains the same, but the underlying implementation is more maintainable and extensible:

```python
serializer = MovieSerializer()
json_output = serializer.serialize(movie, 'JSON')
print(json_output)

xml_output = serializer.serialize(movie, 'XML')
print(xml_output)
```

This refactored code improves readability and maintainability while adhering to the **Open/Closed Principle** (open for extension, closed for modification). Adding new formats (like YAML) can be done by simply adding new methods and extending the `serialize` function minimally.

### Summary:
- Initially, all serialization logic was in a single method, which worked but was hard to extend.
- The solution was refactored to separate the format-specific logic into individual helper methods.
- This refactoring leads to cleaner, more maintainable code, and with the use of the **Factory Method** pattern, it ensures that adding new serialization formats (like YAML) is easy and requires minimal changes to the core code.

## 9
In this video, we are enhancing our `MovieSerializer` class by refactoring it to use the **Factory Method Pattern**. The idea behind this pattern is to decouple the logic of creating the appropriate serializer (for different formats) from the actual serialization process. Let’s break down the key improvements made:

### **Step 1: Import Required Modules**
We begin by importing the necessary modules for JSON and XML serialization:
```python
import json
import xml.etree.ElementTree as et
```

### **Step 2: Base Class `MovieSerializer`**
The `MovieSerializer` class will act as the **Factory** that delegates the serialization responsibility to subclasses. This class contains:
- A dictionary (`__fmt_dictionary`) to store the formats (JSON, XML, etc.) and their corresponding serializer functions.
- An initializer (`__init__`) to register serializer functions for supported formats.
- A class method (`serialize`) to handle the serialization logic. It looks up the format in the `__fmt_dictionary` and uses the appropriate function to serialize the movie.

Here is the class definition:
```python
class MovieSerializer:
    __fmt_dictionary = {}

    def __init__(self, fmt, serializer_fn):
        self.__fmt_dictionary[fmt] = serializer_fn

    @classmethod
    def serialize(cls, movie, fmt):
        if fmt not in cls.__fmt_dictionary:
            raise ValueError(fmt)
        serializer_fn = cls.__fmt_dictionary[fmt]
        return serializer_fn(movie)
```
- **`__init__`**: Registers the format and serializer function (e.g., JSON, XML) in the `__fmt_dictionary`.
- **`serialize`**: Looks up the format in the `__fmt_dictionary`, and if found, calls the corresponding serializer function.

### **Step 3: Subclasses for JSON and XML Serialization**

Next, we create two subclasses that handle serialization in specific formats. These classes inherit from `MovieSerializer` and register their respective serializer functions.

#### **JSON Serialization**
The `JSONMovieSerializer` class handles serialization to JSON. We define an internal method (`_serialize_to_json`) to convert the movie object into a JSON string:
```python
class JSONMovieSerializer(MovieSerializer):
    def __init__(self):
        MovieSerializer.__init__(self, 'JSON', self._serialize_to_json)

    def _serialize_to_json(self, movie):
        movie_info = {
            'id': movie.movie_id,
            'name': movie.name,
            'director': movie.director
        }
        return json.dumps(movie_info)
```
- **`__init__`**: Registers the 'JSON' format and its corresponding serializer function (`_serialize_to_json`).
- **`_serialize_to_json`**: Converts the `movie` object into a dictionary and serializes it to a JSON string using `json.dumps`.

#### **XML Serialization**
The `XMLMovieSerializer` class handles XML serialization. It converts the movie object into an XML structure:
```python
class XMLMovieSerializer(MovieSerializer):
    def __init__(self):
        MovieSerializer.__init__(self, 'XML', self._serialize_to_xml)

    def _serialize_to_xml(self, movie):
        movie_element = et.Element('movie', attrib={'id': movie.movie_id})
        name = et.SubElement(movie_element, 'name')
        name.text = movie.name
        director = et.SubElement(movie_element, 'director')
        director.text = movie.director
        return et.tostring(movie_element, encoding='unicode')
```
- **`__init__`**: Registers the 'XML' format and its corresponding serializer function (`_serialize_to_xml`).
- **`_serialize_to_xml`**: Creates an XML structure using the `xml.etree.ElementTree` module and serializes the movie object.

### **Step 4: Using the Serializer**
Now, we can use the `MovieSerializer` to serialize movie objects into different formats without worrying about the underlying implementation.

1. **Import the module**: After saving the `movieserializer.py` file, we import it into our main script:
```python
import movieserializer
```

2. **Create a movie object**:
```python
movie = Movie('578', 'Avengers: End Game', 'Russo brothers')
```

3. **Serialize the movie**:
```python
movieserializer.MovieSerializer.serialize(movie, 'JSON')
movieserializer.MovieSerializer.serialize(movie, 'XML')
```
The `MovieSerializer.serialize()` method automatically selects the correct serializer (either `JSONMovieSerializer` or `XMLMovieSerializer`) based on the format specified.

### **Step 5: Adding New Formats (YAML, etc.)**
To extend the `MovieSerializer` for additional formats (e.g., YAML), we can:
- Create a new subclass of `MovieSerializer` (e.g., `YAMLMovieSerializer`).
- Register the new serializer function in the `__fmt_dictionary` via the `MovieSerializer.__init__()` method.
This change only requires adding a new subclass and does not modify the existing base class or other subclasses, adhering to the **Open/Closed Principle** (open for extension, closed for modification).

### **Conclusion**
By implementing the **Factory Method Pattern** in the `MovieSerializer` class, we have created a flexible and extensible system for serializing movie objects to multiple formats (JSON, XML, YAML, etc.). The main benefit is that the `MovieSerializer` class is now closed for modification (we don’t need to change it to support new formats), but open for extension (we can easily add new serializers).

## 10
In this video, we explore how to implement the Abstract Factory design pattern in Python. Here's a breakdown of the steps taken and the concepts covered:

### **1. Introduction to the Abstract Factory Pattern**
The Abstract Factory Pattern allows us to create families of related objects without specifying their concrete classes. This pattern involves defining an interface for creating objects, and then implementing the interface in concrete factories. The pattern ensures that objects from the same family are created together, which is useful in scenarios where related objects must be created together to maintain consistency.

### **2. Setting Up the Abstract Base Classes**
- **Toy Class**: This class represents a toy in the family, and it's an abstract base class (ABC) with an abstract method `show`.
  ```python
  class Toy(metaclass=abc.ABCMeta):
      @abc.abstractmethod
      def show(self): pass
  ```

- **Color Class**: This is another abstract base class representing color. It also has an abstract method `show_color`.
  ```python
  class Color(metaclass=abc.ABCMeta):
      @abc.abstractmethod
      def show_color(self): pass
  ```

### **3. Concrete Classes for Toy and Color**
- **Toy Subclasses**: Specific toys like `Car`, `ActionFigure`, and `ConstructionToy` derive from the `Toy` base class, providing implementations for the `show` method.
  ```python
  class Car(Toy):
      def show(self):
          print("Remote controlled car")

  class ActionFigure(Toy):
      def show(self):
          print("Captain America action figure")

  class ConstructionToy(Toy):
      def show(self):
          print("Lego")
  ```

- **Color Subclasses**: Specific colors like `Red`, `Green`, and `Blue` derive from the `Color` base class, implementing the `show_color` method.
  ```python
  class Red(Color):
      def show_color(self):
          print("red")

  class Green(Color):
      def show_color(self):
          print("green")

  class Blue(Color):
      def show_color(self):
          print("blue")
  ```

### **4. Using Abstract Factory**
- **AbstractFactory Class**: This is an abstract base class that defines two abstract factory methods, `get_toy` and `get_color`, which will be responsible for returning toy and color objects respectively.
  ```python
  class AbstractFactory(metaclass=abc.ABCMeta):
      @abc.abstractmethod
      def get_toy(self): pass

      @abc.abstractmethod
      def get_color(self): pass
  ```

### **5. Concrete Factory Implementation**
- **ColorfulToysFactory**: This factory class inherits from `AbstractFactory`. It implements the `get_toy` and `get_color` methods, returning specific toy and color objects based on the input provided.
  ```python
  class ColorfulToysFactory(AbstractFactory):
      def get_toy(self, toy_type):
          if toy_type == "car":
              return Car()
          elif toy_type == "action figure":
              return ActionFigure()
          elif toy_type == "construction toy":
              return ConstructionToy()

      def get_color(self, color_type):
          if color_type == "red":
              return Red()
          elif color_type == "green":
              return Green()
          elif color_type == "blue":
              return Blue()
  ```

### **6. Using the Factory to Get Combinations of Toy and Color**
- **ColorfulToysProducer**: This class uses the `ColorfulToysFactory` to create combinations of toys and colors. It includes a class method `get_toy_and_color`, which returns both a toy and a color based on the specified choice.
  ```python
  class ColorfulToysProducer:
      __colorful_toys_factory = ColorfulToysFactory()

      @classmethod
      def get_toy_and_color(cls, choice):
          toy = None
          color = None
          if choice == 'red_car':
              toy = cls.__colorful_toys_factory.get_toy('car')
              color = cls.__colorful_toys_factory.get_color('red')
          elif choice == 'blue_lego':
              toy = cls.__colorful_toys_factory.get_toy('construction toy')
              color = cls.__colorful_toys_factory.get_color('blue')
          elif choice == 'green_action_figure':
              toy = cls.__colorful_toys_factory.get_toy('action figure')
              color = cls.__colorful_toys_factory.get_color('green')
          return toy, color
  ```

### **7. Example Usage**
- The `ColorfulToysProducer` can be used to create specific combinations of toys and colors:
  ```python
  toy, color = ColorfulToysProducer.get_toy_and_color('red_car')
  toy.show()  # Output: Remote controlled car
  color.show_color()  # Output: red
  ```

- Other combinations can be retrieved in a similar manner:
  ```python
  toy, color = ColorfulToysProducer.get_toy_and_color('blue_lego')
  toy.show()  # Output: Lego
  color.show_color()  # Output: blue
  ```

### **Conclusion**
The Abstract Factory Pattern in Python can be implemented, although it is not as elegant as other patterns due to the constraints of the language. The pattern is still useful when you need to work with families of related objects and ensure they are created together consistently. In this case, the pattern helps us create various toy and color combinations without directly instantiating objects from their respective classes. 

The abstract factory design pattern is not commonly used in Python due to its verbosity, but knowing how to implement it can be helpful in certain scenarios where you need strict object families.

## 11
In this video, we delve into the **Builder Design Pattern**, which is used to separate the construction process of an object from its representation. The Builder pattern is particularly useful when constructing complex objects, allowing for a step-by-step process and different variations of the same object.

### **Key Concepts of the Builder Design Pattern:**

1. **Separation of Concerns**:
   - The builder pattern allows you to manage the construction of an object separately from its representation.
   - This means you can focus on how the object is constructed (step-by-step) without worrying about its final form during the process.

2. **Managing Complexity**:
   - In simple cases, objects can be created directly using their class constructors, but as the complexity of the object increases, the constructor may become cumbersome.
   - The builder pattern abstracts away the complexity of constructing an object, especially when the object has many components, some of which are optional or may vary.

3. **Flexible Object Construction**:
   - Builder pattern helps to build different representations of the same class. This is beneficial when constructing complex objects that can have many variations depending on the situation.

4. **Example Use Case: SQL Query Builder**:
   - A common example of the builder pattern in action is in **SQL query construction**. A SQL query typically has many components, such as:
     - **Fields** to select
     - **Filter conditions**
     - **Grouping and aggregation**
   - Some components are optional, and the builder pattern allows you to build the query step-by-step, specifying only the necessary components.
   - The result is that a complex SQL query can be constructed once and used multiple times within the program.

5. **Construction and Representation**:
   - The builder pattern focuses on constructing an object in phases. Each phase is responsible for adding specific details to the object.
   - The final representation is the fully constructed object (e.g., a SQL query, or a meal order).

### **Real-World Example: Building a Kid's Meal in a Restaurant:**

Imagine a customer ordering a **Kid's Meal** at a fast-food restaurant. The process can be viewed through the lens of the builder pattern:

1. **Step 1: Preparing the Food**:
   - This is the first step in the meal construction. The builder (restaurant crew) decides what kind of food (burger, chicken, etc.) to prepare based on the customer's order.
   
2. **Step 2: Adding the Drinks**:
   - The second step involves adding a drink to the meal. The drink (e.g., soda, juice) is a part of the meal but is prepared separately from the food.
   
3. **Step 3: Packaging the Meal**:
   - Once the food and drinks are ready, they are packaged together. The packaging step ensures that all parts of the meal are grouped together for delivery.
   
4. **Step 4: Delivering the Meal**:
   - The final step is delivering the completed meal to the customer, completing the construction process.

### **Summary**:
The **Builder Design Pattern** is useful when:
- You have complex objects with multiple parts or variations.
- You need to construct these objects step-by-step, managing each part independently.
- You want to allow different configurations or representations of the same object.

In this video, the builder pattern is used to simplify complex object construction by breaking down the process into smaller, manageable steps. Whether it's creating a meal, building a SQL query, or constructing any object with multiple components, the builder pattern helps ensure the process is both manageable and flexible.

## 12
In this video, we explore the **Builder Design Pattern** with a practical example of creating a `Mobile` class. The builder pattern helps manage complex object construction by separating the construction process from the representation of the object. The goal is to simplify the instantiation of objects with many attributes or optional properties.

### **Step-by-Step Explanation:**

#### **Mobile Class (Without Builder Pattern)**

1. **Defining the Mobile Class**:
   - The `Mobile` class has several properties such as `name`, `weight`, `screen_size`, `ram`, `os`, `camera_mp`, and `battery`. These properties are required when creating an instance of `Mobile` via the constructor.
   - The `__init__` method takes all these properties as input arguments to initialize the object. This can become cumbersome because every time you create a `Mobile`, you need to specify values for all these attributes.

   ```python
   class Mobile:
       def __init__(self, name, weight, screen_size, ram, os, camera_mp, battery):
           self.name = name
           self.weight = weight
           self.screen_size = screen_size
           self.ram = ram
           self.os = os
           self.camera_mp = camera_mp
           self.battery = battery
   ```

2. **Creating a Mobile Object**:
   - To create an object like `samsung_s10`, you need to manually specify values for each property. This can be error-prone and difficult to manage when creating multiple `Mobile` objects with varying properties.

   ```python
   samsung_s10 = Mobile(name="Samsung S10", weight="157g", screen_size="6.1 inch", 
                        ram="8GB", os="Android 9.0", camera_mp="12 megapixel", battery="3400 mAh")
   samsung_s10.show()
   ```

#### **Simplifying with Default Values (Not Builder Pattern)**

1. **Using Optional Properties**:
   - To simplify the object creation, you can set default values for some properties in the `__init__` method. This reduces the number of parameters you need to specify when creating an object.

   ```python
   class Mobile:
       def __init__(self, name, weight='157g', screen_size='5 inches', ram='8GB',
                    os='Android', camera_mp='16 megapixels', battery='3400 mAh'):
           self.name = name
           self.weight = weight
           self.screen_size = screen_size
           self.ram = ram
           self.os = os
           self.camera_mp = camera_mp
           self.battery = battery
   ```

2. **Creating an Object with Default Values**:
   - With default values in place, you only need to specify the `name` of the mobile when creating an object. If you want to change any other property, you can override the default value.

   ```python
   samsung_s10 = Mobile('Samsung S10')
   samsung_s10.show()  # Uses default values for all properties except the name.
   ```

3. **Overriding Defaults**:
   - If you want to change a few attributes, such as the screen size or RAM, you can easily pass those when creating the object.

   ```python
   samsung_s8 = Mobile('Samsung S8', screen_size='4.4 inches', ram='4GB')
   samsung_s8.show()  # Only overrides screen_size and ram, other properties use defaults.
   ```

While this approach reduces complexity, it doesn't fully capture the flexibility of the **builder pattern**, especially in scenarios where you might want to create multiple objects with different combinations of properties.

#### **Builder Pattern Implementation:**

1. **The Builder Class**:
   - The builder class (`MyMobileBuilder`) is introduced to handle the construction of the `Mobile` object. It provides helper methods for each property of the `Mobile` class, allowing for step-by-step construction of the object.

   ```python
   class MyMobileBuilder:
       def __init__(self):
           self.__mobile = Mobile()

       def build_name(self, name):
           self.__mobile.name = name
       def build_memory(self, ram):
           self.__mobile.ram = ram
       def build_camera(self, camera_mp):
           self.__mobile.camera_mp = camera_mp
       def build_otherfeatures(self, weight, screen_size, os, battery):
           self.__mobile.weight = weight
           self.__mobile.screen_size = screen_size
           self.__mobile.os = os
           self.__mobile.battery = battery

       def get_mobile(self):
           return self.__mobile
   ```

2. **Using the Builder**:
   - The builder is used to specify the mobile's properties one step at a time, making it easier to manage and less error-prone.

   ```python
   builder = MyMobileBuilder()
   builder.build_name('Samsung S10')
   builder.build_memory('8GB')
   builder.build_camera('16 megapixels')
   mobile = builder.get_mobile()
   mobile.show()
   ```

#### **When the Builder Pattern is Less Useful in Python**

1. **Default Arguments in Python**:
   - Python's ability to handle default arguments reduces the need for the builder pattern. If the attributes of an object can have meaningful default values, you can use those instead of building the object step-by-step.

   ```python
   class Mobile:
       def __init__(self, name, weight='157g', screen_size='5 inches', ram='8GB',
                    os='Android', camera_mp='16 megapixels', battery='3400 mAh'):
           self.name = name
           self.weight = weight
           self.screen_size = screen_size
           self.ram = ram
           self.os = os
           self.camera_mp = camera_mp
           self.battery = battery
   ```

2. **Simplified Object Creation**:
   - You can still create an object easily with defaults, and override only the values you want to change. This can be sufficient for many cases without needing a full builder pattern.

   ```python
   samsung_s10 = Mobile('Samsung S10')
   samsung_s10.show()
   ```

### **Conclusion**:
- The **Builder Pattern** is extremely useful for constructing complex objects step-by-step, especially when the object has many optional attributes or combinations of properties.
- In **Python**, the pattern can be less necessary if default arguments are used effectively, but it still provides a clear, structured way to handle complex object construction.

## 13
In this video, we’re introduced to the **Object Pool design pattern**, which is similar to the **Singleton pattern** but differs in its approach to managing object instances. The Object Pool pattern limits the number of instances of a class to ensure that only a few objects are created and reused efficiently, avoiding unnecessary overhead from repeatedly creating and destroying objects. This pattern is especially useful when the cost of object creation is high, such as when objects require significant resources like memory or external connections (e.g., database connections).

### Key Points:
1. **Cost of Initialization**: Object pools are useful when creating objects is expensive, either in terms of time or resources. By reusing existing objects from the pool, we can save on the overhead of instantiating new ones.
   
2. **Low Object Usage**: If the objects in use at any given time are relatively few, object pools allow us to limit the number of instantiated objects and prevent creating excess objects that might go unused.

3. **High Rate of Object Requests**: When many clients frequently request and release objects, an object pool can efficiently manage the creation and recycling of objects to meet demand without repeatedly creating new instances.

4. **Thread Pools**: A common example of the Object Pool pattern is the **thread pool**. Since creating new threads is resource-intensive, thread pools maintain a cache of reusable threads that clients can request for tasks. The thread pool reduces the overhead of creating and destroying threads and ensures that threads are reused efficiently.

5. **Management of Reused Objects**: The Object Pool handles the management of objects (whether threads, database connections, or other resources) by maintaining a pool of objects that are reused rather than constantly recreated. Clients request objects from the pool and release them once they're done, allowing other clients to use them.

6. **Example with Office Equipment**: The video gives a simple analogy of an office equipment pool to explain the concept: If a newly hired employee needs equipment (e.g., a laptop), you check the inventory (the object pool). If equipment is available, you provide it; if not, you order new equipment (create new objects). When the employee leaves, the equipment is returned to the warehouse, ready to be reused by another employee (recycled object). This is similar to how an object pool manages resources—reusing and recycling objects as necessary.

### Benefits of Object Pools:
- **Performance**: By reusing objects, we reduce the need for expensive object creation and destruction.
- **Resource Management**: Limits the number of objects created, which is useful for managing scarce resources like threads or database connections.
- **Concurrency**: Helps manage access to shared resources by controlling the number of instances that can be used at any given time.

In summary, the Object Pool pattern is essential when dealing with high-cost object creation, low object usage, and frequent object requests, especially in scenarios like thread management or resource-intensive applications. It effectively reduces overhead, improves performance, and ensures efficient resource management.

## 14
### Object Pooling in Python

#### Connection Class
The `Connection` class simulates a connection to a database. 

```python
class Connection:
    def __init__(self):
        self.__is_used = False
    
    def acquire(self):
        self.__is_used = True
    
    def release(self):
        self.__is_used = False
    
    def is_used(self):
        return self.__is_used
    
    def connect_to_database(self):
        pass
```

- The `__is_used` attribute tracks whether the connection is currently in use.
- The `acquire` method sets `__is_used` to `True` when the connection is assigned to a client.
- The `release` method sets `__is_used` to `False` when the connection is released.
- The `is_used` method returns the current usage status of the connection.
- `connect_to_database` is a placeholder for the database connection logic.

#### ConnectionPool Class
The `ConnectionPool` class manages a pool of `Connection` objects, ensuring a limited number of connections.

```python
class ConnectionPool:
    def __init__(self, num_connections):
        self.__num_connections = num_connections
        self.__connections = [Connection() for _ in range(num_connections)]
    
    def acquire(self):
        for connection in self.__connections:
            if not connection.is_used():
                connection.acquire()
                return connection
        return None
    
    def release(self, connection):
        if connection.is_used():
            connection.release()
```

- The `__init__` method initializes the pool with a specified number of connections (`num_connections`).
- The `acquire` method checks each connection to find an unused one, marks it as in use, and returns it.
- If all connections are in use, `acquire` returns `None`.
- The `release` method frees a connection, making it available for other clients.

#### Example Usage

```python
# Create a connection pool with 3 connections
pool = ConnectionPool(3)

# Acquire a connection
conn_1 = pool.acquire()

# Acquire another connection
conn_2 = pool.acquire()

# Acquire a third connection
conn_3 = pool.acquire()

# Attempt to acquire a fourth connection (None will be returned)
conn_4 = pool.acquire()

# Release a connection
pool.release(conn_3)

# Acquire a new connection after releasing one (reused connection)
conn_4 = pool.acquire()

# Release another connection
pool.release(conn_2)

# Acquire a new connection after releasing another one
conn_5 = pool.acquire()
```

- `conn_1`, `conn_2`, and `conn_3` are the first three connections acquired from the pool.
- `conn_4` is returned as `None` because all connections are in use.
- After releasing `conn_3`, `conn_4` is reused by the next client.
- The same behavior occurs with `conn_5`, which is reused from `conn_2`.

#### Singleton Pattern for ConnectionPool
Currently, the `ConnectionPool` can be instantiated multiple times. To ensure only one instance of the pool exists (singleton pattern), the class needs to be modified.

## 15
In the previous video, we addressed a major flaw in the `ConnectionPool` implementation: it was not a singleton. This meant that multiple instances of the `ConnectionPool` class could be created, which defeated the purpose of limiting the number of connections in the pool. In this video, we fixed this by turning the `ConnectionPool` into a singleton.

Here's a summary of the changes we made to implement the singleton pattern:

1. **Class-Level Instance Variable (`__instance`)**:  
   We introduced a class variable `__instance` which will hold the single instance of the `ConnectionPool`.

2. **Overriding `__new__` Method**:  
   We overrode the `__new__` special method. The `__new__` method is responsible for creating a new instance of a class. It is called before the `__init__` method. In the `__new__` method, we check if the class variable `__instance` is `None`. If it is, it means no instance of the `ConnectionPool` exists, so we create one and assign it to `__instance`. If an instance already exists, we return the existing instance.

3. **Singleton Behavior**:  
   With this change, no matter how many times you try to instantiate the `ConnectionPool`, only one instance will be created and used throughout the application. Any further attempts to instantiate it will return the already existing instance.

### Code Walkthrough of Changes:

- **Initialization Check**:  
  The first step in the `__new__` method is to check if `__instance` is `None`, which indicates that no instance has been created yet. If true, it proceeds to create a new instance.
  
- **Returning Singleton Instance**:  
  If `__instance` is not `None`, it means an instance already exists, and we simply return the existing instance, enforcing the singleton pattern.

Here is the updated implementation:

```python
class ConnectionPool:
    __instance = None  # Class variable to hold the instance

    def __new__(cls, num_connections):
        if cls.__instance is None:  # Check if instance exists
            print('No instance exists, creating a new one')
            cls.__instance = super(ConnectionPool, cls).__new__(cls)  # Create new instance
            cls.__instance.num_connections = num_connections  # Initialize connections
            cls.__instance.__connections = []
            for i in range(num_connections):
                cls.__instance.__connections.append(Connection())  # Add connection objects to the pool
        else:
            print('A previously created instance exists, returning that same one')
        return cls.__instance  # Return the singleton instance

    def acquire(self):
        for connection in self.__connections:
            if not connection.is_used():  # Find an unused connection
                connection.acquire()  # Mark it as in use
                return connection
        return None  # If no connections are available, return None

    def release(self, connection):
        if connection.is_used():  # If the connection is in use
            connection.release()  # Mark it as available
```

### Example Usage:

```python
# Create a ConnectionPool instance with 2 connections
pool = ConnectionPool(2)

# First client acquires a connection
conn_1 = pool.acquire()
print(conn_1)

# Second client acquires the second connection
conn_2 = pool.acquire()
print(conn_2)

# Third client attempts to acquire a connection (None because both are in use)
conn_3 = pool.acquire()
print(conn_3)  # Should be None

# Client 2 releases their connection
pool.release(conn_2)

# Now the third client can acquire the released connection
conn_3 = pool.acquire()
print(conn_3)
```

### Key Points:
- **Singleton Enforcement**:  
   The use of `__new__` ensures that no matter how many times `ConnectionPool` is instantiated, only one instance exists throughout the lifetime of the program.

- **Resource Management**:  
   The pool still functions as intended, where connections are recycled. When a client releases a connection, it becomes available for other clients to acquire.

- **Client Interaction**:  
   Clients can acquire and release connections. If all connections are in use, new clients will receive `None` until an existing client releases their connection.

This fix ensures that the `ConnectionPool` behaves as a singleton, adhering to the design pattern and maintaining efficient resource management.