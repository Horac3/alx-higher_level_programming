# Python - Almost a circle
Background Context:
The project "Python - Almost a Circle" is part of the Higher-Level Curriculum and aims to prepare you for more advanced Python programming. It involves reviewing various topics in Python, including Object-Oriented Programming (OOP), classes, inheritance, unit testing, file handling, JSON serialization, and more.

Learning Objectives:
At the end of this project, you should be able to:

General:
- Understand Unit testing and how to implement it in a large project.
- Serialize and deserialize a Class using JSON.
- Write and read data to/from a JSON file.
- Use *args and **kwargs to handle variable-length arguments in functions.
- Handle named arguments in a function.


Project Requirements:
- Python scripts should be compatible with Python 3.8.5 on Ubuntu 20.04 LTS.
- Files should end with a newline character.
- The first line of all files should be `#!/usr/bin/python3`.
- A README.md file at the root of the project folder is mandatory.
- The code should follow the PEP 8 style guidelines.
- All modules, classes, and functions should be documented.

Tasks:
1. Create a Base class that manages the 'id' attribute for all other classes in the project.
2. Write a Rectangle class that inherits from the Base class, representing a rectangle.
3. Add validation for attributes (width, height, x, y) in the Rectangle class.
4. Implement a method to calculate the area of a rectangle.
5. Create a method to display a rectangle using the character '#'.
6. Override the __str__ method in the Rectangle class to provide a custom string representation.
7. Improve the display method to handle the 'x' and 'y' coordinates of a rectangle.
8. Add an update method to the Rectangle class to modify attributes based on arguments or keyword arguments.
9. Create a Square class that inherits from the Rectangle class, representing a square.
10. Add a 'size' attribute to the Square class and validate it using the same logic as the Rectangle class.
11. Implement the update method in the Square class to handle the 'size' attribute.
12. Create a method in the Rectangle class to convert an instance to a dictionary representation.
13. Implement a similar method in the Square class to convert an instance to a dictionary representation.
14. Add a method to the Base class that converts a list of dictionaries to a JSON string.
15. Implement a class method in the Base class to save a list of instances to a JSON file.
16. Create a method in the Base class to convert a JSON string to a list of dictionaries.
17. Implement a class method in the Base class to create an instance from a dictionary.
18. Add a class method in the Base class to load instances from a JSON file.

