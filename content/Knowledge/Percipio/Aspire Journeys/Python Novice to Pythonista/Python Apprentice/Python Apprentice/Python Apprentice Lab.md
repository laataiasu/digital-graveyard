---
date: 2001-01-01
---

# Python Apprentice Lab

4 Hours Remaining
Python Apprentice
Getting Started
In this lab, you will be presented with a series of exercises. Each exercise will introduce a task or series of tasks to perform followed immediately by a step-by-step instruction set detailing how to complete the tasks. Each exercise includes a question to test your understanding of the technology and tasks presented in the exercise.

The exercises presented in this lab include:

Exercise 1 - File Handling

Exercise 2 - Object Oriented Programming

Exercise 3 - Special Method Names

Exercise 4 - Static and Abstract Classes

Exercise 5 - Use a List as a Stack

Exercise 6 - Python Queues

Exercise 7 - Graphs as an Adjacency Matrix

Exercise 8 - Tree Traversal

The Lab Configuration section details the devices, operating systems, tools, and software available in the lab. No need to download or configure anything - unless of course it is required as part of an exercise.

When you’re ready to begin, move to the next page using the navigation button below.

Lab Configuration
Devices
Ubuntu Desktop

Visual Code Studio
PyCharm
Assets
The assets are located in the 'ASSETS' folder on the desktop

---

Python Apprentice
3 Hr 56 Min Remaining
Exercise 2 - Object Oriented Programming
Introduction
Welcome to the Object Oriented Programming Python Lab. Your assignment for this exercise is to derive a class and implement polymorphism in your program using Python

Task
Derive a class and implement polymorphism in your program using Python

Implement a Python class to be derived
Implement methods in the class
Implement a subclass
Override methods in the subclass
Demonstrate use of the classes by printing results and output to the console
Instructions
Task 1 - Implement a Python class to be derived
The first step is to implement a Python class to be derived. So the class we've created is called Service. This will simulate a base class for a service running on a particular host and port served over the Internet. We have class Service. And then we defined a __init__ method to be called when the class is created. We have self, host, and port as its parameters. And I set self.host = host and self.port = port.
# Implement a python class to be derived
class Service:

  def __init__(self, host, port):
    self.host = host
    self.port = port
Task 2 - Implement methods in the class
The next step is to implement methods in the class. We implement two methods, getService and getData. Then, def getService with self, so it's a member method. Then return f string, or formatted string, with {self.host} : {self.port}. And then getData returns an empty string because at this point the service is not defined. It needs to be subclassed for a particular implementation.
# Implement methods in the class
  def getService(self):
    return f'{self.host}:{self.port}'

  def getData(self):
    return ''
Task 3 - Implement a subclass
The next step is actually to implement a subclass. Scroll down, we have class Web. And then in parentheses we have Service, the base class. Our subclass is Web, and it implements its own init method, so def__init__ with self. And it has a protocol, in this case http.

Now, you can imagine a Web service with an HTTPS protocol for a secure service. We have the protocol in there to simulate that, and then we have host = 0.0.0.0. We have a default host which sets to the 0 host and port=80, the default HTTP port. And in this method, we actually call the base class init method using super(). We get the super, so this is the base class implementation, __init__, and we pass host and port to it. So we don't need to repeat ourselves and carry out the initialization in service. We don't need to repeat it here in Web. And then I set self.protocol=protocol.

# Implement a subclass
class Web(Service):

  def __init__(self, protocol='http', host='0.0.0.0', port=80):
    super().__init__(host, port)
    self.protocol=protocol
Task 4 - Override methods in the subclass
Then the next step of the exercise is to override methods in the subclass. We override getService and getData. GetService returns a formatted string with self.protocol://. We'd have the typical http:// followed by host:port. And then the getData, if it's a Web service we expect some sort of Web data to be returned, which could be some HTML. So just return html in the open and closed tags followed by ..., an ellipsis to simulate something being there. And then we close the HTML tag.

Now, for the sake of this exercise, to highlight the subclass, we implement a second subclass. Which wasn't required by the exercise, but we want to to highlight the subclassing in another way.

We have class Mail which subclasses from Service. It has its __init__ method, so def __init__ with self. It sets a method, so a mail method, and it defaults to IMAP. The host is 0.0.0.0, and the port is 143, the default port init, which is the default IMAP port. We call the super()__init__ method inside of this init with the host and port. And then we set self.method=method. And in this case, it overrides the getData method, and it returns something that simulates a mail message. It has a To, a From, and a Content-Type. And then a \n\n, so two new lines, nHello, World to simulate the message body. We'll see this in the output when we run the program.

# Override methods in the subclass
  def getService(self):
    return f'{self.protocol}://{self.host}:{self.port}'

  def getData(self):
    return '<html>...</html>'

class Mail(Service):
  def __init__(self, method='IMAP', host='0.0.0.0', port=143):
    super().__init__(host,port)
    self.method=method

  def getData(self):
    return 'To: <steve@example.com>\nFrom: <jane@example.com>\nContent-Type: text/plain;\n\nHello, World!\n'
Task 5 - Demonstrate use of the classes by printing results and output to the console
The last step of the exercise is to demonstrate use of the classes by printing results and outputting to the console. Create a Service, create a Web instance, and a Mail instance. We have s = Service with 0.0.0.0 as the host and 8888 as the port. And print the Service call to getService. And print an empty print to put some space between this example and the next one.

