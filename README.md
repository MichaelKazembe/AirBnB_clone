# 0x00. AirBnB clone - The console

---

<img src="[/images/console.png](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230714%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230714T163831Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=97bdc5ea59445ceceaa313b5a2cac67f3775dafd86c200e3f067b561ace231fa)" border="0">
This project is the first step towards building a full web application: the **AirBnB clone**.

The console or command interpreter create the data model and allows create, update, destroy, store and persist objects to a file (JSON file). This console will be a tool to validate this storage engine.

## Table of Contents

---

* Objectives
* Requirements
* Installation and execution
* Console commands
* Tests
* Development environment
* Authors

## Objectives

---

* How to create a Python package
* How to create a command interpreter in Python using the `cmd module`
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a `Class`
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

## Requirements 

---

Airbnb was built and tested in **Ubuntu 14.04 LTS** via Vagrant in VirtualBox. Programming language python3

## Installation and execution 

---

* Clone the repository

> $ git clone https://github.com/ahmadoa/AirBnB_clone.git

* Move into the directory

> $ cd AirBnB_clone

* Execute the console file

> /AirBnB_clone$ ./console.py


## How to Use Command Interpreter

---

The commands available for this command interpreter are:

| Name      | Sample usage                               | Description                                 |
| --------- | ------------------------------------------ | ------------------------------------------- |
| `help`    | `help`                                     | Displays all commands available             |
| `create`  | `create <class>`                           | Creates new object (ex. a new User, Place)  |
| `update`  | `User.update('123', {'name' : 'Michael'})` | Updates attribute of an object              |
| `destroy` | `User.destroy('123')`                      | Destroys specified object                   |
| `show`    | `User.show('123')`                         | Retrieves an object from a file, a database |
| `all`     | `User.all()`                               | Displays all objects in Class               |
| `count`   | `User.count()`                             | Returns count of objects in specified Class |
| `EOF`     | `ctrl D`                                   | Exits the console.                          |
| `quit`    | `quit`                                     | Exits the Console                           |

***create, destroy and update commands save changes into a JSON file.***

## Tests ⚙️

---

Interactive Mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

Non-Interactive Mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```



### Development Environment

------

* Language: **Python3**

* Operating System: **Ubuntu 14.04 LTS**
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

### Authors✒️

---

* [Ahmad Ouladaouid](https://github.com/ahmadoa) Software Engineering student at [ALX Africa]([ALX Africa - Power Your Future in Tech](https://www.alxafrica.com/))
* [Michael Kazembe](https://github.com/MichaelKazembe) - Software Engineering student at [ALX Africa]([ALX Africa - Power Your Future in Tech](https://www.alxafrica.com/))
