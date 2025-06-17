---
date: 1970-01-01T00:00:00Z
---

# Python Journeyman

Python Journeyman

## Getting Started

In this lab, you will be presented with a series of exercises. Each exercise will introduce a task or series of tasks to perform, followed immediately by a step-by-step instruction set detailing how to complete the tasks. Each exercise includes a question to test your understanding of the technology and tasks presented in the exercise.

The exercises presented in this lab include:
- **Exercise 1**: Testing in pytest
- **Exercise 2**: Making HTTP Requests
- **Exercise 3**: Web Services with Flask
- **Exercise 4**: Template Rendering with Jinja
- **Exercise 5**: Implement Multithreading
- **Exercise 6**: Multiprocessing with Python
- **Exercise 7**: Queue Processing
- **Exercise 8**: Asyncio

The **Lab Configuration** section details the devices, operating systems, tools, and software available in the lab. There is no need to download or configure anything unless specified as part of an exercise.

When you’re ready to begin, move to the next page using the navigation button below.

---

### Lab Configuration

**Devices**:
- Ubuntu Desktop

**Software**:
- Visual Studio Code
- PyCharm
- Flask
- pytest
- Asyncio

**Assets**:
- The assets are located in the 'ASSETS' folder on the desktop.

## Exercise 1 - Testing in pytest

### Introduction

Welcome to the **Testing with pytest** Python Lab. In this exercise, your task is to use Python to run unit tests using the pytest framework.

---

### Tasks

1. **Use Python to run unit tests using the pytest framework**.
2. **Use the `test_sorts.py` file** to complete this task.
3. **Create a simple function** to be tested.
4. **Create unit test functions** to test your function.
5. **Run pytest** to execute your tests.
6. **Make modifications** to induce a failure in your test.
7. **Rerun pytest** and make modifications to correct the failures.


### Task 1 - Create a Simple Function to Be Tested

Here is the function `simple_function` that you will create:

```python
def simple_function(a, b, c):
    if a is None:
        raise ValueError("'a' cannot be none.")
    if isinstance(a, str):
        return f'Hello, {a}!'
    if b < 0:
        return abs(b)
    if (c % 2) == 0:
        return 2
    return a + b + c
```

### Task 2 - Create Unit Test Functions to Test Your Function

Now, create the unit test functions to test the `simple_function`. There are four test cases, each designed to test a different path in the function:

```python
def test_a_none():
    try:
        simple_function(None, 1, 1)
    except ValueError:
        return True
    assert False

def test_b_neg():
    assert simple_function(0, -5, 0) == 5

def test_c_div_2():
    assert simple_function(0, 0, 4) == 2

def test_addition():
    assert simple_function(3, 5, 9) == 17
```

### Task 3 - Run Pytest

To run the tests, open the terminal and type the following command:

```bash
pytest
```

This will execute all the defined tests in the `test_sorts.py` file.

### Task 4 + 5 - Induce Failure and Fix It

To induce a failure in one of your tests, modify the `test_addition` function to intentionally introduce an incorrect value. For example:

```python
def test_addition():
    assert simple_function(3, 5, 9) == 21  # Modify this to cause a failure
```

This change will cause the test to fail because `simple_function(3, 5, 9)` will return `17`, not `21`.

Once you rerun the tests, you'll see that the test fails.

After that, fix the test by updating the assertion back to the correct value:

```python
def test_addition():
    assert simple_function(3, 5, 9) == 17  # Fix the test
```

### Check Your Work

- [ ] Create a simple function to be tested
- [ ] Create unit test functions to test your function
- [ ] Run pytest
- [ ] Make modifications to induce a failure in your test
- [ ] Rerun pytest and make modifications to correct the failures

Once you have completed the above tasks, select **Next** below to move to the next exercise.


## Exercise 2 - Making HTTP Requests

### Introduction

Welcome to the **Making HTTP Requests** Python Lab. In this exercise, your task is to use Python to make a URL request to a website or web API.

---

### Task

1. **Use Python to make a URL request** to a website or web API.
2. **Make a URL or API request** using an HTTP method.
3. **Handle request failures** with exception handling.
4. **Process or filter the response** as needed.
5. **Output the results** of your request.