We have http = Web(). And then print Web Service with a call to http.getService, and print the getData method. So http.getData, and then an empty print to put a new line character in and put some space between this example and the next one.

Then we have the mail variable = the Mail class, where we specify a method = POP3, we specify a different mail method. Print Mail Service, the formatted string, with a call to getService. And then print mail.getData.

# Demonstrate use of the classes by printing results and output to the console
s = Service('0.0.0.0', 8888)
print(f'Service: {s.getService()}')
print()

http = Web()
print(f'Web Service: {http.getService()}')
print(http.getData())
print()

mail = Mail(method='POP3')
print(f'Mail Service: {mail.getService()}')
print(mail.getData())
Terminal
Run the program and have a look at the Debug Console to see the results. We see the Service call to getService returns 0.0.0.0:8888, as expected. The Web Service returns the http:// with the host:port, the 0.0.0.0:80. And then the getData call returns the HTML tag example. And then the Mail Service returns something similar. It returns the host:port number and returns the contents of the mail message, translating the \n characters to actual new line characters. So we have To, From, Content-Type, and Hello, World as the message body. And that concludes this exercise.
terminal_app_02.png

Check your work
Check each box to confirm completion of the task.

Implement a Python class to be derived
Implement methods in the class
Implement a subclass
Override methods in the subclass
Demonstrate use of the classes by printing results and output to the console
Select Next below to move to the next exercise.

---

Python Apprentice
3 Hr 52 Min Remaining
Exercise 3 - Special Method Names
Introduction
Welcome to the Special Method Names Python Lab. Your assignment for this exercise is to Implement special method names in a Python class and call them in your program

Task
Implement special method names in a Python class and call them in your program

Create a basic Python class
Implement an __init__ method
Implement __repr__ and __str__ methods
Implement comparison or numeric special methods as appropriate for your class
Instructions
Task 1 + 2
Start from functools import total_ordering. Which helps us compare items or compare classes just by implementing a couple of the ordering methods. And then Python will take care of implementing the rest.

The first step is to create a basic Python class. We have @total_ordering, which is the decorator to direct this class to fill in the ordering methods based on what we implement. Implement a less than and an equals operator, and total_ordering will fill in the rest. So it will fill in the greater than and less than or equal or greater than or equal, everything it needs to compare our Book class.

Define a class called Book. And then the next step is to implement a double_init method. We have def __init__ which takes self and then title, author and isbn. It's going to construct a record of a book with the title, author and isbn. Set self.title = title, self.author = author and self.isbn = isbn.

from functools import total_ordering

# Create a basic python class
@total_ordering
class Book:
# Implement an __init__ method
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
Task 3 - Implement __repr__ and __str__ methods
We set the member attributes or member variables to the parameters that are defined in this method. Then we implement the representation and string methods. Our __repr__ and __str__ methods. So for def __repr__, which takes a single argument, self, and it returns a representation of this class. It returns this formatted string with the braces and the variables enumerated. It has an open angle bracket and a closed angle bracket. It has the __module__, the type of the object or the type of the class, in this case book. Object at and then it has a hex id of self. It takes the id of self and it uses the hex value of that to say where this object is defined. It's almost like a memory location or a memory reference. And then it has in parentheses, the title, the author and the isbn. The representation is more for debugging purposes and the string representation is a human readable string.

We define them slightly differently in most cases. Define the __str__ method and return the f string of the self.title in double quotes by self.author in double quotes. ;isbn:v and then the isbn number for the book. And we need to implement comparison or numeric special methods as appropriate for our class.

Implement the less than equals and all the other comparison operators get populated. Because we've supplied the total_ordering decorator above the class. For less than, we have def __lt__ with self and other. And our return, self.author, is less than other.author. We compare in alphabetical or lexicographical order the author strings. And if one is less than the other, then the book is less than the other book in terms of ordering. Then put a backslash so we can have a multiline statement. If self.author is equal to other.author, if it's the same author then we look at the title to see the order they should be in. So self.author equal to other.author and self.title is less than other.title then the books are less, then the books can be compared this way. So that's how we define the less than.

To define equality, so we have a def __eq__ with self and other as the parameters. In this case true gets returned if the authors are equal and the titles are equal between self and other. We'll implement these classes.

# Implement __repr__ and __str__ methods
  def __repr__(self):
    return '<{0}.{1} object at {2}> ({3}, {4}, {5})'.format(
      self.__module__, type(self).__name__, hex(id(self)),
      self.title, self.author, self.isbn)

  def __str__(self):
    return f'"{self.title}" by "{self.author}"; ISBN: {self.isbn}'

  def __lt__(self, other):
    return (self.author < other.author) or \
            (self.author == other.author and self.title < other.title)

  def __eq__(self, other):
    return (self.author==other.author and self.title == other.title)
Task 4 - Implement comparison or numeric special methods as appropriate for your class
Create some books with authors and titles and isbns and we'll run some of the comparisons to verify the results. We have b = Book with Ulysses, by Joyce, James. So James Joyce, we put last name comma first name and then an ISBN number. We create a second book, b2 equal to the same definition with Ulysses, Joyce, James and the same isbn. So if we compare these two books they should be equal.

But first call print of b. If you just supply the variable without anything else, it will take the string representation of the book. If I call the repr function on b, it will give us the representation of the book. And if I print b == b2, and check the result. It will print true or false whether or not these books are the same or have the same author and title.

