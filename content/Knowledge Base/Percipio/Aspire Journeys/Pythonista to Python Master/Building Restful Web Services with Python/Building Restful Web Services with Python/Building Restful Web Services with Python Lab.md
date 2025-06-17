---
date: 1970-01-01T00:00:00Z
---

# Building Restful Web Services with Python

## Exercise 1 – Using Flask-RESTful Request Parser with Arguments
Here's a step-by-step guide on how to complete the tasks:

### Task 1 – Create a File in Jupyter Terminal using Python3
1. **Open Anaconda Terminal:**
   - Open a terminal and type `anaconda-navigator` to launch Anaconda Navigator.
   - Once the GUI opens, select **Jupyter Notebook** from the options.

2. **Navigate to `Lab01` Folder:**
   - In the Jupyter Notebook interface, navigate to the folder `Lab01`.
   - This should be your current working directory once you select it.

3. **Create a New Python File:**
   - In the Jupyter interface, click on **New** (top-right corner), and then select **Python 3** from the dropdown.
   - A new notebook will be created. 
   - Go to **File** > **Save As...**, enter the filename as `Installflask` and click **Save**.

### Task 2 – Install the Packages Flask and Flask-RESTful
1. Open the terminal in the Jupyter Notebook (or use the terminal in Anaconda Navigator).
2. Type the following command to install **Flask-RESTful**:
   ```bash
   pip install Flask-RESTful
   ```

### Task 3 – Import the Libraries Flask and Resource, Api
In your Jupyter Notebook (the `Installflask` file you created), type the following code to import the necessary libraries:

```python
from flask import Flask
from flask_restful import Resource, Api, reqparse
```

### Task 4 – Initialize the App and Load Student Details
Next, initialize the Flask app, set up the `Api` instance, and define the student details in the code cell:

```python
app = Flask(__name__)
api = Api(app)

# Student details stored in a dictionary
STUDETAILS = {
    '1': {'NAME': 'MARK', 'AGE': 21, 'SUBJECT': 'MATH', 'ADDRESS': 'US'},
    '2': {'NAME': 'ROCKY', 'AGE': 20, 'SUBJECT': 'COMPUTER', 'ADDRESS': 'US'},
    '3': {'NAME': 'STEPHEN', 'AGE': 22, 'SUBJECT': 'SCIENCE', 'ADDRESS': 'US'},
    '4': {'NAME': 'JOSEPH', 'AGE': 23, 'SUBJECT': 'IT', 'ADDRESS': 'US'},
    '5': {'NAME': 'PHILIP', 'AGE': 20, 'SUBJECT': 'PHYSICS', 'ADDRESS': 'US'}
}

# Request parser for input data
parser = reqparse.RequestParser()
```

### Task 5 – Create a Class Using GET and POST Methods
Create a class `Studlist` which will handle GET and POST requests to manage student details. Add the following code:

```python
class Studlist(Resource):
    # GET method to return student details
    def get(self):
        return STUDETAILS

    # POST method to add a new student
    def post(self):
        parser.add_argument("NAME")
        parser.add_argument("AGE")
        parser.add_argument("SUBJECT")
        parser.add_argument("ADDRESS")
        args = parser.parse_args()

        # Creating a new student ID and adding the new student to the details dictionary
        student_id = int(max(STUDETAILS.keys())) + 1
        student_id = '%i' % student_id
        STUDETAILS[student_id] = {
            "NAME": args["NAME"],
            "AGE": args["AGE"],
            "SUBJECT": args["SUBJECT"],
            "ADDRESS": args["ADDRESS"]
        }

        return STUDETAILS[student_id], 201
```

This class defines two methods:
- **GET**: Returns the list of student details.
- **POST**: Allows creating a new student record by adding arguments (name, age, subject, address).

