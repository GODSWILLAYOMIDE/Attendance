import datetime

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.attendance_record = {}

    def mark_present(self, date):
        self.attendance_record[date] = True

    def calculate_attendance_percentage(self):
        total_classes = len(self.attendance_record)
        attended_classes = sum(1 for attended in self.attendance_record.values() if attended)
        percentage = (attended_classes / total_classes) * 100
        return percentage

class AttendanceManagementSystem:
    def __init__(self, filename):
        self.students = {}
        self.filename = filename

    def add_student(self, name, roll_number):
        self.students[name] = Student(name, roll_number)

    def search_student(self, name):
        if name in self.students:
            return True
        else:
            return False

    def mark_present(self, name, date):
        if self.search_student(name):
            self.students[name].mark_present(date)
        else:
            print("Student not found. Please add the student first.")

    def store_attendance_record(self):
        with open(self.filename, 'w') as file:
            for student in self.students.values():
                file.write(f"Name: {student.name}, Roll Number: {student.roll_number}, Attendance Record: {student.attendance_record}\n")

    def generate_report(self, date):
        print(f"\nAttendance Report for {date}:")
        for student in self.students.values():
            attended = student.attendance_record.get(date, False)
            attended = "PRESENT" if attended else "ABSENT"
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Avialability: {attended}","\n")

    def calculate_attendance_percentage(self, name):
        if self.search_student(name):
            percentage = self.students[name].calculate_attendance_percentage()
            print(f"Attendance Percentage for {name}: {percentage}%")
        else:
            print("Student not found. Please add the student first.")

def main():
    AMS = AttendanceManagementSystem("attendance_record.txt")

    while True:
        print("1. Add Student")
        print("2. Mark Present")
        print("3. Generate Report")
        print("4. Calculate Attendance Percentage")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll_number = int(input("Enter roll number: "))
            AMS.add_student(name, roll_number)
        elif choice == "2":
            name = input("Enter student name: ")
            date = datetime.date.today()
            AMS.mark_present(name, date)
        elif choice == "3":
            date = datetime.date.today()
            AMS.generate_report(date)
        elif choice == "4":
            name = input("Enter student name: ")
            AMS.calculate_attendance_percentage(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()