And then finally, create another book called d = Book of Pride and Prejudice by Austen, Jane and fill in N/A for the isbn. And then on line 36, we print whether or not d is less than b. So comparing them which should be true because Austin in terms of alphabetical or lexicographical order, comes before Joyce. This should return true.

# Implement comparison or numeric special methods as appropriate for your class
b = Book('Ulysses', 'Joyce, James', '9780679722762')
b2 = Book('Ulysses', 'Joyce, James', '9780679722762')
print(b)
print(repr(b))
print('b == b2: {}'.format(b==b2))

d = Book('Pride and Prejudice', 'Austen, Jane', 'N/A')
print('d < b: {}'.format(d<b))
Terminal
Now let's run the code and we can have a look at the results. So in this case, we get the string representation Ulysses by Joyce James with the ISBN number. Then we print the representation of it with main.book object at 0x and this hexadecimal value. And in parentheses Ulysses, Joyce, James, and the ISBN. And the way we've defined b and b2 with the same author and title, they are true and d is less than b. That returns true as expected because Austen is less than Joyce. And that concludes the exercise.
terminal_app_03.png

Check your work
Check each box to confirm completion of the task.

Create a basic Python class
Implement an __init__ method
Implement __repr__ and __str__ methods
Implement comparison or numeric special methods as appropriate for your class
Select Next below to move to the next exercise.

---

Python Apprentice
3 Hr 45 Min Remaining
Exercise 4 - Static and Abstract Classes
Introduction
Welcome to the Static and Abstract Classes Python Lab. Your assignment for this exercise is to implement an abstract class and use static methods in a Python program

Task
Implement an abstract class and use static methods in a Python program

Create a class that implements an abstract method
Create a subclass
Implement a static method in the subclass
Instantiate the class and output its contents
Instructions
Task 1 - Create a class that implements an abstract method
For this exercise start out by importing some important features or methods that we need to implement our abstractions. On line 1 we have from abc import the uppercase ABC, abstractmethod. The ABC stands for abstract base class and abstractmethod is a decorator for abstract methods.

The second step of the exercise is to create a class that implements an abstract method. Create a class Post(ABC) with ABC as its parent class. On line 5 we have @abstractmethod, we have the decorator. Then def getTitle with self to make it a member method or member function, and I define it with pass. It has the pass keyword because it doesn't implement a body to the method.

On line 9, there's another @abstractmethod decorator with another method def getText. We have two abstract methods in this abstract class called Post.

from abc import ABC, abstractmethod

# Create a class that implements an abstract method
class Post(ABC):
  @abstractmethod
  def getTitle(self):
    pass

  @abstractmethod
  def getText(self):
    pass
Task 2 + 3
Now we need to create a subclass and implement a static method in the subclass. Those are the next two steps of the exercise. Create a class link which subclasses or inherits from Post, our abstract base class. It defines its __init__ method that take two parameters, a title and a URL, and then it sets the self.title and the self.url to their given variables.

On line 20, define the getTitle which is required because it's an abstract method in the base class. And it just returns self.title and then getText which returns self.url. The text of the link is the actual URL of that link. And we implement two more subclasses.

# Create a subclass
# Implement a static method in the subclass
class Link(Post):
  def __init__(self, title, url):
    self.title = title
    self.url = url

  def getTitle(self):
    return self.title

  def getText(self):
    return self.url
The first one is comment. A comment is a type of post. We have class Comment(Post). In its __init__ method, it takes the parameters, title, comment, and user. Each comment has a title of the comment, the comment itself, the comment body or text, and the user that submitted the comment. On line 29, set self.title is equal to title. Check the length of the comment and if it's greater than 500 characters, raise a value error saying that the comment is too long. Otherwise I set comment equal to comment and self.user equals user. Implement the getTitle and getText methods, as well as a getUser method. And they return their respective variables. In the case of getText, the text of a comment is the actual comment body itself, so it returns self.comment.
class Comment(Post):
  def __init__(self, title, comment, user):
    self.title = title
    if(len(comment) > 500):
      raise ValueError('Comment too long.') 
    self.comment = comment
    self.user = user

  def getTitle(self):
    return self.title

  def getText(self):
    return self.comment

  def getUser(self):
    return self.user
And then my third subclass of our abstract base class Post is an article. We have class Article(Post). In its __init__ method, it has a title and a body, so the body of the article, and it sets the respective variables of self.title and self.body. And it returns the title for getTitle and the getText method returns self.body.
class Article(Post):
  def __init__(self, title, body):
    self.title = title
    self.body = body

  def getTitle(self):
    return self.title

  def getText(self):
    return self.body
Task 4 - Instantiate the class and output its contents
Now we need to instantiate the class and output its contents. Start by creating a list called posts. This will have the different posts, whether it be a link, a comment, or an article, and we'll add them to this list.

On line 59 create a link a = Link, that's called link title with a link http://example.com/link.html. Then call post.append(a), so we append this to the posts list. And then I print a.getText() and print an empty print statement to put a space between this and the next part of the output.

Then on line 64 we have b = Comment with the title as Comment title, the body of the text comment, and the user Steve. Create an article c = Article with Article title and Article text as its arguments. Then call posts.append(b) and then posts.append(c). Now loop over the posts and call getTitle on each of these posts, because they all implement the getTitle. On line 69, we have for p in posts, print p.getTitle.

