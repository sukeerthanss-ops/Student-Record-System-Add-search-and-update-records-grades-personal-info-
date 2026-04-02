import json
import os

FILE_NAME = "students.txt"

# ---------------- FILE HANDLING ---------------- 
def load_data(): 
    if not os.path.exists(FILE_NAME):
        return []
    try: 
        with open(FILE_NAME, "r") as file: 
            return json.load(file) 
    except (json.JSONDecodeError, FileNotFoundError): 
        return [] 

def save_data(data): 
    with open(FILE_NAME, "w") as file: 
        json.dump(data, file, indent=4) 

# ---------------- STAFF FUNCTIONS ---------------- 
def add_student(data): 
    roll = input("Enter Roll Number: ")
    # Check if Roll Number already exists
    for s in data:
        if s["roll"] == roll:
            print("Error: Roll Number already exists!")
            return
            
    name = input("Enter Name: ") 
    age = input("Enter Age: ") 
    grade = input("Enter Grade: ") 
    
    student = {"roll": roll, "name": name, "age": age, "grade": grade} 
    data.append(student) 
    save_data(data) 
    print("Student added successfully!") 

def display_students(data): 
    if not data: 
        print("No records found.") 
        return 
    print("\n--- ALL STUDENT RECORDS ---")
    for student in data: 
        print(f"Roll: {student['roll']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}") 

def search_student(data): 
    roll = input("Enter Roll Number to search: ") 
    for student in data: 
        if student["roll"] == roll: 
            print(" Student Found:", student) 
            return 
    print("Student not found.") 

def update_student(data): 
    roll = input("Enter Roll Number to update: ") 
    for student in data: 
        if student["roll"] == roll: 
            print(f"Updating record for {student['name']}...")
            student["name"] = input("Enter new name: ") 
            student["age"] = input("Enter new age: ") 
            student["grade"] = input("Enter new grade: ") 
            save_data(data) 
            print("Record updated successfully!") 
            return 
    print("Student not found.") 

# ---------------- STUDENT FUNCTION ---------------- 
def student_view(data): 
    roll = input("Enter your Roll Number: ") 
    for student in data: 
        if student["roll"] == roll: 
            print("\n--- YOUR DETAILS ---")
            print(f"Name: {student['name']}\nAge: {student['age']}\nGrade: {student['grade']}") 
            return 
    print(" Record not found.") 

# ---------------- STAFF MENU ---------------- 
def staff_menu(data): 
    while True: 
        print("\n--- STAFF MENU ---") 
        print("1. Add Student") 
        print("2. Display Students") 
        print("3. Search Student") 
        print("4. Update Student") 
        print("5. Logout") 
        choice = input("Enter choice: ") 
        
        if choice == "1": 
            add_student(data) 
        elif choice == "2": 
            display_students(data) 
        elif choice == "3": 
            search_student(data) 
        elif choice == "4": 
            update_student(data) 
        elif choice == "5": 
            print("Logging out of Staff Portal...")
            break 
        else: 
            print("Invalid choice!") 

# ---------------- MAIN MENU ---------------- 
def main(): 
    data = load_data() 
    while True: 
        print("\n=== STUDENT MANAGEMENT LOGIN SYSTEM ===") 
        print("1. Staff Login") 
        print("2. Student Login") 
        print("3. Exit") 
        choice = input("Enter choice: ") 
        
        if choice == "1": 
            username = input("Enter username: ") 
            password = input("Enter password: ") 
            if username == "admin" and password == "1234": 
                print(" Staff Login Successful!") 
                staff_menu(data) 
            else: 
                print(" Invalid login credentials!") 
        elif choice == "2": 
            student_view(data) 
        elif choice == "3": 
            print("Exiting program... Goodbye!") 
            break 
        else: 
            print("Invalid choice!") 

if __name__ == "__main__": 
    main()
