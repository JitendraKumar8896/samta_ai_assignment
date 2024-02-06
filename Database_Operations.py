import mysql.connector


# Function to create a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3306",
            database="samta"
        )

        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table(connection):
    cursor = connection.cursor()
    table_creation_query = """
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age INT,
            grade FLOAT
        )
    """
    cursor.execute(table_creation_query)
    connection.commit()


# Function to insert a new student record
def insert_student(connection, first_name, last_name, age, grade):
    cursor = connection.cursor()
    insert_query = """
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """
    data = (first_name, last_name, age, grade)
    cursor.execute(insert_query, data)
    connection.commit()


# Function to update the grade of a student
def update_grade(connection, first_name, new_grade):
    cursor = connection.cursor()
    update_query = """
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """
    data = (new_grade, first_name)
    cursor.execute(update_query, data)
    connection.commit()


# Function to delete a student record
def delete_student(connection, last_name):
    cursor = connection.cursor()
    delete_query = "DELETE FROM students WHERE last_name = %s"
    #delete_query = "DELETE FROM students WHERE student_id = %s"
    data = (last_name,)
    cursor.execute(delete_query, data)
    connection.commit()


# Function to fetch and display all student records
def fetch_and_display_students(connection):
    cursor = connection.cursor()
    select_query = "SELECT * FROM students"
    cursor.execute(select_query)
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
    else:
        print("Student Records:")
        for student in students:
            print(student)


def main():
    connection = create_connection()
    print(connection)
    while True:
        print("1.Insert data\n2.update_grade\n3.delete_student\n4.display_students")
        choice=int(input("choose your choices:"))
        if choice==1:
            first_name=input("Enter first_name:")
            last_name=input("Enter last_name:")
            age=int(input("Enter age:"))
            grade=float(input("Enter grade:"))
            insert_student(connection, first_name, last_name, age, grade)
        elif choice==2:
            first_name = input("Enter first_name:")
            grade = float(input("Enter grade:"))

            update_grade(connection, first_name, grade)
        elif choice==3:
            last_name = input("Enter last_name:")
            #student_id = int(input("Enter student_id:"))
            delete_student(connection, last_name)
            # delete_student(connection, student_id)

        elif choice==4:
            fetch_and_display_students(connection)
        else:
            print("Invalid choice")
            connection.close()

        ans= input("Do you want to Continue?(y/n):")
        ans=ans.lower()
        if ans!='y':
            break



'''
    if connection:
        create_table(connection)

        # Insert a new student record
        
        insert_student(connection, "Alice", "Smith", 18, 95.5)
        insert_student(connection, "Jitendra", "Kumar", 23, 95.5)
        insert_student(connection, "Vishal", "Sharma", 24, 88.5)
        insert_student(connection, "Subhash", "Sahani", 25, 75.5)
        insert_student(connection, "Avaneesh", "Chauhan", 27, 79.5) 
        insert_student(connection, "Aman", "Kumar", 20, 95.5)

        # Update the grade of the student named "Alice"
        update_grade(connection, "Avaneesh", 97.0)

        #Delete the student with the last name "Smith"
        delete_student(connection, "Smith")
        #delete_student(connection, 2)

        # Fetch and display all student records
        fetch_and_display_students(connection)

        connection.close()'''


if __name__ == "__main__":
    main()