# Instantiate the class and output its contents
posts = []
a = Link('Link title', 'http://example.com/link.html')
posts.append(a)
print(a.getText())
print()

b = Comment('Comment title', 'comment', 'Steve')
c = Article('Article title', 'Article text')
posts.append(b)
posts.append(c)

for p in posts:
  print(p.getTitle())
Terminal
Run the code, And we get the output. We get the URL, so the getText called on the variable a, which was a link so it returns the link. And then in our for loop, the getTitle of each of the elements in the Posts list, are Link title, Comment title, and Article title as expected. And that concludes this exercise.
terminal_app_04.png

Check your work
Check each box to confirm completion of the task.

Create a class that implements an abstract method
Create a subclass
Implement a static method in the subclass
Instantiate the class and output its contents
Select Next below to move to the next exercise.

---

Python Apprentice
3 Hr 38 Min Remaining
Exercise 5 - Use a List as a Stack
Introduction
Welcome to the Use a List as a Stack Python Lab. Your assignment for this exercise is to recognize how a Python list can be used as a stack by loading and unloading elements from the same end and to answer the assessment questions

Task
Recognize how a Python list can be used as a stack by loading and unloading elements from the same end

Create a List to be used as a stack
Push elements onto the stack
Pop elements off of the stack
Output the contents of the stack
Instructions
Task 1 - Create a List to be used as a stack
The first step in the exercise is to create a list to be used as a stack. Now you can do this directly, or you can incorporate the list inside of a stack class. We can implement some stack functions and carry out the exercise on the class itself. Define a class stack, and then I define the __init__ method to be used when the stack is instantiated. It has initial values as a parameter and max_size which defaults to none. But if we want, we can set a max_size of the stack, and prevent it from pushing new elements on to the stack if it is full, if it's reached the max_size. And then, inside the ¬¬__init__ method, check to see if isinstance of initial values is a list. So if it's a list, then we can set self.stack equal to those initial_values, otherwise, we set self.stack equal to initial_values wrapped in square brackets. We make the value itself if it's a single value, we make it into a list.

We set self.max_size = max_size, which defaults to none. And self.size, the current size is equal to len(self.stack),

# Create a List to be used as a stack
class Stack:
  def __init__(self, initial_values, max_size=None):
    if isinstance(initial_values, list):
      self.stack = initial_values
    else:
      self.stack = [initial_values]

    self.max_size = max_size
    self.size = len(self.stack)
Define the push function. push takes a value and it pushes it onto the list or appends it to the list. Then I check if self.max_size:, so if the variable is defined, check to see if self.size < self.max_size. If there's room on the stack, then append it to the stack variable to the list. Call stack.append value, and increment the size by 1, so + = 1, else raise a value error that says the stack is full. And then the else that corresponds to the max_size variable, if max_size is not defined, call self.stack.append(value_, and self.size + = 1 to increment it.
  def push(self, value):
    if self.max_size:
      if self.size < self.max_size:
        self.stack.append(value)
        self.size += 1
      else:
        raise ValueError('Stack is full!')
    else:
      self.stack.append(value)
      self.size += 1
Define a top method, so many stacks have this top method that gets the top most element on the stack, but it doesn't actually pop it off. The pop checks to see if the stack is empty, so I call self.is_empty. And if that's true, it returns none, otherwise it returns self.stack index that- 1. That's the last element in the list, which we defined to be the top of the stack.

Define the pop function, which checks to see if the size is greater than zero, and if it is, it calls self.stack.pop. Put the self.stack.pop in an if function because the pop function will return a value if there's one there. And then we can decrement the size by one and return true otherwise I return false.

My is_empty method just checks to see if self.size is equal to zero and if it is it returns true. Otherwise it returns false, I implement the special function double underscore len. If the len function is called on our stack, it returns the size. And if a print function is called on our stack, or if it's turned into a string, it returns the string representation of the stack list. So it makes an f string of self.stack.

 def top(self):
    if self.is_empty():
      return None
    return self.stack[-1]

 def pop(self):
    if self.size > 0:
      if self.stack.pop():
        self.size -= 1
        return True
    return False

 def is_empty(self):
    if self.size == 0:
      return True
    return False

 def __len__(self):
    return self.size

 def __str__(self):
    return f'{self.stack}'
Task 2 - Push elements onto the stack
Now the next step of the exercise is to push some elements onto the stack. Create a stack equal to the stack class with the initial values, the list of strings, these names Steve, Jane and Jim. Then call stack.push on Alice. The string Alice, put another name and stack.push Bob, and then I print the contents of the stack
# Push elements onto the stack
stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')
print(stack)
Task 3 + 4
Now we need to pop elements off of the stack and output the contents of the stack. Call print stack.pop, which will return true if there's an element to pop. I print the state of the stack at that point after that pop, I call pop again, so stack.pop, and then print the stack.

One way we can iterate through all of the elements popping elements off of the stack is inside of a loop. We have while len(stack) > 0, so while there are elements on the stack call stack.pop. And after this executes the len of stack at this point should be zero and it should print stack is empty.

# Pop elements off of the stack
# Output the contents of the stack
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

while len(stack) > 0:
  stack.pop()

if len(stack) == 0:
  print('Stack is empty!')