### Task 6 – Run the Flask Application in the Terminal
Finally, add the following code to run the Flask application when the script is executed:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # or use app.run(debug=True) for local testing
```

This will run the Flask server on port 80 or 8080 depending on your setup. You can replace the host and port as needed.

### Execute the Program
- To execute the program, press **Shift + Enter** after entering all the code in the Jupyter notebook.
- The Flask app will start, and you'll be able to test the GET and POST requests through the browser or API testing tools like Postman.

### Conclusion
This sets up a basic Flask REST API that can manage student details. You can now send GET and POST requests to retrieve and add student data, respectively.
## Exercise 2 – Using Flask-RESTful Input Request With Arguments and Validation
### Task 1 – Create a File `webapp.py` to Build the App

1. **Create the `webapp.py` file:**
   - Open the `Lab02` folder in your preferred IDE (VS Code, Jupyter Notebook, or PyCharm).
   - Create a new file named `webapp.py` inside the `Lab02` folder.

2. **Import the Required Libraries:**
   - In the `webapp.py` file, add the following lines of code to import the necessary libraries:

   ```python
   from flask import Flask, render_template
   from flask_wtf import FlaskForm
   from wtforms import StringField, SubmitField
   from wtforms.validators import ValidationError, DataRequired, Length
   ```

3. **Initialize the Flask App:**
   - Next, initialize the app and set a secret key for CSRF protection:

   ```python
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'Thisissecretkey'
   ```

4. **Define the UserForm Class:**
   - Create the form class `UserForm` with a `StringField` for the username and validation for a minimum of 6 characters and a maximum of 42 characters:

   ```python
   class UserForm(FlaskForm):
       username = StringField(label=('Enter User name:'), validators=[DataRequired(), Length(min=6, max=42, message='Username length must be between %(min)d and %(max)d characters')])
   ```

5. **Create the Submit Button:**
   - Add a submit button to the form:

   ```python
       submit = SubmitField(label=('Submit'))
   ```

6. **Define the Route and Logic:**
   - Define a route (`/`) that handles both `GET` and `POST` methods, renders the form, and handles form submission:

   ```python
   @app.route('/', methods=('GET', 'POST'))
   def index():
       form = UserForm()
       if form.validate_on_submit():
           return f'''<h1> Welcome {form.username.data} </h1>'''
       return render_template('form1.html', form=form)
   ```

7. **Run the Flask Application:**
   - At the end of the `webapp.py` file, add the following to run the app:

   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

   The full `webapp.py` file should now look like this:

   ```python
   from flask import Flask, render_template
   from flask_wtf import FlaskForm
   from wtforms import StringField, SubmitField
   from wtforms.validators import ValidationError, DataRequired, Length

   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'Thisissecretkey'

   class UserForm(FlaskForm):
       username = StringField(label=('Enter User name:'), validators=[DataRequired(), Length(min=6, max=42, message='Username length must be between %(min)d and %(max)d characters')])
       submit = SubmitField(label=('Submit'))

   @app.route('/', methods=('GET', 'POST'))
   def index():
       form = UserForm()
       if form.validate_on_submit():
           return f'''<h1> Welcome {form.username.data} </h1>'''
       return render_template('form1.html', form=form)

   if __name__ == '__main__':
       app.run(debug=True)
   ```

### Task 2 – Create the Form Using an HTML File `form1.html`

1. **Create the HTML File:**
   - Inside the `Lab02` folder, create a new file named `form1.html`.

2. **Add the Form Code:**
   - Open the `form1.html` file and add the following HTML code:

   ```html
   <form method="POST" action="">
       <div class="form-row">
           <div class="form-group col-md-6">
               {{ form.csrf_token() }}
               <label for=""> {{ form.username.label }}</label>
               {{ form.username }}
               {% for field, errors in form.errors.items() %}
               <small class="form-text text-muted ">
                 {{ ', '.join(errors) }}
               </small>
               {% endfor %}
           </div>
           <div class="form-group">
               {{ form.submit(class="btn btn-primary")}}
           </div>
       </div>
   </form>
   ```

3. **Save the File:**
   - Press `Ctrl + S` to save the `form1.html` file.

### Task 3 – Run the Flask Application in the Terminal

1. **Set the `FLASK_APP` Environment Variable:**
   - In your terminal, navigate to the `Lab02` folder and set the `FLASK_APP` environment variable to point to the `webapp.py` file:
   
   On **macOS/Linux** or **Git Bash (Windows)**, use the following command:

   ```bash
   export FLASK_APP=webapp.py
   ```

   On **Windows Command Prompt**, use:

   ```cmd
   set FLASK_APP=webapp.py
   ```

2. **Set the Flask Environment to Development:**
   - Set the environment to `development` mode by running the following command:

   On **macOS/Linux** or **Git Bash (Windows)**, use:

   ```bash
   export FLASK_ENV=development
   ```

   On **Windows Command Prompt**, use:

   ```cmd
   set FLASK_ENV=development
   ```

3. **Run the Flask Application:**
   - Now, run the Flask application by typing the following command:

   ```bash
   flask run
   ```

   This will start the Flask app, and you can open it in a web browser at `http://127.0.0.1:5000/`.

### Testing the Application

1. Open the browser and go to `http://127.0.0.1:5000/`.
2. You should see the form asking for the username. Enter a username (with at least 6 characters and no more than 42).
3. Upon submitting the form, it should display a welcome message with the entered username.

### Conclusion
This process sets up a basic Flask app with a form using Flask-WTF for validation. The app handles `GET` and `POST` methods to render a form and process user input.
## Exercise 3 – Integrating Web Server With a Database

To run MySQL using Docker instead of installing it directly on Linux, you'll follow these steps. Docker allows you to create a containerized version of MySQL, which is easier to manage and deploy across environments. Below are the revised steps using Docker.

### Task 1 – Run MySQL Using Docker

