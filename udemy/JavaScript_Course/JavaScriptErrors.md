What happens to the code:
Parser:
    Abstract Syntax Tree:
        Conversion to Machine Code:
            Machine Code:
                Code Runs

Global execution context is associated with the global object, which in the of the browser is the window object. Everything declared to the global context it get attached to the window object in the browser. 
Example: lastName === window.lastName // true
Global execution context id for code that is not inside af nay function.
Function declaration is also in a global context
Execution context is when you called a function. 