Terminal
Now run the code, and then in the debug console, we get the output of the stack at various points in the program. So we start with Steve, Jane, Jim, Alice and Bob, so we initialize it with the first three names. Then we push Alice and Bob onto the stack, and then we call stack.pop. So that returns true, which leaves us with Steve, Jane, Jim and Alice and Bob is popped off at the top of the stack. We call pop again, which returns true and then Steve, Jane and Jim are left on the stack, and Alice is gone. Then we remove all of the elements in our loop, we pop all of them off the stack. And then at the end the stack is empty as expected, and that concludes the exercise.
terminal_app_05.png

Check your work
Check each box to confirm completion of the task.

Create a List to be used as a stack
Push elements onto the stack
Pop elements off of the stack
Output the contents of the stack
Question 1
Assume you push elements onto the stack in the following order.


stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')

What would be the first name "popped" off the stack?

Jane
Steve
Bob
Alice
Question 2
Assume you push elements onto the stack in the following order.


stack = Stack(['Steve', 'Jane', 'Jim'])
stack.push('Alice')
stack.push('Bob')

What would be the command print(stack.pop()) return?

False
['Bob', 'Alice', 'Jim', 'Jane', 'Steve']
['Steve', 'Jane', 'Jim', 'Alice', 'Bob']
True
Select Next below to move to the next exercise.

---

Python Apprentice
3 Hr 35 Min Remaining
Exercise 6 - Python Queues
Introduction
Welcome to the Python Queues Python Lab. Your assignment for this exercise is to use the native Queue class of Python and perform standard queue operations on it and to answer the assessment questions

Task
Use the native queue class of Python and perform standard queue operations on it

Implement a queue using the appropriate Python collection
Add elements to the queue
Pop elements from the queue in first-in, first-out fashion
Display the final contents of the queue
Instructions
Task 1 - Implement a queue using the appropriate Python collection
For this exercise, from collections import deque, which is short for a double ended queue, which is contained in the collections library from the Python standard library.

Now the first step of the exercise is to implement a queue using the appropriate Python collection. Well, the appropriate collection is a deque. Now, you could potentially do it with a list so you can implement a queue using a list, but it's inefficient to do so because of the way list is implemented. It's not recommended to use a list to implement a queue. If you're implementing a stack, a list is a perfectly fine data structure. But in this case with implementing a queue, we're going to use a deck. Now in our case, the queue is ‘a first in first out queue’, so a single ended queue, but we'll only be pulling off the front of the queue.

We have a class queue, which extends the basic object. And then define the __init__ function, which takes the initial values and the max_size. We'll have an option to set a max size of our queue, and once it reaches that size, the queue will be full. Now this wasn't a strict requirement for this exercise, but include it so we can demonstrate how this could be done.

We set self.queue = deque with the initial_values. Set self.max_size = max_size. And self.size is the number of elements in the initial_values or the len of initial_values. Define a push function, so we can push elements into the queue. And this takes a value that we're going to push. And then inside the body of the function, check to see if self.max_size: is set. If it's none, we just append the element to the queue, and increment the size by 1. So call self.queue.append parsing value as the argument, and set self.size += 1, to increment it by 1.

If the max size is set, we make sure that the current size, self.size, is less than the max size. If it is, we call self.queue.append(value) and self.size +=1. Otherwise, raise a value error saying that the queue is full.

from collections import deque

# Implement a queue using the appropriate python collection
class Queue(object):
  def __init__(self, initial_values, max_size=None):
    self.queue = deque(initial_values)
    self.max_size = max_size
    self.size = len(initial_values)

  def push(self, value):
    if self.max_size:
      if self.size < self.max_size:
        self.queue.append(value)
        self.size += 1
      else:
        raise ValueError('Queue is full!')
    else:
      self.queue.append(value)
      self.size += 1
The next method is a method called top. This is the first element or the current element in the queue that's next to come off. Checked to see if the queue is empty, so if self.is_empty() is true then return none, so there's no element in the queue. Otherwise, return self.queue at index 0, so this is the first element in the queue. Define def pop, so it's a pop function that will pop the current element off of the queue. Check to see if the size is greater than 0. If it is, then there are items that we can pop from the queue. And then call self.queue.popleft. Popping left pops the first element off, and popping if we just call pop on queue, it will pop the rightmost element off. But that would be pulling from the queue from the wrong end because we want it in ‘first in first out’ fashion. So if this is true, if there's an element to pop off, then decrement the size. So self.size -=1, and return true saying that the pop was successful, otherwise return false. If we call pop on an empty queue, it will return false.

We have def is_empty, so this is an empty function, checks the self.size and if it's 0 it returns true, otherwise it returns false. Define a __len__ special function to return the size. If the len function is called on the queue, so I returned self.size, and the __str__ or string representation of the queue, which returns the f string of self.queue, which will output the values that are currently in the queue.

Now we can continue with the exercise, start by initializing the queue, so we have queue = Queue class. So we're creating an instance with the list of initial values being Steve, Jane and Joe, and the max_size to be 6. We can have 6 elements in this queue before we reach the limit. Then call print len of queue to see how many elements are currently in the queue. At this point, it should be 3. Print an empty line.

  def top(self):
    if self.is_empty():
      return None
    return self.queue[0]

  def pop(self):
    if self.size > 0:
      if self.queue.popleft():
        self.size -= 1
        return True
    return False

  def is_empty(self):
    if self.size == 0:
      return True
    return False

  def __len__(self):
    return self.size

  def __str__(self):
    return f'{self.queue}'