---

You will use Python's `requests` library to perform these tasks, which is commonly used to make HTTP requests. Make sure to import the library and handle exceptions properly to ensure robust error handling.

### Task 1 - Make a URL or API Request Using an HTTP Method

We will start by making a request to the Environment Canada weather service for the city of Halifax, Nova Scotia. This will return the weather data in RSS format. Here’s how we initiate the URL request in Python:

```python
import requests
from xml.etree import ElementTree
import sys

# Make a URL or API request using an HTTP method
url = 'https://weather.gc.ca/rss/city/ns-19_e.xml'
```

### Task 2 - Handle Request Failures with Exception Handling

We need to handle possible request failures, such as network issues or an invalid response. We'll use a `try` block to capture any issues and raise an exception if the HTTP status code is not `200`, which indicates a successful request.

```python
# Handle request failures with exception handling
try:
    result = requests.get(url)
    if result.status_code != 200:
        raise ConnectionError('Status code: {}'.format(result.status_code))
```

### Task 3 - Process or Filter the Response

Next, we need to process the XML response. The RSS feed is in XML format, so we’ll use the `ElementTree` module to parse the response and extract the relevant data. In this case, we are looking for the "Current Conditions" title.

```python
# Process or filter the response
conditions_found = False  # Track if we find the current conditions
tree = ElementTree.fromstring(result.content)  # Parse the response content

# Loop over the elements in the XML tree and find the title containing "Current Conditions"
for node in tree.iter():
    if 'title' in node.tag:
        if 'Current Conditions' in node.text:
            print(node.text)  # Output the current conditions
            conditions_found = True
            break  # Exit loop after finding the current conditions
```

### Task 4 - Output the Results

If we find the "Current Conditions" in the XML response, we print it. If no conditions are found, we raise a `ValueError`. Additionally, if an exception occurs during the process, we catch it and print the exception information.

```python
# Output the results
if not conditions_found:
    raise ValueError('No weather conditions found.')

except:
    print(sys.exc_info())
```

### Full Code Example

Here is the complete code that handles the request, processes the response, and outputs the weather conditions:

```python
import requests
from xml.etree import ElementTree
import sys

# Make a URL or API request using an HTTP method
url = 'https://weather.gc.ca/rss/city/ns-19_e.xml'

try:
    result = requests.get(url)
    if result.status_code != 200:
        raise ConnectionError('Status code: {}'.format(result.status_code))

    # Process or filter the response
    conditions_found = False
    tree = ElementTree.fromstring(result.content)
    for node in tree.iter():
        if 'title' in node.tag:
            if 'Current Conditions' in node.text:
                print(node.text)  # Output the current conditions
                conditions_found = True
                break  # Exit loop once found

    if not conditions_found:
        raise ValueError('No weather conditions found.')

except:
    print(sys.exc_info())
```

### Output Example

When running the above code, if the "Current Conditions" are found, you should see an output similar to:

```
Current Conditions: Freezing Fog at -5.3 degrees C
```

### Check Your Work

- [ ] Make a URL or API request using an HTTP method
- [ ] Handle request failures with exception handling
- [ ] Process or filter the response
- [ ] Output the results

Once you have completed these tasks, select **Next** below to move to the next exercise.


## Exercise 3 - Web Services with Flask

**Introduction**  
Welcome to the Web Services with Flask Python Lab. Your assignment for this exercise is to use Python to serve HTTP requests with a Flask endpoint.  

**Task**  
- Use Python to serve HTTP requests with a Flask endpoint.  
- Use the `app.py` file to complete this task.  

**Output the Results**  
- Implement an endpoint for a GET request to serve a simple response.  
- Run the web service.  

**Note**  
To run your service, use the following command in your console/terminal window:  
`python3 -m flask run`  

**Test the Web Service**  
Test the web service response from a web browser.  


### Task 1 - Output the results

**We need Flask for this one.**  
So, on line 1, we have:  
`from flask import Flask, request`  

Now, the first step is to create a web service using Flask. The simple way of doing this is to set up an app:  
`app = Flask(__name__)`  
This creates an instance of a Flask web service when it’s run.

---

