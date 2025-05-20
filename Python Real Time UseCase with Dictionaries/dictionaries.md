# Dictionaries

Most used data types in Devops Engineers as a Devops engineer you want to write Python scripts to interact with Jira Github or AWS most of the times these tools return information back to you is mostly JSON format what you do you convert this JSON into dictonaries in python and performs operations on the data
properties of element dictionaries keep, entire characteristic of element for example EC2 :(name, id, subnets,IPs), you are going to store bunch of properties for each every instance.key/value pair to store properties. 

## Overview:
A dictionary in Python is a data structure that allows you to store and retrieve values using keys. It is also known as a hashmap or associative array in other programming languages. Dictionaries are implemented as hash tables, providing fast access to values based on their keys.

## Creating a Dictionary:
```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

## Accessing Values:
```python
print(my_dict['name'])  # Output: John
```

## Modifying and Adding Elements:
```python
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
```

## Removing Elements:
```python
del my_dict['city']  # Removing a key-value pair
```

## Checking Key Existence:
```python
if 'age' in my_dict:
    print('Age is present in the dictionary')
```

## Iterating Through Keys and Values:
```python
for key, value in my_dict.items():
    print(key, value)
```