class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Add New Student ---")
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        student = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "course": course
        }
        self.students.append(student)
        print(f"✅ Student '{name}' successfully added!")

    def view_students(self):
        if not self.students:
            print("\n⚠️ No student records found.")
            return
        
        print("\n--- Student List ---")
        for s in self.students:
            print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")

    def search_student(self):
        roll_no = input("\nEnter Roll No to search: ")
        found = False
        for s in self.students:
            if s['roll_no'] == roll_no:
                print(f"\n🔍 Student Found:")
                print(f"Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
                found = True
                break
        if not found:
            print("❌ Student with this Roll No not found.")

    def delete_student(self):
        roll_no = input("\nEnter Roll No to delete: ")
        for s in self.students:
            if s['roll_no'] == roll_no:
                self.students.remove(s)
                print(f"🗑️ Student record deleted successfully!")
                return
        print("❌ Student not found.")

def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM  ")
        print("==============================")
        print("1. Add Student of kashmir university")
        print("2. View Students records")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            sms.search_student()
        elif choice == '4':
            sms.delete_student()
        elif choice == '5':
            print("\nExiting system. Thank you!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