**Task 2 - Implement an endpoint for a GET request to serve a simple response**  
Next, we need to implement an endpoint for a GET request to serve a simple response.  
Start with the decorator `@app.route`. Give it the forward slash `/` as the route path. We can set the methods explicitly. By default, Flask handles GET requests, but we’ll explicitly state it like this:  
`methods=['GET']`  

Then, we define the function the decorator belongs to:  
```python
def index():
  name = request.args.get('name', type=str)
  if name is None:
    name = 'World'
  return f'Hello, {name}!'
```
Here, we are looking for a `name` argument in the URL query string. If it's not found, the default value is `'World'`. The function then returns a string: `Hello, {name}!`.

```python
# Implement an endpoint for a GET request to serve a simple response
@app.route('/', methods=['GET'])
def index():
  name = request.args.get('name', type=str)
  if name is None:
    name = 'World'
  return f'Hello, {name}!'
```

---

**Task 3 - Run the web service**  
To run the Flask web service, use the following command:  
`python3 -m flask run --host=0.0.0.0`  

This will start the service and listen on all available interfaces. If the file is named `app.py`, Flask will automatically look for this file to run the service. It will display something like:  
`Running on http://10.0.72.90:5000/`  

When you open the browser and go to `http://localhost:5000`, it will display `Hello, World!`. If you append `/?name=Steve` to the URL (like `http://localhost:5000/?name=Steve`), it will display `Hello, Steve!`.

---

**Task 4 - Test the web service response from a web browser**  
Once the service is running, you can test the response from your web browser.  

In the terminal window where Flask is running, you’ll see debug messages showing each request. For example, if the root `/` is accessed, the log will show a GET request to `/`, like:  
```
GET / HTTP/1.1
Status Code: 200
```
Similarly, for `/?name=Steve`, the log will show:  
```
GET /?name=Steve HTTP/1.1
Status Code: 200
```
Flask reads the `name` parameter from the URL query and uses it to format the string as `Hello, Steve!`.  

---

**Check Your Work**  
- Check each box to confirm completion of the task:  
  - Output the results  
  - Implement an endpoint for a GET request to serve a simple response  
  - Run the web service  
  - Test the web service response from a web browser  

Select **Next** below to move to the next exercise.

## Exercise 4 - Template Rendering with Jinga
**Introduction**  
Welcome to the Template Rendering with Jinja Python Lab. Your assignment for this exercise is to use Python to render a Jinja template.  

---

**Task**  
- Use Python to render a Jinja template.  
- To complete this exercise, you will need to use the files `iris-summary.json` and `hello.txt` located in your file tree.  

### Steps:
1. **Load a Template in Jinja2 Format**  
   You will need to load the Jinja2 template from the file (e.g., `hello.txt`).

2. **Load Data for the Template from a JSON File**  
   Use Python to read data from `iris-summary.json` (a JSON file). This data will be used to populate the template.

3. **Render the Template Using the Loaded Data**  
   Use Jinja2 to render the template by substituting placeholders with values from the JSON data.

4. **Output the Results of the Rendered Template**  
   Finally, output the results of the rendered template (i.e., display the formatted template with the data).


**Pre-Task**  
Before we carry out the actual steps in the exercise and explain the code, let’s first review the data we’ll be using to render the template. It's good to have a picture of the data before diving into the template and the code.  

In the `iris-summary.json` file, we have data regarding measurements of various species of iris, specifically **Iris virginica**, **Iris setosa**, and **Iris versicolor**. The file contains a list of species and their corresponding counts, which represent the number of measurements taken for each species (50 for each species). This data will be used to render into our template.

---

**Template Overview**  
The `hello.txt` file is a text file, but it contains Jinja2 template syntax. On line 1 of the template, there is a label for **flower observation counts** followed by a double brace tag: `{{ species }}`, which will display the list of species. The template then includes a loop to iterate through the species counts.

```plaintext
Flower observation counts:
{{ species }}:
{% for c in counts %}
  {{ c }}: {{ counts[c] }}
{% endfor %}
```

