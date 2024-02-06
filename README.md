Ques1..Explanation=>
calculate_area(length, width): This function takes two parameters, length and width, and calculates the area of the rectangle. If the length is equal to the width,
it returns a string indicating that it's a square; otherwise, it returns the product of length and width.

main(): This function is the entry point of the program. It prompts the user to input the length and width of the rectangle, 
then calls the calculate_area() function to compute the area. It handles any potential ValueError that might occur if the user enters non-numeric input for length or width.

The try-except block in main() is used to handle potential errors that might occur during user input. If the user enters non-numeric values for length or width,
a ValueError will be raised, and the program will print a message asking the user to enter valid numerical values.

The if __name__ == "__main__": block ensures that main() will only be executed if the script is run directly, rather than being imported as a module into another script.

Ques2..Explanation=>

Importing Libraries: The script imports the mysql.connector module for interacting with MySQL databases.

Connection Function: create_connection() establishes a connection to the MySQL database.
It specifies the host, username, password, port, and database name. If the connection is successful, it returns the connection object; otherwise,
it prints the error and returns None.

Table Creation Function: create_table(connection) creates the "students" table if it does not already exist. 
It includes columns for student_id, first_name, last_name, age, and grade.

CRUD Operations:

insert_student(connection, first_name, last_name, age, grade): Inserts a new student record into the table.
update_grade(connection, first_name, new_grade): Updates the grade of a student identified by their first name.
delete_student(connection, last_name): Deletes a student record based on the last name.
fetch_and_display_students(connection): Fetches and displays all student records from the table.
Main Function (main()):

Establishes a connection to the database.
Enters a loop to continuously prompt the user for choices.
Based on the user's choice, it calls the corresponding CRUD operation function.
Asks the user if they want to continue or exit the program.
Sample Data and Function Calls: There's commented-out code at the end of the script that demonstrates how to create the table, 
insert sample data, update a record, delete a record, and fetch all records. However, this part is currently commented out,
and the CRUD operations are performed based on user input in the main() function.


Ques3..Explanation=>

generate_fibonacci(n) Function:

This function takes an integer n as input, representing the number of terms in the Fibonacci sequence to generate.
It initializes fibonacci_series as a list with the first two Fibonacci numbers: [0, 1].
Using a while loop, it calculates the next Fibonacci number by adding the last two numbers in fibonacci_series and appends it to the list.
The loop continues until the length of fibonacci_series reaches n.
Finally, it returns the first n Fibonacci numbers in the sequence.
main() Function:

This function serves as the entry point of the script.
It prompts the user to input the number of terms (n) they want in the Fibonacci sequence.
It checks if the input is a positive integer. If not, it prompts the user to enter a valid integer.
If the input is valid, it calls the generate_fibonacci() function with n and prints the resulting Fibonacci sequence.
Exception Handling:

The script handles the case where the user enters a non-integer value for n by catching a ValueError and printing an appropriate error message.
__name__ == "__main__" Check:

This condition ensures that the main() function is only executed if the script is run directly (not imported as a module into another script).
