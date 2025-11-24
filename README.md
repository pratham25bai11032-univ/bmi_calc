#Python BMI Tracker calculates BMI, categorizes health, and saves history locally.
##Modular BMI tracker and History Log.

Overview of Project

The BMI python programme is a program designed to help users calculate their Body Mass Index(BMI) and maintain records of the readings of the user measurements . The system is built with in mind to keep the user interface , calculation logic, and record keeping logic in separate codes and to maintain good visibility and good software design. It is built on concepts such as function definition,conditional logic,datetime handling and file I/O.

Key features

the project core functionality is divided is into following areas:

Module 				Description 				Location

Calculation		takes weight and height,computes BMI 		calculatio_bmi function
			and determines the health category.	

history 		store the resulting data and measurements	view_history function


User interface		provides a simple menu for interaction,		main()function
			input prompt and display of result,
			history						



Non functional requirements


1. Usability: the system uses a straightforward , menu-driven interface with clear commands(1,2,3).
2. Relaibility: the view_history function uses try....except FileNotFoundError to prevent crashes when accessing the history for the first time.
3. Maintainability: while currently a single file , the function are distinct and logically seperable making future changes into modules easy
4. Data Integrity: Alll records are time stamped, ensuring that the chronological order of readings is preserved.


Technologies/Tools used 
*Language : Python 3.x
*Standard Library : datetime
*Storage : Local file I/O (bmi_history.txt)

Steps to Install and run the Project
1. Prerequisites: Ensure python is installed
2. Setup : Save the entire code into a single file name bmi_tracker.py
3. Execution : Open your Command/IDE/pythgon program runner and browse and opent the file and execute the following command
		python bmi_tracker.py
4. Use : Follow the BMI menu to interact and find the BMI.

Instruction for testing
*   **Test 1 (It Works):** Enter valid numbers (like Weight: 70 kg, Height: 175 cm). Confirm the BMI is accurate (22.86) and that the category shows Normal Weight.
    *   **Test 2 (Bad Input):** Enter letters instead of numbers for Weight or Height (like abc). It should display Error: Weight and Height must be valid numbers and return to the main menu without crashing.
2.  **Saving & Showing History**

    *   **Test 3 (Saving):** Calculate at least two BMIs. Then, select option 2 to view the history. Ensure both new entries appear with the correct timestamps.
    *   **Test 4 (No History):** If you delete or rename bmi_history.txt, option 2 should display No history found instead of returning an error.


