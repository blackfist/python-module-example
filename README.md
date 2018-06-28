# Example of modular python

When you write your code you want to keep your classes separate from your main function. Don't allow main (or any function) to know
too much about the workings of your other classes and functions.

In this example we create a module called `services` and there are code files for three hypothetical pasting services:
Pastebin, Pastie, and Kevpaste. In each of the code files we have defined a simple and consistent set of functions to 
interact with that service.

In main.py we import each of the services and create a list of the services. Then we simply use a for loop to call the
same set of functions for each of the services