Here’s what happens:
- `{{ species }}` will render the species list.
- The `{% for c in counts %}` loop iterates through the species names, and `{{ c }}: {{ counts[c] }}` displays the species name followed by its count (50 for each species). The `-` after `{%-` trims any unnecessary whitespace.

---

**Task 1 - Load a template in the Jinja2 format**  
We start by importing the necessary modules and setting up the Jinja2 environment to load the template. The `FileSystemLoader` is used to load the template from the current directory.

```python
import json
from jinja2 import Environment, FileSystemLoader

# Load a template in the jinja2 format
env = Environment(
  loader=FileSystemLoader('.')
)

template = env.get_template('hello.txt')
```

This code initializes the Jinja2 environment and loads the `hello.txt` template.

---

**Task 2 - Load data for the template from a JSON file**  
Next, we load the data for the template from a JSON file (`iris-summary.json`). The `json.load()` function reads the file and converts the JSON data into a Python dictionary.

```python
# Load data for the template from a JSON file
data = None
with open('iris-summary.json') as f:
  data = json.load(f)
```

This code reads the `iris-summary.json` file and stores its contents in the `data` variable.

---

**Task 3 - Render the template using the loaded data**  
Before rendering the template, we check if the data has been successfully loaded. If the data is `None` (e.g., if the file doesn't exist or isn't properly formatted), we raise a `ValueError`. Once the data is loaded correctly, we render the template using `template.render(data)`.

```python
# Render the template using the loaded data
if not data:
  raise ValueError('Could not load json data.')

result = template.render(data)
```

---

**Task 4 - Output the results of the rendered template**  
Finally, we output the results of the rendered template by printing it to the terminal.

```python
# Output the results of the rendered template
print(result)
```

When the code is executed, the template will be rendered with the data from the JSON file, and the output will look like this:

```plaintext
Flower observation counts:
setosa: 50
versicolor: 50
virginica: 50
```

---

**Terminal Output**  
After running the code, the output will show the flower observation counts along with the species and their respective counts (50 for each species).  

---

**Check Your Work**  
Make sure to check each box to confirm completion of the following tasks:  
- Load a template in the Jinja2 format  
- Load data for the template from a JSON file  
- Render the template using the loaded data  
- Output the results of the rendered template  

Select **Next** below to move to the next exercise.

---

## Exercise 5 - Implement Multithreading

**Introduction**  
Welcome to the Multithreading Python lab. Your assignment for this exercise is to use Python to create a multithreaded program and to answer the assessment questions.

**Task**  
1. Use Python to create a multithreaded program.  
2. Create a class or function that implements a Python thread.  
   - Hint: Remember to import the appropriate modules.  
3. Create multiple threads.  
4. Start the threads.  
5. Add the threads to a thread list, if necessary.  
6. Synchronize the threads and wait for the threads to complete.  
7. Verify the results of the threads.


### Task 1 - Create a class or function that implements a Python thread

**Introduction**  
Start by importing the `threading` module, which is essential for creating threads in Python. Additionally, import the `time` module to use its `sleep` function, allowing us to add a delay to each thread for better observation of the process.

**Task 1: Create a Thread Class**  
The first step of the exercise is to create a class or function that implements the Python thread. Here, we create a class called `StringDeleter`, which will delete characters from a string one by one in a separate thread to demonstrate how threads work. The `StringDeleter` class will subclass `threading.Thread`.

