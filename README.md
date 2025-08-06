# TASK01-ELEVATE-LABS-INTERNSHIP

Calculator CLI app.

Overview:<br/>
This code implements a simple calculator app in Python that performs basic operations (addition, subtraction, multiplication, division) on user-provided multiple numbers. It uses functions for each operation and a Calculator() function to handle user interaction.

Function details:<br/>
1. Add(Entered_Numbers)<br/>
•	Purpose: Adds all numbers in Entered_Numbers.<br/>
•	Logic: Initializes Result to 0, then iterates through the list, summing the numbers.<br/>
•	Output: Prints the total sum.<br/>

2. Sub(Entered_Numbers)<br/>
•	Purpose: Subtracts all subsequent numbers from the first number.<br/>
•	Logic: Sets Result to the first number, then subtracts each of the remaining numbers in order.<br/>
•	Output: Prints the difference.<br/>

3. Mul(Entered_Numbers)<br/>
•	Purpose: Multiplies all numbers.<br/>
•	Logic: Starts with Result = 1, then multiplies by each number.<br/>
•	Output: Prints the product.<br/>

4. Div(Entered_Numbers)<br/>
•	Purpose: Divides the first number by each of the subsequent numbers sequentially.<br/>
•	Logic: Starts with the first number, then divides by each subsequent number inside a try block to catch division by zero errors.<br/>
•	Error Handling: If division by zero occurs, prints an error message and exits the function early.<br/>
•	Output: Prints the final division result.<br/>

Main function: Calculator()<br/>
•	Loop: Runs indefinitely until the user chooses to exit (choice == 5).<br/>

•	User Interaction:<br/>
  o	Displays a welcome message and options for operations plus exit.<br/>
  o	Asks the user for their choice, converting input to integer.<br/>
  o	Handles invalid input with try-except.<br/>
  
•	Action:<br/>
  o	If the user chooses 5, it exits the loop and ends the program.<br/>
  o	Otherwise, prompts the user to input multiple numbers separated by spaces.<br/>
  o	Converts the input into a list of floats (Entered_Numbers).<br/>
  o	Checks if at least two numbers are entered; if not, prompts again.<br/>
  o	Calls the appropriate function based on the choice.<br/>
  
•	Error Handling:<br/>
  o	If invalid choice or invalid number input, prompts again.<br/>

Summary:<br/>
•	The program offers a menu-driven calculator.<br/>
•	Uses functions for each operation for modularity.<br/>
•	Handles invalid inputs and division by zero gracefully.<br/>
•	Continuously runs until the user chooses to exit.<br/>


Programming language used: Python (Functions, Loops, List)<br/>
Tool: PyCharm
