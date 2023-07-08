#! /Users/adalatjurat/Desktop/Adalat.Jurat_T1A3/myenv/bin/python
import datetime
import pycountry
import csv


# all the inputs from student
class Student:
    def __init__(self, name, date_of_birth, country, language_level, primary_language):
        self.name = name
        self.date_of_birth = date_of_birth
        self.country = country
        self.language_level = language_level
        self.primary_language = primary_language

# all the inputs from the teacher
class Teacher:
    def __init__(self, name, primary_language, country, preferred_age_group, preferred_teaching_level):
        self.name = name
        self.primary_language = primary_language
        self.country = country
        self.preferred_age_group = preferred_age_group
        self.preferred_teaching_level = preferred_teaching_level

# validating student and teacher name make sure it includes alphabet only
def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False

   
# validating country 
def validate_country(country):
    try:
        pycountry.countries.search_fuzzy(country)
        return True
    except LookupError:
        return False
  
    

language_levels = [
    " No knowledge",
    " Basic understanding but unable to speak",
    " Basic daily communication",
    " Can read",
    " Can read and write"
]

def validate_primary_language(primary_language):
    try:
        pycountry.languages.lookup(primary_language)
        return True
    except LookupError:
        return False
    
def validate_age_group(age_group):
    try:
        age_range = age_group.split('-')
        if len(age_range) == 2:
            start_age = int(age_range[0].strip())
            end_age = int(age_range[1].strip())
            if start_age >= 5 and end_age <= 25 and start_age <= end_age:
                return True
    except ValueError:
        pass
    return False

    
def get_student_info():
    while True:
        name = input("Enter student name: ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please try again.")


    while True:
        date_of_birth = input("Enter student date of birth (dd/mm/yyyy): ")
        try:
            date_of_birth_datetime = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date of birth. Please enter a valid date in the format dd/mm/yyyy.")

    # Convert the input string to a datetime object
    date_of_birth_datetime = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
    # Calculate the age based on the current date
    current_date = datetime.datetime.now()
    age = current_date.year - date_of_birth_datetime.year - ((current_date.month, current_date.day) < (date_of_birth_datetime.month, date_of_birth_datetime.day))
    print("Age:", age)  # Display the age on the terminal

    country = input("Enter student country: ")
    while not validate_country(country):
        print("Invalid country. Please enter a valid country.")
        country = input("Enter student country: ")
    
    language_level = None
    while True:
        print("Choose the language level:")
        for i, level in enumerate(language_levels, start=1):
            print(f"{i}. {level}")

        language_level_input = input("Enter the number corresponding to the language level: ")
        if language_level_input.isdigit() and 1 <= int(language_level_input) <= len(language_levels):
            language_level = language_levels[int(language_level_input) - 1]
            break
        else:
            print("Invalid language level. Please enter a valid number.")


    while True:
        primary_language = input("Enter student primary language(s) (comma-separated): ")
        primary_languages = [lang.strip() for lang in primary_language.split(",")]
        if all(validate_primary_language(lang) for lang in primary_languages):
            break
        else:
            print("Invalid primary language. Please try again.")


    # Create a Student object with the collected information
    student = Student(name, date_of_birth, country, language_level, primary_language)

    # Save the student data to CSV file
    save_student_to_csv(student)

    return student

def save_student_to_csv(student):
    fieldnames = ['Name', 'Date of Birth', 'Country', 'Language Level', 'Primary Language']
    
    with open('students.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({
            'Name': student.name,
            'Date of Birth': student.date_of_birth,
            'Country': student.country,
            'Language Level': student.language_level,
            'Primary Language': student.primary_language
        })
        
    print("Student information collected and saved to student_data.csv")

def get_teacher_info():
    while True:
        name = input("Enter teacher name: ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please try again.")

    while True:
        primary_language = input("Enter teacher primary language(s) (comma-separated): ")
        primary_languages = [lang.strip() for lang in primary_language.split(",")]
        if all(validate_primary_language(lang) for lang in primary_languages):
            break
        else:
            print("Invalid primary language. Please try again.")


    country = input("Enter teacher country: ")
    while not validate_country(country):
        print("Invalid country. Please enter a valid country.")
        country = input("Enter teacher country: ")

     # Get the preferred age group
    preferred_age_group = input("Enter teacher preferred age group (age range 5-25 years): ")

    while not validate_age_group(preferred_age_group):
        print("Invalid age group. Please enter a valid range (age range 5-25 years).")
        preferred_age_group = input("Enter teacher preferred age group: ")
    
    # Get the preferred teaching levels
    preferred_teaching_levels = []
    print("Choose the preferred teaching level(s):")
    for i, level in enumerate(language_levels, start=1):
        print(f"{i}. {level}")
    
    teaching_level_input = input("Enter the number(s) corresponding to the preferred teaching level(s) (comma-separated): ")
    teaching_level_numbers = teaching_level_input.split(",")
    
    for number in teaching_level_numbers:
        if number.isdigit() and 1 <= int(number) <= len(language_levels):
            preferred_teaching_levels.append(language_levels[int(number) - 1])
    

    # Create a Teacher object with the collected information
    teacher = Teacher(name, primary_language, country, preferred_age_group, preferred_teaching_levels)

    # Save the teacher data to CSV file
    save_teacher_to_csv(teacher)

    return teacher


def save_teacher_to_csv(teacher):
    fieldnames = ['Name', 'Primary Language', 'Country', 'Preferred Age Group', 'Preferred Teaching Level']
    
    with open('teachers.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({
            'Name': teacher.name,
            'Primary Language': teacher.primary_language,
            'Country': teacher.country,
            'Preferred Age Group': teacher.preferred_age_group,
            'Preferred Teaching Level': teacher.preferred_teaching_level
        })
        
    print("Teacher information collected and saved to teacher_data.csv")


def main():
    print("Welcome to the Uyghur Language Class Scheduling System!")
    
    students = []  # List to store student information
    teachers = []  # List to store teacher information
    
    while True:
        print("Please select your role:")
        print("1. Student")
        print("2. Teacher")
        print("0. Exit")

        role = input("Enter your role (1, 2, or 0 to exit): ")
        if role == "0":
            print("Exiting the application...")
            break

        elif role == "1":
            student = get_student_info()
            students.append(student)
            # Process student information
            print("Student information collected:")
            print("Name:", student.name)
            print("Date of Birth:", student.date_of_birth)
            print("Country:", student.country)
            print("Language Level:", student.language_level)
            print("Primary Language:", student.primary_language)
        
        elif role == "2":
            teacher = get_teacher_info()
            teachers.append(teacher)
            # Process teacher information
            print("Teacher information collected:")
            print("Name:", teacher.name)
            print("primary_language:", teacher.primary_language)
            print("Country:", teacher.country)
            print("Preferred Age Group:", teacher.preferred_age_group)
            print("Preferred Level:", teacher.preferred_teaching_level)
        
        else:
            print("Invalid role selection.")


# Run the main function
if __name__ == "__main__":
    main()