We initialize the thread by calling `threading.Thread.__init__(self)` and set up two attributes: `self.thread_id` (to store the thread's unique identifier) and `self.data` (to store the string passed to the class).  

```python
import threading
import time

# Creating a class that implements a Python thread
class StringDeleter(threading.Thread):
    def __init__(self, thread_id, data):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.data = data
```

Next, we implement the `run` method, which is executed when the thread is started. This method will print the current thread's ID and the string being processed. The thread will then delete one character from the string at a time, pausing for one second between each deletion.

```python
    def run(self):
        print(f'Running: {self.thread_id}')
        while len(self.data) > 0:
            print('{}: {}'.format(self.thread_id, self.data))
            self.data = self.data[:-1]  # Remove the last character
            time.sleep(1.0)
```

**Task 2: Create Multiple Threads**  
To create multiple threads, initialize the necessary variables: a `thread_id` counter, a list of strings (`data`), and an empty list to store the threads.

```python
# Create multiple threads
thread_id = 1
data = ['Hi', 'Python', 'Concurrently']
threads = []
```

**Task 3 & 4: Start the Threads and Add Them to the List**  
For each string in the `data` list, create a new `StringDeleter` thread, start it, and append it to the `threads` list. We increment the `thread_id` after each thread is started.

```python
# Start the threads
# Add the threads to a thread list if necessary
for s in data:
    t = StringDeleter(thread_id, s)
    t.start()
    threads.append(t)
    thread_id += 1
```

**Task 5: Synchronize the Threads and Wait for Completion**  
To synchronize the threads, we need to wait for each thread to complete. This is done by calling `t.join()` for each thread in the `threads` list.

```python
# Synchronize the threads and wait for them to complete
for t in threads:
    t.join()
```

**Task 6: Verify the Results**  
Once all threads have completed, print a message indicating the end of the main thread.

```python
# Verify the results of the threads
print('End of Main.')
```

**Execution and Results**  
When the program is run, each thread will process a string, removing one character at a time. After each iteration, the thread pauses for one second to make it easier to observe. The debug console will show the following:

1. `Running 1` will be printed when thread 1 starts processing the string "Hi".
2. Thread 1 will print "Hi", "H" as it deletes each character.
3. Similarly, thread 2 will process the string "Python", and thread 3 will process "Concurrently".
4. After each thread finishes, the message "End of Main" will be displayed.

**Check Your Work**  
Confirm the completion of the following tasks by checking the corresponding boxes:

- Create a class or function that implements a Python thread.
- Create multiple threads.
- Start the threads.
- Add the threads to a thread list if necessary.
- Synchronize the threads and wait for the threads to complete.
- Verify the results of the threads.

---

### **Assessment Questions**

**Question 1**  
Which of the following would you use to synchronize the threads and wait for the threads to complete?  
- a) `t.wait()`  
- b) `t.pause()`  
- c) `t.synch()`  
- d) `t.join()`  

**Question 2**  
Which of the following methods would you use to pause the thread execution for a specific amount of time?  
- a) `wait`  
- b) `stop`  
- c) `sleep`  
- d) `pause`

---

Select **Next** to proceed to the next exercise.

## Exercise 6 - Multiprocessing with Python

**Introduction**  
Welcome to the Multiprocessing Python lab. In this exercise, your goal is to define, initialize, and execute a process in Python. You will also answer assessment questions related to the use of multiprocessing in Python.

**Task**  
1. Define, initialize, and execute a process in Python.  
2. Create Python functions to be used as multiprocessing targets.  
3. Construct data to be processed by the functions.  
4. Create and start the processes.  
5. Print the output of each process.  


**Instructions**

**Task 1 + 2**  
We'll begin by importing the necessary modules for this exercise. First, import `multiprocessing` and `Process` from it. Additionally, import `random` and `time`. Then, we'll initialize the random seed using `random.seed()`.

```python
import multiprocessing
from multiprocessing import Process
import random
import time

random.seed()
```

The first step is to create Python functions that will be used as multiprocessing targets. These functions will process data. Let's start with the `inc` (increment) function.

In the `inc` function:
- We first print the name of the current process using `multiprocessing.current_process().name` to identify which process is running.
- We initialize a `total` variable with 0.
- While `total` is less than 1000, we add a random number between 1 and 100 to it, sleep for 0.5 seconds, and print the current total.

```python
# Create Python functions to be used as multiprocessing targets
# Construct data to be processed by the functions
def inc():
    print(multiprocessing.current_process().name)
    total = 0
    while total < 1000:
        time.sleep(0.5)
        total += random.randrange(1, 100)
        print('inc: {}'.format(total))
```

Next, let's create the `dec` (decrement) function. This function will be similar to the `inc` function, but it will start at 1000 and subtract random values until it reaches 0.

```python
def dec():
    print(multiprocessing.current_process().name)
    total = 1000
    while total > 0:
        time.sleep(0.5)
        total -= random.randrange(1, 100)
        print('dec: {}'.format(total))
```