queue = Queue(['Steve', 'Jane', 'Joe'], 6)
print(len(queue))
print()
Task 2 - Add elements to the queue
The next step of the exercise, is to add elements to the queue. So we call queue.push on the following strings, the following names, Alice, Bob, James and Sally. So if we count how many names we have to this point, we have three initially, and then we add four more. Sally will be the seventh name, so we should see a problem here with the max size if it's done correctly.

And then after that, print the queue, print the len of queue, and then print an empty line.

# Add elements to the queue
queue.push('Alice')
queue.push('Bob')
queue.push('James')
queue.push('Sally')
print(queue)
print(len(queue))
print()
Task 3 - Pop elements from the queue in first-in, first-out fashion
Now we are going to pop the elements. So we're popping elements from the queue in ‘first in, first out’ fashion. The first one in is Steve, so that's the one that should be popped out. Print queue.top to make sure it is Steve then call queue.pop, and print the queue. Push another name, queue.push Mallory. Print this state of the queue at that point, and then print queue.top, and an empty print.
# Pop elements from the queue in first-in, first-out fashion
print(queue.top())
queue.pop()
print(queue)
queue.push('Mallory')
print(queue)
print(queue.top())
print()
Task 4 - Display the final contents of the queue
Then we display the final contents of the queue by printing queue. And then, while len of queue is greater than 0, I call queue.pop to remove everything off of the queue.
# Display the final contents of the queue
print(queue)

while len(queue) > 0:
  queue.pop()
Terminal
Now We run the program and see what happens in the debug console. At the very bottom, we see value error queue is full, and that's what we expected when we pushed Sally onto the queue. If we scroll up, we get the three printed from line 45 or we printed the len of queue, but then it only gets to line 52 before it fails. So we’re going to comment out queue.push of Sally on line 52, so that we can see the rest of the program execute successfully.

Now run the program again, and in this case, we get more output. We get the queue printed which is a deque from line 53 with Steve, Jane, Joe, Alice, Bob and James. And then call the length which is 6. And then top at this point is Steve, call pop, and then print the queue again. In this case, it starts at Jane, and then Joe, Alice, Bob and James with Steve being popped off the front of the queue. And then push Mallory onto the queue. And then at this point, the top of the queue is Jane, so when we print the results, we have Jane, Joe, Alice, Bob James, and Mallory. And that concludes this exercise.

terminal_app_06.png

Check your work
Check each box to confirm completion of the task.

Implement a queue using the appropriate Python collection
Add elements to the queue
Pop elements from the queue in first-in, first-out fashion
Display the final contents of the queue
Question 1
Which of the following are valid methods used to add an item to a Python queue?

append
put
push
insert
Question 2
Which of the following are valid methods used to retrieve an item to a Python queue?

get
push
insert
put
Select Next below to move to the next exercise.

---

Python Apprentice
3 Hr 30 Min Remaining
Exercise 7 - Graphs as an Adjacency Matrix
Introduction
Welcome to the Graphs as an Adjacency Matrix Python Lab. Your assignment for this exercise is to implement a graph as an adjacency matrix in Python and to answer the assessment questions

Task
Implement a graph as an adjacency matrix in Python

Create a graph class that implements an adjacency matrix
Implement a method to add an edge to the graph
Implement a method to remove an edge from the graph
Implement a method to display the contents of the matrix
Construct a graph and display its contents
Instructions
Task 1 - Create a graph class that implements an adjacency matrix
The first step in the exercise is to create a graph class that implements an adjacency matrix. On line 2, we have a class graph. And in this graph, define a __init__ method that takes self and size as parameters. Inside the body of the class graph, define a __init__ method that defines a single parameter size. It's going to be a square matrix of the given size, its size by size. Define the matrix, self.m equals the double brackets. These square brackets define a list. It's going to be a list of lists to define our adjacency matrix.

And then for _ in range(size), so we don't need the loop variable, so I just put it as an underscore and we loop size times. We're going to do self.m.append, and we're going to have 0 array times size. This is an adjacency matrix that's initialized to all zeros. Then self.size = size.

# Create a graph class that implements an adjacency matrix
class Graph:
  def __init__(self, size):
    self.m = []
    for _ in range(size):
      self.m.append([0] * size)
    self.size = size
Task 2 - Implement a method to add an edge to the graph
Now we need to implement a method to add an edge to the graph. It's to set the appropriate cell in our matrix to be 1 to designate an edge. The parameters that define the nodes are v and w. On line 11, We check to see that v = w. If it is, then we raise a ValueError saying that we cannot add an edge to itself. Then we set, self.m of vw, so we're indexing at v and w equal to 1, and we need to set self.m[w][v] = 1. So an edge from one node to another and back so that edge is complete.
# Implement a method to add an edge to the graph
  def add(self, v, w):
    if v == w:
      raise ValueError('Cannot add an edge to itself.')
    self.m[v][w] = 1
    self.m[w][v] = 1
Task 3 - Implement a method to remove an edge from the graph
If there's an edge from node v to w, there's automatically an edge from w to v. Now we need to implement a method to remove an edge from the graph. We define a remove function that specifies v and w. Now if self.m[v][w] is already equal to 0, so if there's no edge, then we can just skip the removal. Otherwise, we set self.m at v and w equal to 0 and at w and v equal to 0.
# Implement a method to remove an edge from the graph
  def remove(self, v, w):
    if self.m[v][w] == 0:
      return
    self.m[v][w] = 0
    self.m[w][v] = 0