1. **Install Docker** (if you haven't installed it already):
   - Follow the installation guide for Docker on [Docker's official website](https://docs.docker.com/get-docker/) based on your operating system.

2. **Navigate to the Lab03 Folder**:
   Open your terminal and change to the `Lab03` directory:
   ```bash
   cd Lab03
   ```

3. **Pull the MySQL Docker Image**:
   You need to pull the MySQL Docker image from Docker Hub. Run the following command:
   ```bash
   docker pull mysql:latest
   ```

4. **Run the MySQL Container**:
   To start a MySQL container, run the following command:
   ```bash
   docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=rootpassword -d mysql:latest
   ```

   - `--name mysql-container`: Names the container "mysql-container".
   - `-e MYSQL_ROOT_PASSWORD=rootpassword`: Sets the root password for MySQL to `rootpassword`.
   - `-d mysql:latest`: Runs MySQL in detached mode using the latest image.

5. **Check if the MySQL Container is Running**:
   You can verify the container is running with:
   ```bash
   docker ps
   ```

6. **Access MySQL Inside the Docker Container**:
   To access MySQL in the Docker container, run:
   ```bash
   docker exec -it mysql-container mysql -uroot -prootpassword
   ```

   This will log you into the MySQL shell inside the container with the `root` user and `rootpassword` as the password.

### Task 2 – Create the `EMPLOYEE` Database Using MySQL Commands

1. **Show Existing Databases**:
   Inside the MySQL shell, list all databases with:
   ```sql
   show databases;
   ```

2. **Create the `EMPLOYEE` Database**:
   Create the `EMPLOYEE` database:
   ```sql
   create database EMPLOYEE;
   ```

3. **Use the `EMPLOYEE` Database**:
   Switch to the `EMPLOYEE` database:
   ```sql
   use EMPLOYEE;
   ```

4. **Verify the Database**:
   List the databases again to ensure the `EMPLOYEE` database exists:
   ```sql
   show databases;
   ```

### Task 3 – Create a Login Form Using an HTML File `Login.html`

1. **Create the `Login.html` File**:
   Inside the `Lab03` folder, create a new file named `Login.html`.

2. **Set Up the Login Form**:
   Add the following HTML code for the login form:

   ```html
   {% block title %} Home {% endblock %}
   {% block body %}
   <div class="container">
       <h1>Home Page - Welcome to Skillsoft</h1>
       <h3>Python </h3> 
       <br><br><hr> 

       {% with messages = get_flashed_messages() %}
           {% if messages %}
               {% for message in messages %}
                   <div class="alert alert-success alert-dismissable" role="alert">
                       <button type="button" class="close" data-dismiss="alert" aria-label="close">
                           <span aria-hidden="true">X</span>
                       </button> 
                       {{ message }}
                   </div> 
               {% endfor %}
           {% endif %}
       {% endwith %}

       <h1>Please Login</h1> 
       <form action="" method="post" novalidate>
           {{ form.csrf_token }}
           <p>
               {{ form.Ename.label }}
               {{ form.Ename(size=32) }}  
               {% for error in form.Ename.errors %}
                   <span style="color:red;"> 
                   {{ error }}
                   </span>
               {% endfor %}
           </p>
           <p>
               {{ form.password.label }}
               {{ form.password(size=32) }}
               {% for error in form.password.errors %}
                   <span style="color:red;"> 
                   {{ error }}
                   </span>
               {% endfor %}
           </p>
           <p>
               <input type="submit" value="Login" class="btn btn-success"> 
           </p>
       </form>
   </div>
   {% endblock %}
   ```

3. **Save the File**:
   Press `Ctrl + S` to save the `Login.html` file.

### Task 4 – Create the Initial HTML File `index.html`

1. **Create the `index.html` File**:
   In the `Lab03` folder, create a new file named `index.html`.

2. **Set Up the Home Page**:
   Add the following code to `index.html`:

   ```html
   {% block title %} Home {% endblock %}
   {% block body %}
   <div class="container">
       <h1>Home Page - Welcome to Skillsoft</h1>
       <h3>Python </h3>
       <p>
           About Flask SQLAlchemy.
       </p>
   </div>
   {% endblock %}
   ```

3. **Save the File**:
   Press `Ctrl + S` to save the `index.html` file.

### Task 5 – Create a File `webdb.py` to Integrate the Login Form with the Database

1. **Create the `webdb.py` File**:
   In the `Lab03` folder, create a new file named `webdb.py`.

2. **Write the Program**:
   Add the following code to `webdb.py`:

   ```python
   from flask import Flask, request, flash, url_for, redirect, render_template
   from flask_sqlalchemy import SQLAlchemy
   from flask_wtf import FlaskForm
   from wtforms import StringField, SubmitField
   from wtforms.validators import ValidationError, DataRequired, Length

   app = Flask(__name__)

   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootpassword@localhost/EMPLOYEE'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   db = SQLAlchemy(app)

   class EmpDetails(db.Model):
       Eid = db.Column(db.Integer, primary_key=True)
       Ename = db.Column(db.String(100), unique=True)
       password = db.Column(db.String(100))

       def __init__(self, Ename, password):
           self.Ename = Ename
           self.password = password

   class LoginForm(FlaskForm):
       Ename = StringField('Username', validators=[DataRequired()])
       password = StringField('Password', validators=[DataRequired()])
       submit = SubmitField('Login')

   @app.route('/')
   def Index():
       return render_template('index.html')

   @app.route('/Login', methods=['GET', 'POST'])
   def Login():
       form = LoginForm()

       if form.validate_on_submit():
           employee = EmpDetails.query.filter_by(Ename=form.Ename.data).first()
           if employee and employee.password == form.password.data:
               return redirect(url_for('Index'))
           else:
               flash("Invalid, Please Try Again")

       return render_template('Login.html', form=form)

   if __name__ == "__main__":
       app.run(debug=True)
   ```

3. **Save the File**:
   Press `Ctrl + S` to save the `webdb.py` file.

### Task 6 – Run the `webdb.py` Flask Application in the Terminal

1. **Navigate to the Lab03 Folder**:
   Open a new terminal and navigate to the `Lab03` directory:
   ```bash
   cd Lab03
   ```

2. **Run the Flask Application**:
   Run the `webdb.py` file using Flask:
   ```bash
   python3 webdb.py
   ```

   This will start the Flask application. You can now visit the login page at `http://127.0.0.1:5000/Login` and use the form to log in. If the credentials match, you will be redirected to the home page.

### Conclusion

By following these steps, you have successfully:
- Installed MySQL using Docker.
- Created a database (`EMPLOYEE`).
- Developed a Flask web application that integrates with MySQL and allows users to log in using credentials stored in the database.

This Dockerized approach helps keep MySQL isolated, providing more flexibility and portability across different environments.
## Exercise 4 – Creating a Virtual Environment for Running Molten REST APIs

To complete the tasks of setting up a Molten API and deploying it using Gunicorn, follow these steps. I will guide you through each task.

---

### **Task 1 – Install Molten and Gunicorn**

1. **Navigate to Lab04 Folder**:
   Open your terminal and change to the `Lab04` directory:
   ```bash
   cd Lab04
   ```

2. **Install `virtualenv`**:
   First, install `virtualenv` to create a virtual environment:
   ```bash
   sudo apt install virtualenv
   ```

3. **Create a Virtual Environment**:
   Create a virtual environment named `penv`:
   ```bash
   virtualenv penv -p python3
   ```

4. **Activate the Virtual Environment**:
   Activate the virtual environment to isolate the project dependencies:
   ```bash
   source penv/bin/activate
   ```

   You should see the prompt change to indicate that you're working within the `penv` environment.

5. **Install Molten and Gunicorn**:
   Install `molten` and `gunicorn` in the virtual environment:
   ```bash
   pip install molten gunicorn
   ```

---

### **Task 2 – Create a Python Program to Set Up the API**

1. **Create `Moapp.py`**:
   In the `Lab04` folder, create a new file named `Moapp.py`.

2. **Import Required Libraries**:
   Open `Moapp.py` and add the following imports:
   ```python
   from typing import Optional, Tuple
   from molten import App, Route, HTTP_201, field, schema
   from molten.openapi import OpenAPIHandler, OpenAPIUIHandler, Metadata
   ```

   These imports allow us to define routes, work with schemas, and set up OpenAPI documentation for the API.

---

### **Task 3 – Define a Class with Schema and Set Up the Routes**

1. **Define the `STUD` Class**:
   Add the following code to define the `STUD` schema:
   ```python
   @schema
   class STUD:
       ID: Optional[int] = field(response_only=True)
       NAME: str
       AGE: int = field(minimum=0, maximum=100)
   ```

   - This class represents the schema for a student with `ID`, `NAME`, and `AGE`.
   - `response_only=True` means `ID` will only appear in the response and not in requests.
   - The `AGE` field is restricted between 0 and 100.

2. **Create the `create_stud` Function**:
   Define the function that handles `POST` requests to create a student:
   ```python
   def create_stud(stud: STUD) -> Tuple[str, STUD]:
       return HTTP_201, stud
   ```

   This function accepts a `STUD` object as input, returns a `201` HTTP status code, and the created `stud` object as a response.

3. **Set Up OpenAPI Handler**:
   Add the OpenAPI handler to generate API documentation:
   ```python
   get_schema = OpenAPIHandler(
       metadata=Metadata(
           title="Skillsoft",
           description="PYTHON",
           version="0.0.0",
       ),
   )

   get_docs = OpenAPIUIHandler()
   ```

   - `get_schema` generates the OpenAPI specification.
   - `get_docs` provides the interactive Swagger UI to view the API documentation.

4. **Define Routes**:
   Define the routes for the API:
   ```python
   app = App(
       routes=[
           Route("/studs", create_stud, method="POST"),
           Route("/_schema", get_schema),
           Route("/_docs", get_docs),
       ]
   )
   ```

   - `/studs`: Route for creating a new student via a `POST` request.
   - `/_schema`: Route to retrieve the OpenAPI schema.
   - `/_docs`: Route to access the Swagger UI documentation.

---

### **Task 4 – Run the Python App at the Prompt**

1. **Run the Python App**:
   To run the Python app, use the following command in the terminal:
   ```bash
   python3 Moapp.py
   ```

   The app will start a development server on `http://127.0.0.1:8000`.

---

### **Task 5 – Use Gunicorn to Deploy the App**

1. **Deploy the App with Gunicorn**:
   To run the app using Gunicorn (which is more suitable for production environments), use this command:
   ```bash
   gunicorn --reload Moapp:app
   ```

   - The `--reload` flag enables automatic reloading of the server when changes are made to the code.
   - This will run the app on `http://127.0.0.1:8000`.

---

### **Task 6 – Use `curl` to Retrieve the HTML Code of the Site**

1. **Retrieve the OpenAPI Schema with `curl`**:
   In a new terminal window (while the app is running), you can retrieve the schema from the server using `curl`:
   ```bash
   curl http://127.0.0.1:8000/_schema
   ```

   This will return the OpenAPI schema in JSON format, which describes the available API routes and models.

2. **Exit the Application**:
   Once you’re done testing, stop the Flask/Gunicorn server by pressing `Ctrl + C` in the terminal where the server is running.

3. **Deactivate the Virtual Environment**:
   To exit the virtual environment, type:
   ```bash
   deactivate
   ```

---

### **Summary**

By following these tasks, you have successfully:

1. Installed `molten` and `gunicorn` in a virtual environment.
2. Created a REST API using `molten` with a schema for `STUD`.
3. Set up routes to create a student and retrieve OpenAPI documentation.
4. Deployed the app using Gunicorn.
5. Used `curl` to interact with the API and retrieve the OpenAPI schema.

You can now extend this app by adding more routes, handling different HTTP methods (GET, PUT, DELETE), and building a fully functional API.

## Exercise 5 – Creating Views Using Django Templates

The steps you've outlined provide a detailed guide on how to set up a basic Django project and app, visualize the project structure, and implement a simple view rendering an HTML page. Here's a step-by-step summary of the tasks involved:

### **Task 1: Start a Project `EMPproject` in Django**
1. **Change to the Lab05 Directory:**
   Open your terminal and navigate to the `Lab05` directory:
   ```bash
   cd Lab05
   ```
   
2. **Check the Django Version:**
   To ensure Django is installed, check the version:
   ```bash
   python -m django --version
   ```

3. **Create the Django Project:**
   Start a new Django project named `EMPproject`:
   ```bash
   django-admin startproject EMPproject
   ```

4. **List the Project Files:**
   List the files in your current directory to confirm the creation of `EMPproject`:
   ```bash
   ls
   ```

5. **Navigate into the Project Directory:**
   Change the working directory into the newly created `EMPproject` folder:
   ```bash
   cd EMPproject
   ```

6. **List Files in the EMPproject Folder:**
   List the contents of the `EMPproject` directory:
   ```bash
   ls
   ```

7. **Install `tree` to Visualize the Directory Structure:**
   Install the `tree` command to visualize directory structures:
   ```bash
   apt install tree
   ```

8. **Display the Project Hierarchy:**
   Use the `tree` command to visualize the project hierarchy:
   ```bash
   tree
   ```

9. **Run the Development Server:**
   Start the Django development server to test the project:
   ```bash
   python3 manage.py runserver
   ```

10. **Stop the Server:**
    Press `Ctrl + C` to stop the server.

---

### **Task 2: Create an App in the EMPproject**
1. **Create the Django App:**
   Create a new app named `epapp` within your project:
   ```bash
   python3 manage.py startapp epapp
   ```

2. **Display the App's Hierarchy:**
   Use `tree` to see the directory structure of the `epapp` app:
   ```bash
   tree epapp/
   ```

---

### **Task 3: Add the App to `INSTALLED_APPS` in `settings.py`**
1. **Open `settings.py`:**
   Open the `settings.py` file found in the `EMPproject` folder.

2. **Add `epapp` to `INSTALLED_APPS`:**
   Add `'epapp'` to the `INSTALLED_APPS` list, which is typically located around line 40 in the `settings.py` file:
   ```python
   'epapp',
   ```

3. **Import `os` in `settings.py`:**
   Add `import os` at line #12 to use it later for setting the templates directory.

---

### **Task 4: Create a `templates` Directory in the `epapp` Folder**
1. **Create the `templates` Directory:**
   Create a new folder named `templates` inside the `epapp` directory.

---

### **Task 5: Create the `index.html` File**
1. **Create the `index.html` File:**
   Inside the `templates` directory, create a new file called `index.html`.

2. **Edit `index.html`:**
   Add the following content to `index.html`:
   ```html
   <!DOCTYPE html>  
   <html lang="en">  
   <head>  
       <meta charset="UTF-8">  
       <title>Index</title>  
   </head>  
   <body>  
   <h2>Welcome to Skillsoft!!</h2>  
   </body>  
   </html>  
   ```

---

### **Task 6: Set Up the Template Directory in `settings.py`**
1. **Add the Template Directory Path:**
   In `settings.py`, find the `DIRS` option under the `TEMPLATES` setting and add the path to the templates folder:
   ```python
   'DIRS': [os.path.join(BASE_DIR, 'templates')],
   ```

2. **Save the `settings.py` File**.

---

### **Task 7: Create a View in `views.py`**
1. **Open `views.py` in `epapp`:**
   Open the `views.py` file located in the `epapp` folder.

2. **Import Required Modules:**
   Add the following imports at the top of the file:
   ```python
   from django.template import loader
   from django.http import HttpResponse
   ```

3. **Create the View:**
   Define a function-based view that loads and renders the `index.html` template:
   ```python
   def index(request):
       template = loader.get_template('index.html')
       return HttpResponse(template.render())
   ```

4. **Save `views.py`**.

---

### **Task 8: Set Up URL Path in `urls.py`**
1. **Open `urls.py` in `EMPproject`:**
   Open the `urls.py` file in the `EMPproject` folder.

2. **Import the View:**
   Add the import for the `index` view at line #18:
   ```python
   from epapp import views
   ```

3. **Set Up the URL Path:**
   Add the URL pattern for the `index` view at line #21:
   ```python
   path('index/', views.index),
   ```

4. **Save `urls.py`**.

---

### **Task 9: Run the App**
1. **Run the Server Again:**
   Run the Django development server again to test the app:
   ```bash
   python3 manage.py runserver
   ```

2. **Navigate to `http://127.0.0.1:8000/` in a Web Browser:**
   Go to the URL `http://127.0.0.1:8000/` to view the page that says "Welcome to Skillsoft!!".

This is a complete guide on setting up your Django project and app, and creating a simple view to render an HTML page.

## Exercise 6 – Installing Django in a Virtual Python Environment

Below is a step-by-step guide to complete the tasks in your instructions. This will help you create a Django project and app, set up views, templates, and URLs, and run the app in the terminal.

### **Task 1 – Create a virtual Python environment and install Django**

1. **Install virtualenv (if not installed already)**:
   ```bash
   sudo apt install virtualenv
   ```

2. **Create a virtual environment `penv`**:
   ```bash
   virtualenv penv -p python3
   ```

3. **Activate the virtual environment**:
   ```bash
   source penv/bin/activate
   ```

4. **Install Django in the virtual environment**:
   ```bash
   pip install django
   ```

---

### **Task 2 – Start the Django project `Studproject` and visualize the hierarchy**

1. **Create a Django project**:
   ```bash
   django-admin startproject Studproject
   ```

2. **List the directory contents**:
   ```bash
   ls
   ```

3. **Change the working directory to `Studproject`**:
   ```bash
   cd Studproject
   ```

4. **List the files in the `Studproject` directory**:
   ```bash
   ls
   ```

5. **Install the `tree` command** to display directory structures:
   ```bash
   apt install tree
   ```

6. **Display the hierarchy of the project**:
   ```bash
   tree
   ```

7. **Run the Django server**:
   ```bash
   python3 manage.py runserver
   ```

---

### **Task 3 – Create an app in `Studproject`**

1. **Create the app `studentapp`**:
   ```bash
   python3 manage.py startapp studentapp
   ```

2. **Display the directory structure of `studentapp`**:
   ```bash
   tree studentapp/
   ```

---

### **Task 4 – In `settings.py`, add `studentapp` to `INSTALLED_APPS`**

1. **Open the `settings.py` file** inside the `Studproject` folder.

2. **Import `os` at line 12**:
   ```python
   import os
   ```

3. **Add `studentapp` to `INSTALLED_APPS`** (line 40):
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'studentapp',  # Add this line
   ]
   ```

---

### **Task 5 – Create a `templates` directory in `studentapp` folder**

1. **Create the `templates` directory inside the `studentapp` folder**:
   - In your file explorer, right-click `studentapp` and create a new folder named `templates`.

---

### **Task 6 – Create a file `index.html` in the `templates` folder**

1. **Create the `index.html` file inside the `templates` folder**:
   - Inside the `templates` folder, create a new file named `index.html`.

2. **Add the following content to `index.html`**:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Index</title>
   </head>
   <body>
       <h2>Welcome to PYTHON LAB</h2>
       <h3>Name is: {{ student }}</h3>
   </body>
   </html>
   ```

---

### **Task 7 – Set up the path to the `templates` folder in `settings.py`**

1. **In `settings.py`, add the path for the templates directory** at line 58:

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

---

### **Task 8 – Create a view in the `views.py` file in `studentapp`**

1. **Open the `views.py` file inside `studentapp`**.

2. **Import the required classes** at the top of the file:
   
   ```python
   from django.template import loader
   from django.http import HttpResponse
   ```

3. **Define the `index` view**:
   ```python
   def index(request):
       template = loader.get_template('index.html')  # Use lowercase 'index.html'
       name = {
           'student': 'JOHN',
       }
       return HttpResponse(template.render(name))
   ```

---

### **Task 9 – Import views and set the path in `urls.py`**

1. **Open `urls.py` inside the `Studproject` folder**.

2. **Import the views** at line 18:
   
   ```python
   from studentapp import views
   ```

3. **Add the path for the `index` view**:
   
   ```python
   from django.urls import path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index),  # Add this line
   ]
   ```

---

### **Task 10 – Run the app in the terminal**

1. **Run the server**:
   ```bash
   python3 manage.py runserver
   ```

2. **Visit the app** in the browser at `http://127.0.0.1:8000/` to see the page.

3. **Quit the server** by pressing `Ctrl+C`.

4. **Deactivate the virtual environment**:
   ```bash
   deactivate
   ```

---

By following these steps, you will successfully create a Django project, set up an app, create templates, configure URLs, and run your Django application.

## Exercise 7 – Creating a Django Model

To complete the tasks outlined for setting up a Django project and app, here's a detailed step-by-step guide:

### Task 1: Start the Django Project and Visualize the Hierarchy

1. **Change Directory to Lab07**:
    ```bash
    cd Lab07
    ```

2. **Start a Django Project named `Studproject`**:
    ```bash
    django-admin startproject Studproject
    ```

3. **List the Directory Contents**:
    ```bash
    ls
    ```

4. **Change into the `Studproject` Directory**:
    ```bash
    cd Studproject
    ```

5. **List the Files in `Studproject`**:
    ```bash
    ls
    ```

6. **Install `tree` to Visualize Directory Structure**:
    ```bash
    sudo apt install tree
    ```

7. **Visualize the Project Hierarchy**:
    ```bash
    tree
    ```

8. **Run the Development Server**:
    ```bash
    python3 manage.py runserver
    ```

9. **Stop the Server (Ctrl + C)**.

### Task 2: Create an App in `Studproject`

1. **Create the App `studentapp`**:
    ```bash
    python3 manage.py startapp studentapp
    ```

2. **List the Contents of the `studentapp` Folder**:
    ```bash
    tree studentapp/
    ```

### Task 3: Add `studentapp` to `INSTALLED_APPS` in `settings.py`

1. **Open `settings.py` in `Studproject` folder** and import `os` at the beginning:
    ```python
    import os
    ```

2. **Add `'studentapp'` to `INSTALLED_APPS`**:
    ```python
    INSTALLED_APPS = [
        # Other default apps
        'studentapp',
    ]
    ```

### Task 4: Create `templates` Directory in `studentapp`

1. **Create a Directory named `templates` in `studentapp`**:
    - Navigate to the `studentapp` folder.
    - Right-click and select "New Directory".
    - Name it `templates` and click "Create".

### Task 5: Create `index.html` in `templates` Folder

1. **Create the `index.html` file** inside the `templates` folder:
    - Navigate to the `templates` folder.
    - Right-click and select "New File".
    - Name it `index.html` and click "Create".

2. **Add the following code to `index.html`**:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Index</title>
    </head>
    <body>
        <h2>Welcome to PYTHON LAB</h2>
        <h3>Name is: {{ student }}</h3>
    </body>
    </html>
    ```

### Task 6: Set Path to `templates` Folder in `settings.py`

1. **In `settings.py`, set the path to the templates directory**:
    - Locate the `TEMPLATES` setting in `settings.py` and modify it as follows:
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            # other settings...
        },
    ]
    ```

### Task 7: Create a View in `views.py`

1. **In `studentapp/views.py`, import the necessary modules**:
    ```python
    from django.template import loader
    from django.http import HttpResponse
    ```

2. **Define the `index` view**:
    ```python
    def index(request):
        template = loader.get_template('index.html')  # Ensure this matches the template filename
        context = {'student': 'JOHN'}
        return HttpResponse(template.render(context))
    ```

### Task 8: Set the URL Path for `index` View in `urls.py`

1. **In the `Studproject/urls.py` file**, add an import for `views`:
    ```python
    from studentapp import views
    ```

2. **Add the URL path for the `index` view**:
    ```python
    urlpatterns = [
        path('index/', views.index),  # Mapping the URL to the view
        # other URLs...
    ]
    ```

3. **Save the file** by pressing `Ctrl + S`.

### Task 9: Create a Model in `models.py` in `studentapp`

1. **In `studentapp/models.py`, define a model for student details**:
    ```python
    from django.db import models

    class StudentDetails(models.Model):
        Sid = models.IntegerField()
        Sname = models.CharField(max_length=20)
        Sem = models.IntegerField()
        Emailid = models.EmailField(max_length=30)
        Contact_no = models.IntegerField()

        def __str__(self):
            return self.Emailid
    ```

### Task 10: Run the App in the Terminal

1. **Make Migrations for the Model**:
    ```bash
    python3 manage.py makemigrations
    ```

2. **Apply Migrations**:
    ```bash
    python3 manage.py migrate
    ```

3. **Run the Development Server**:
    ```bash
    python3 manage.py runserver
    ```

4. **Visit `http://127.0.0.1:8000/` in your browser** to see the index page.

5. **Stop the Server (Ctrl + C)**.

### Summary of Project Hierarchy

After completing all the tasks, your project hierarchy should look like this:

```
Lab07/
└── Studproject/
    ├── manage.py
    ├── Studproject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── studentapp/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        ├── views.py
        └── templates/
            └── index.html
```

This setup completes the task of creating and running a Django project and app, creating models, templates, and views, and configuring settings.

## Exercise 8 – Adding and Accessing SQL Data Using Django Model

Here's a step-by-step breakdown of the tasks you've outlined for setting up a Django project with a MySQL database:

---

### Task 1: Install MySQL on the server and create a database `college`
1. **Change to the directory `Lab08`:**
   ```bash
   cd Lab08
   ```
2. **Install MySQL server:**
   ```bash
   sudo apt install mysql-server
   ```
3. **Open MySQL terminal:**
   ```bash
   mysql
   ```
4. **Show the list of existing databases:**
   ```sql
   show databases;
   ```
5. **Create a new database called `college`:**
   ```sql
   create database college;
   ```
6. **Use the `college` database:**
   ```sql
   use college;
   ```

---

### Task 2: Install libmysqlclient, Django, and create a virtual Python environment
1. **Open another terminal window and navigate to `Lab08`:**
   ```bash
   cd Lab08
   ```
2. **Install the library `libmysqlclient-dev`:**
   ```bash
   sudo apt-get install libmysqlclient-dev
   ```
3. **Install `virtualenv`:**
   ```bash
   sudo apt install virtualenv
   ```
4. **Create a virtual environment called `penv`:**
   ```bash
   virtualenv penv -p python3
   ```
5. **Activate the virtual environment:**
   ```bash
   source penv/bin/activate
   ```
   The terminal prompt should show that the virtual environment `penv` is active.

---

### Task 3: Install `mysqlclient` and Django, and start the Django project `College`
1. **Install `mysqlclient` for MySQL support in Django:**
   ```bash
   pip install mysqlclient
   ```
2. **Install Django:**
   ```bash
   pip install django
   ```
3. **Start a new Django project named `College`:**
   ```bash
   django-admin startproject College
   ```
4. **Navigate to the `College` directory:**
   ```bash
   cd College
   ```

---

### Task 4: Create an app in `students`
1. **Create a new app called `students` within the Django project:**
   ```bash
   python3 manage.py startapp students
   ```

---

### Task 5: Create a model in the `models.py`
1. **Open the `models.py` file located in the `students` app.**
2. **Add the following code to define the `Student` model:**
   ```python
   from django.db import models

   class Student(models.Model):   
       Roll = models.CharField(max_length=100)
       sclass = models.CharField(max_length=100)
       fname = models.CharField(max_length=100)
       lname = models.CharField(max_length=100)

       class Meta:
           db_table = "student_details"
   ```

---

### Task 6: Create a directory `templates` in the `students` folder
1. **Create a `templates` directory within the `students` app:**
   - Right-click the `students` folder in your project structure.
   - Select **New Directory** and name it `templates`.

---

### Task 7: Modify `settings.py` to include `students`, set up the templates folder, and connect to MySQL
1. **Open the `settings.py` file.**
2. **Import `os` at line 12:**
   ```python
   import os
   ```
3. **Add `'students'` to the `INSTALLED_APPS` list at line 40:**
   ```python
   'students',
   ```
4. **Configure the path to the `templates` folder at line 58:**
   ```python
   'DIRS': [os.path.join(BASE_DIR, 'templates')],
   ```
5. **Update the MySQL database connection settings at lines 79-80:**
   ```python
   'ENGINE': 'django.db.backends.mysql',
   'NAME': 'college',
   'USER': 'root',
   'PASSWORD': '',
   'HOST': '',
   'PORT': '',
   ```

---

### Task 8: Create a `show.html` file in the `templates` folder
1. **Create a file named `show.html` inside the `templates` directory.**
2. **Enter the following code for the template:**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <title>Django CRUD Operations</title>
       <meta charset="utf-8">
       <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
       <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> 
   </head>
   <body>
   <div class="container">
   <table class="table table-striped">
       <thead>
         <tr>
           <th>Student ID</th>
           <th>Roll</th>
           <th>Class</th>
           <th>First Name</th>
           <th>Last Name</th>
           </tr>
       </thead>
       <tbody>
       {% for stud in student %}  
         <tr>
           <td>{{stud.id}}</td>
           <td>{{stud.Roll}}</td>
           <td>{{stud.sclass}}</td>
           <td>{{stud.fname}}</td>
           <td>{{stud.lname}}</td>
           </tr>
           {% endfor %} 
           </tbody>
   </table>
   </div>
   </body>
   </html>
   ```

---

### Task 9: Create a view in the `views.py` file within the `College` folder
1. **Open the `views.py` file in the `College` folder.**
2. **Add the following code to create the `show` view:**
   ```python
   from students.models import Student
   from django.shortcuts import render

   def show(request):
       student_details = Student.objects.all()
       return render(request, "show.html", {'student': student_details})
   ```

---

### Task 10: Update the `urls.py` file to include the `show` view
1. **Open the `urls.py` file in the `College` folder.**
2. **Add the import statement for views at line 18:**
   ```python
   from students import views
   ```
3. **Add the URL path for the `show` view at line 21:**
   ```python
   path('show', views.show),
   ```

---

### Task 11: Run the app in the terminal
1. **Create and apply the migration for the `Student` model:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
2. **Run the Django development server:**
   ```bash
   python3 manage.py runserver
   ```
3. **To check the schema of the `student_details` table, run:**
   ```sql
   describe student_details;
   ```

---

With these steps, you've set up a Django project with MySQL, created a `Student` model, and displayed student data on a webpage!

## 