**Task 3 + 4**  
Now, we'll create and start the processes, and then print the output from each process.

Within the `if __name__ == '__main__':` block:
- We create two processes: `process_1` for the `inc` function and `process_2` for the `dec` function.
- Each process is started using the `start()` method.
- We then call `join()` on both processes to ensure that the main program waits for them to finish before continuing.
- After both processes have finished, we print "End of program" to signal the end of the execution.

```python
# Create and start the processes
# Print the output of each process
if __name__ == '__main__':
    process_1 = Process(name='Increment', target=inc)
    process_2 = Process(name='Decrement', target=dec)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    print('End of program')
```

**Execution and Results**  
When you run this code, you will see the output from each process while they are running. Each process will print its process name and the current total (incrementing or decrementing). Once both processes finish, "End of program" will be printed.

You should observe the following:
- The increment process will stop when it exceeds 1000.
- The decrement process will stop when it reaches 0.
- Finally, the program will print "End of program" once both processes are complete.

**Check Your Work**  
Confirm the completion of the following tasks by checking the corresponding boxes:

- Create Python functions to be used as multiprocessing targets.
- Construct data to be processed by the functions.
- Create and start the processes.
- Print the output of each process.

---

### **Assessment Questions**

**Question 1**  
Which of the following would you use to create a Python process assuming you have a Python function named `inc()` you wanted to run?  
- a) `process_1 = Process(name='Increment', target=inc)`  
- b) `process_1 = Process(name='Increment', function=inc)`  
- c) `process_1 = new Process(name='Increment', target=inc)`  
- d) `process_1 = Process(name='Increment', run=inc)`  

**Question 2**  
Which of the following are valid for threads and processes?  
- a) Threads share the same memory space  
- b) Processes run in their own unique memory space  
- c) Processes share the same memory space  
- d) Threads run in their own unique memory space  

---

Select **Next** to proceed to the next exercise.


## Exercise 7 - Queue Processing

### Introduction

Welcome to the Queue Processing Python lab. In this exercise, you will process data in a queue using a producer-consumer model in Python and answer the assessment questions.

---

### Task

Your task is to process data in a queue with a producer-consumer model in Python. The steps are as follows:

1. **Create Python functions** to act as the producer and consumer for the queue.
2. **Pop elements off the queue** in the consumer.
3. **Output the results** of the consumed data.
4. **Use a multithreaded priority queue** to manage the data.
5. **Push elements onto the queue** from the producer.

### Task 1 - Create Python functions to act as producer and consumer for a queue

### Imports and Setup

We start by importing the necessary modules:

```python
from multiprocessing import Queue, Process
import time
```

We define the maximum queue size and the number of elements we will be working with in this exercise:

```python
QUEUE_SIZE = 10
```

---

### Task 1: Create Producer and Consumer Functions

Next, we create Python functions to act as the producer and consumer for the queue. We'll begin by defining the **consumer function**:

```python
# Create Python functions to act as producer and consumer for a queue
def queueConsumer(mq):
    size = 0
    while size < QUEUE_SIZE:
        try:
            size += 1
            print('got: {}'.format(mq.get(timeout=3)))
        except:
            print('Timeout')
            break
```

---

### Task 2 & 3: Pop Elements Off the Queue and Output Results

In the consumer function, we pop elements off the queue and output the results. The `mq.get(timeout=3)` retrieves an element from the queue with a 3-second timeout. If the timeout is reached, it prints `'Timeout'` and exits the loop.

---

### Task 4: Use a Multithreaded Priority Queue

To use a multithreaded priority queue, we implement a multiprocessing queue. Here, we set up the queue and create a separate process for the consumer function:

```python
# Use a multithreaded priority queue
if __name__ == "__main__":
    print('start')

    # Set up the multiprocessing queue
    q = Queue(maxsize=QUEUE_SIZE)

    # Create and start the consumer process
    process = Process(target=queueConsumer, args=(q,))
    process.start()
```

---

### Task 5: Push Elements onto the Queue from the Producer

In the main thread, we act as the **producer**, pushing elements onto the queue. We use a `for` loop to put numbers from 1 to `QUEUE_SIZE` into the queue, printing each value as it's added:

