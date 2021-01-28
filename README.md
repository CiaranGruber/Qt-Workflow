# Qt Workflow

This program is designed to improve the workflow when designing Qt applications relying primarily on the QUiLoader framework. It works by compiling the .qrc and the .ui files by running Qt for Python's built-in pyside6-rcc and pyside6-uic files. 

In order to work fully, the variable ENVIRONMENT_LOCATION must be set to either the absolute or relative path of the virtual environment before running.

To use the program, place setup.py in the base directory, modify ENVIRONMENT_LOCATION and it will go through all files in the current directory and any subdirectories and convert any available .ui or .qrc files and place them in the same location
