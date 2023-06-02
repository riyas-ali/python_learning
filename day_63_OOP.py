class Job:
    name = None
    salary = None
    hours_worked = None

    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_details(self):
        print("=== JOB ===")
        print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:>10}")


class Doctor(Job):
    experience = None
    speciality = None

    def __init__(self, salary, hours_worked, experience, speciality):
        self.name = "Doctor"
        self.salary = salary
        self.hours_worked = hours_worked
        self.experience = experience
        self.speciality = speciality

    def print_details(self):
        print("=== JOB ===")
        print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:^10} {self.experience:<10} {self.speciality:>21}")


class Teacher(Job):
    subject = None
    position = None

    def __init__(self, salary, hours_worked, subject, position):
        self.name = "Teacher"
        self.salary = salary
        self.hours_worked = hours_worked
        self.subject = subject
        self.position = position

    def print_details(self):
        print("=== JOB ===")
        print(f"{self.name:<10} {self.salary:^10} {self.hours_worked:^10} {self.subject:<10} {self.position:>21}")


lawyer = Job("Lawyer", "$100,000", "40")
lawyer.print_details()

doc = Doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print_details()

teacher = Teacher("$140,000", "8", "English", "Senior")
teacher.print_details()