```python
# Push elements onto the queue from the producer
    for m in range(1, QUEUE_SIZE):
        q.put(m)
        print(f'put {m}')
        time.sleep(0.5)

    # Wait for the consumer process to finish
    process.join()

    print('complete')
```

---

### Terminal Output

When running the program, the output will display each element being added to the queue (`put {m}`). The consumer will process each item and print `got: {item}`. If there are no more items to process within the timeout period, it will print `'Timeout'`. Finally, the program will print `'complete'` when the process finishes.

---

### Check Your Work

Confirm the completion of the tasks by checking the following:

- [ ] Create Python functions to act as producer and consumer for a queue
- [ ] Pop elements off the queue in the consumer
- [ ] Output the results
- [ ] Use a multithreaded priority queue
- [ ] Push elements onto the queue from the producer

---

### Questions

**Question 1:**  
In order to process data in a queue with a producer-consumer model in Python, what two classes will you need to import?

- **Queue**
- **Process**

**Question 2:**  
In your multiprocessing program, what method would you use to push elements onto the queue from the producer?

- **put**
- **Queue**
- **Processing**
- **QueueProcess**
  
Select Next below to move to the next exercise.


## Exercise 8 - Asyncio

### Introduction

Welcome to the **Using Asyncio Python Package** lab. In this exercise, you will create and execute a coroutine in a Python program using the Asyncio package. You will also answer assessment questions based on your implementation.

---

### Task

Your task is to create and execute a coroutine in a Python program using the Asyncio package. The steps are as follows:

1. **Create asynchronous functions** to run tasks.
2. **Create instances of the tasks**.
3. **Run the tasks concurrently**.
4. **Gather the results** as the tasks complete.
5. **Output the results**.

### Task 1 - Create asynchronous functions to run tasks

### Imports and Setup

We begin by importing the **asyncio** library, which allows us to create asynchronous functions:

```python
import asyncio
```

---

### Task 1: Create Asynchronous Functions to Run Tasks

Next, we create an **asynchronous function** called `summation`. This function takes a **process ID** (`pid`) and a list of **values** to sum. We use the `await` keyword with `asyncio.sleep(1)` to simulate a delay of 1 second during each iteration.

```python
# Create asynchronous functions to run tasks
async def summation(pid, values):
    total = 0
    for n in values:        
        await asyncio.sleep(1)  # Simulating a delay
        print('{}: {}'.format(pid, n))
        total += n
    return total
```

---

### Task 2: Create Instances of the Tasks

We now create the event loop using `asyncio.get_event_loop()`, and then define our tasks as instances of the `summation` function. These tasks are stored in a list:

```python
# Create instances of the tasks
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(summation(1, [5, 9, 23, 9919, 1, 44, 6])),
    loop.create_task(summation(2, [555, 333, 222, 81, 17, 982, 389]))
]
```

---

### Task 3 & 4: Run Tasks Concurrently and Gather Results

We run the tasks concurrently using `loop.run_until_complete()`, and use `asyncio.wait()` to wait until all tasks are completed. The results are stored in `results`. After the tasks are complete, we close the loop:

```python
# Run the tasks concurrently
# Gather the results as the tasks complete
results, _ = loop.run_until_complete(asyncio.wait(tasks))
loop.close()

total = 0
for r in results:
    total += r.result()  # Retrieve the result from the completed task
```

---

### Task 5: Output the Results

Finally, we output the total sum of all the values processed by both tasks:

```python
# Output the results
print('Total: {}'.format(total))
```

---

### Terminal Output

When running the program, the debug console will show each process adding a number to its total. After the tasks complete, the final total (12,586) is printed.

---

### Check Your Work

Confirm the completion of the tasks by checking each box:

- [ ] Create asynchronous functions to run tasks
- [ ] Create instances of the tasks
- [ ] Run the tasks concurrently
- [ ] Gather the results as the tasks complete
- [ ] Output the results

---

### Questions

**Question 1:**  
In order to use coroutines, we need to create an asyncio event loop. Which of the following would correctly do this?

- **loop = asyncio.get_event_loop()**

**Question 2:**  
What method would we use to schedule the execution of a coroutine?

- **create_task**