Task 4 - Implement a method to display the contents of the matrix
We need to implement a method to display the contents of the matrix. Overload the special string method the __str__ method, so that we can do a print on the graph instance and it will print the contents. Define this, and then in the body of this method, we have retval equals an empty string.

We start with an empty string, then for i in self.m:, so we loop over m, and we do it for j in i. So i will be a list, since m is the list of lists. In the inner list, we have for j in i:, and then we set retval plus equals the formatted string of the node value. Whether it's a 1 or 0, so that will be contained in j and then a tab character, so we separate each cell by a tab. And then retval += \n. So after each row, we start a new row on a new line, so that's why we need the newline character. And then in the end, we return retval, which should be our constructed string with the contents of the matrix.

# Implement a method to display the contents of the matrix
  def __str__(self):
    retval = ''
    for i in self.m:
      for j in i:
        retval += f'{j}\t'
      retval += '\n'
    return retval
Task 5 - Construct a graph and display its contents
Then the next step is to construct a graph and display its contents. Set the graph, all in lowercase equal to the graph class with the uppercase G, and we set it to be 6. This is a size of 6, so it's a 6 by 6 graph, which means it has 6 nodes and the nodes are enumerated from 0 to 5. We do graph.add(0, 3). So there's an edge from 0 to 3 and 3 to 0. And then graph.add(1, 4), graph.add(2, 5) and graph.add(0, 5). This constructs a graph with the edges as we defined here. And then we just call print graph, which calls the string function we defined above.
# Construct a graph and display its contents
graph = Graph(6)
graph.add(0, 3)
graph.add(1, 4)
graph.add(2, 5)
graph.add(0, 5)

print(graph)
Terminal
Now we run the code, so we can see the results. And here we get our graph, so we have each row. So enumerated from 0, 0, 1, 2, 3, 4, 5. In this case if we go along the row from 0, 1, 2, 3, so this particular one is in the 0 row and the third column. If we're calling from 0 to 0 row and column 3, so that's our graph node from 0 to 3. And then the final one in the first row is our edge from 0 to 5.

Then in the next row, we have our edge from 1 to 4, and then our edge from 2 to 5 in the next row. Now in the bottom part, you'll notice that if you draw a line down the middle of the graph, down the diagonal, this graph is symmetrical. And it will always be symmetrical because it's an un-directed graph, which means if there's a node from 0 to 3, there's automatically a node from 3 to 0. And that concludes this exercise.

terminal_app_07.png

Check your work
Check each box to confirm completion of the task.

Create a graph class that implements an adjacency matrix
Implement a method to add an edge to the graph
Implement a method to remove an edge from the graph
Implement a method to display the contents of the matrix
Construct a graph and display its contents
Question 1
Which of the following would complete the code to add an edge to a graph that implements an adjacency matrix?


def add(self, v, w):
    if v == w:
      raise ValueError('Cannot add an edge to itself.')
    MISSING CODE
    MISSING CODE

OPTIONS:
A.


self.m(v)*(w) = 1
self.m(w)*(v) = 1

B.


self.m(v)(w) = 1
self.m(w)(v) = 1

C.


self.m[v]*[w] = 1
self.m[w]*[v] = 1

D.


self.m[v][w] = 1
self.m[w][v] = 1
Option A
Option B
Option C
Option D
Question 2
Which of the following would complete the code to display the contents of the matrix?


  def __str__(self):
    retval = ''
    for i in self.m:
      for j in i:
        MISSING CODE
      retval += '\n'
    return retval
retval += f'{j}\t'
retval += f'{i}\t'
retval += f'{j, I }\t'
retval -= f'{j}\t'
Select Next below to move to the next exercise.

---

Python Apprentice
3 Hr 27 Min Remaining
Exercise 8 - Tree Traversal
Introduction
Welcome to the Tree Traversal Python Lab. Your assignment for this exercise is to traverse a Binary Search Tree (BST) in depth-first and breadth-first order in Python and to answer the assessment questions

Task
Traverse a Binary Search Tree (BST) in depth-first and breadth-first order in Python

Create a class to implement a binary search tree
Implement an insertion method
Implement a method to traverse the tree in depth-first order
Implement a method to traverse the tree in breadth-first order
Create an instance of the tree and insert data
Display the data points in their traversal orders
Instructions
Task 1 - Create a class to implement a binary search tree
The first step is to create a class to implement a binary search tree. For this, we start with a class Node. And in this class, we define a __init__ method that takes a value, the value for that particular node.

We have self.value = value. Since it's a binary search tree, we have two branches, which we typically call right and left. The right branch or a right node points to another node that has a value greater than the current one. And the left branch or left node will eventually point to another node that has a value less than the current value. The right takes greater values and the left takes lesser values.

# Create a class to implement a binary search tree
class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None
Task 2 - Implement an insertion method
Then the next step is to implement an insertion method. We have def insert, and this takes a value. What happens here is a bit of logic that's very important so that we can handle all of the cases of where to insert a node. The first thing we check if self.value, so if the current node is not equal to the value. Then we check to see if the value is greater than the current value, so greater than self.value. And if self.write is none, if it is a greater value, we look to the right branch. And if it's none, then we set self.write = node of the value.

