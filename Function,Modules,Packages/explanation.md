# Python Functions, Modules and Packages

## 1. Differences Between Functions, Modules, and Packages

### Functions

A function in Python is a block of code that performs a specific task. Functions are defined using the `def` keyword and can take inputs, called arguments. They are a way to encapsulate and reuse code.

functioned your program for each functionality.

whenever you write the function for using it you have to call it. So you need to invoke

readility, reusabality, debugging .. 

funtions takes input and return outputs.

def addition(num1, num2);
   add = num1 + num2 
   return(add)

**Example:**

```python

def addition();
    num = 1 + 2
    print(num)


def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
addition()



```

In this example, `greet` is a function that takes a `name` argument and returns a greeting message.

### Modules

A module is a Python script containing Python code. It can define functions, classes, and variables that can be used in other Python scripts. Modules help organize and modularize your code, making it more maintainable.

you are writing peace of code and you are thinking this peace of code can be used project1 and project2 or project3 you can write just one python.py and you can use this .py at all the modules.

modules == groups of functions.

**Example:**

Suppose you have a Python file named `my_module.py`:

```python
# my_module.py
def square(x):
    return x ** 2

pi = 3.14159265
```

You can use this module in another script:

```python
import my_module

result = my_module.square(5)
print(result)
print(my_module.pi)
```

In this case, `my_module` is a Python module containing the `square` function and a variable `pi`.

### Packages

A package is a collection of modules organized in directories. Packages help you organize related modules into a hierarchy. They contain a special file named `__init__.py`, which indicates that the directory should be treated as a package.

collections of the modules

As a devops engineer we use lots of packages because of 
- you want to make API request to AWS, github,jira,

where are the modules for all of theese things just like when you are writing Dockerfile you are creating docker image can it use by the other people in your company, you will put this image to docker hub or any repository that people can reach ,Similarly 
in python when you wrote a Module for AWS the module as boto3 and writers know that module will go the popular you put your modules the PİP and PyPi 

You can use pip installing anything from PyPi
example : pip install boto3

**Example:**

Suppose you have a package structure as follows:

```
my_package/
    __init__.py
    module1.py
    module2.py
```

You can use modules from this package as follows:

```python
from my_package import module1

result = module1.function_from_module1()
```

In this example, `my_package` is a Python package containing modules `module1` and `module2`.

## 2. How to Import a Package

Importing a package or module in Python is done using the `import` statement. You can import the entire package, specific modules, or individual functions/variables from a module.

**Example:**

```python
# Import the entire module
import math

# Use functions/variables from the module
result = math.sqrt(16)
print(result)

# Import specific function/variable from a module
from math import pi
print(pi)
```

In this example, we import the `math` module and then use functions and variables from it. You can also import specific elements from modules using the `from module import element` syntax.

## 3. Python Workspaces

Python workspaces refer to the environment in which you develop and run your Python code. They include the Python interpreter, installed libraries, and the current working directory. Understanding workspaces is essential for managing dependencies and code organization.

Python workspaces can be local or virtual environments. A local environment is the system-wide Python installation, while a virtual environment is an isolated environment for a specific project. You can create virtual environments using tools like `virtualenv` or `venv`.

**Example:**

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (on Windows)
myenv\Scripts\activate

# Activate the virtual environment (on macOS/Linux)
source myenv/bin/activate
```

Once activated, you work in an isolated workspace with its Python interpreter and library dependencies.


Virtual Environment = this is only usefel if you are using same environment for different projects how it works it will d logical separation for the python packages 

pip install virtualenv
python -m venv project_abc
python -m venv project_xyz
source project_abc/bin/activate i went this folder

and 
ı said pip install something package will be installed this source at this project.