We insert the node when we reach none. Otherwise, we call self.write.insert. We can think of it as recursively going down the rightmost nodes until we reach this place where we can insert the value. elif value is less than self.value. If the value is less than the current value of the current node, then if self.left is None, then we set self.left = Node(value). We create a new node, which left points to, otherwise we take self.left and we call its insert method with the value. Now what if the value is the same? Now in this solution, we’re assuming that the values are unique. If the value is equal, we assume that it's already there and we don't need to insert it again. So there are no duplicate values.

# Implement an insertion method
  def insert(self, value):
    if self.value != value:
      if value > self.value:
        if self.right is None:
          self.right = Node(value)
        else:
          self.right.insert(value)
      elif value < self.value:
        if self.left is None:
          self.left = Node(value)
        else:
          self.left.insert(value)
Task 3 - Implement a method to traverse the tree in depth-first order
Then we need to implement a method to traverse the tree in depth first order. We want to go down the nodes of the tree till we reach the bottom, and then we insert the node value. Set this items variable equal to an empty list. We'll add the values to this list in the order that we traverse them. Now if node is set, so if it's none, we take items.append the node value. Then we take items = items + the result of self.depth traversal of the left nodes. And items = items + self.depth traversal of the right node.

We're going down the nodes, down the left nodes and down the right nodes. Now since this is being called recursively, we're calling depth traversal with each node starting with the left and going down the left most branches and then the right most branches. And this will recursively build up the items with all of the nodes that are traversed. And then in the end we return items, so it doesn't return items until it's traversed down the depth of an entire branch.

# Implement a method to traverse the tree in depth-first order
  def depth_traversal(self, node):
    items = []
    if node:
      items.append(node.value)
      items = items + self.depth_traversal(node.left)
      items = items + self.depth_traversal(node.right)
    return items
Task 4 - Implement a method to traverse the tree in breadth-first order
The next step is to implement a method to traverse the tree in breadth_first order. There are a number of ways we can do this depending on how we view this breadth_first. We want to think of going from left to right. We start at the left branch, and we move across the graph to the rightmost. So breadth_first takes a node. It sets items equal to an empty list, so the items to be returned. And then if we have a valid node, we set items = self.breadth_first(node.left). It goes to the leftmost, and we'll work our way across to the rightmost.

We take our left, then items.append(node.value), and then items = items + self.breadth_first(node.right). We go from leftmost and then we queue up all of the rightmost. We're going across the graph. And we’re doing it this way so that we move across the graph, and this will pick up the nodes in sorted order. Now there are a couple of different ways we can do breadth_first order. We can do it level by level going from left to right. Or we can also do it in a traversal that's picking up all of the nodes from the leftmost, which would be at the lowest level to the rightmost. And that's what I'm doing here. And then in the end, it returns items.

# Implement a method to traverse the tree in breadth-first order
  def breadth_first(self, node):
    items = []
    if node:
      items = self.breadth_first(node.left)
      items.append(node.value)
      items = items + self.breadth_first(node.right)
    return items
Task 5 - Create an instance of the tree and insert data
The next step is to create an instance of the tree and insert the data. Create a node = Node with value 10. We have a single node, we think of this as the root node, the first node we add. Then I called node.insert with the value 5, node.insert with 25, 12, 33, and 18. Insert these six values.
# Create an instance of the tree and insert data
node = Node(10)
node.insert(5)
node.insert(25)
node.insert(12)
node.insert(33)
node.insert(18)
Task 6 - Display the data points in their traversal orders
Then the final step is to display the data points in their traversal orders. print(depth first order: followed by the result of the node.depth_traversal starting at the root node. And then breadth first order where we call node.breadth_first and we insert that into the string.
# Display the data points in their traversal orders
print('Depth first order: {}'.format(node.depth_traversal(node)))
print('Breadth first order: {}'.format(node.breadth_first(node)))
Terminal
Now if I run the program, We get the results printed in the debug console. So depth first order gives us 10, 5, 25, 12, 18, and 33. And breadth first order going from leftmost to rightmost, we get 5, 10, 12, 18, 25, and 33, giving us the results in sorted order. And that concludes this exercise.
terminal_app_08.png

Check your work
Check each box to confirm completion of the task.

Create a class to implement a binary search tree
Implement an insertion method
Implement a method to traverse the tree in depth-first order
Implement a method to traverse the tree in breadth-first order
Create an instance of the tree and insert data
Display the data points in their traversal orders
Question 1
Which of the following would complete the code to traverse a Binary Search Tree in depth-first order?


def depth_traversal(self, node):
    items = []
    if node:
      items.append(node.value)
      MISSING CODE
     MISSING CODE
    return items

OPTIONS:
A.


items = items + self.depth_traversal(node.right)
items = items + self.depth_traversal(node.left)

B.


items = items + self.depth_traversal(node.left)
items = items + self.depth_traversal(node.right)

C.


items = items + self.depth_traversal(node.top)
items = items + self.depth_traversal(node.bottom)

D.


items = items + self.depth_traversal(node.start)
items = items + self.depth_traversal(node.end)
Option A
Option B
Option C
Option D
Question 2
You create an instance of the Binary Search Tree and insert the following data. What would be the result of traversing the tree in depth-first order?


node = Node(10)
node.insert(5)
node.insert(25)
node.insert(12)
node.insert(33)
node.insert(18)
[10, 5, 25, 12, 33, 18]
[10, 5, 25, 12, 18, 33]
[5, 10, 12, 18, 25, 33]
[5, 10, 12, 18, 33, 25]
Congratulations! You have completed the lab.

