#! /Users/adalatjurat/Desktop/T1A3 - Terminal Application/myenv/bin/python
import datetime
import pycountry
from geopy.geocoders import Nominatim
#handiling network connectivity issues or the service being temporarily unavailable.
from geopy.exc import GeocoderTimedOut  


class Student:
    def __init__(self, name, date_of_birth, living_city, country, language_level, primary_language):
        self.name = name
        self.date_of_birth = date_of_birth
        self.living_city = living_city
        self.country = country
        self.language_level = language_level
        self.primary_language = primary_language

class Teacher:
    def __init__(self, name, primary_language, living_city, country, preferred_age_group, preferred_teaching_level):
        self.name = name
        self.primary_language = primary_language
        self.living_city = living_city
        self.country = country
        self.preferred_age_group = preferred_age_group
        self.preferred_teaching_level = preferred_teaching_level

def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False
    
def validate_city(city):
    geolocator = Nominatim(user_agent="your_app_name")
    try:
        location = geolocator.geocode(city)
        if location is not None:
            return True
        else:
            return False
    except GeocoderTimedOut:
        return False

def validate_country(country):
    try:
        pycountry.countries.lookup(country)
        return True
    except LookupError:
        return False

language_levels = [" No knowledge",
                   " Basic understanding but unable to speak",
                   " Basic daily communication",
                   " Can read",
                   " Can read and write"]

def validate_primary_language(primary_language):
    try:
        pycountry.languages.lookup(primary_language)
        return True
    except LookupError:
        return False
    
def validate_age_group(age_group):
    if age_group.isdigit():
        return True
    else:
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

    while True:
        living_city = input("Enter student living city: ")
        if validate_city(living_city):
            break
        else:
            print("Invalid city or unable to retrieve location. Please try again.")

    while True:
        country = input("Enter student country: ")
        if validate_country(country):
            break
        else:
            print("Invalid country. Please try again.")

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
    student = Student(name, date_of_birth, living_city, country, language_level, primary_language)

    return student

def get_teacher_info():
    while True:
        name = input("Enter teacher name: ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please try again.")

    while True:
        primary_language = input("Enter student primary language(s) (comma-separated): ")
        primary_languages = [lang.strip() for lang in primary_language.split(",")]
        if all(validate_primary_language(lang) for lang in primary_languages):
            break
        else:
            print("Invalid primary language. Please try again.")


    while True:
        living_city = input("Enter teacher living city: ")
        if validate_city(living_city):
            break
        else:
            print("Invalid city or unable to retrieve location. Please try again.")

    while True:
        country = input("Enter teacher country: ")
        if validate_country(country):
            break
        else:
            print("Invalid country. Please try again.")

    preferred_age_group = input("Enter teacher preferred age group: ")
    while not validate_age_group(preferred_age_group):
        print("Invalid age group. Please enter a numeric value.")
        preferred_age_group = input("Enter teacher preferred age group: ")


    preferred_teaching_level = None
    while True:
        print("Choose the preferred teaching level:")
        for i, level in enumerate(language_levels, start=1):
            print(f"{i}. {level}")

        teaching_level_input = input("Enter the number corresponding to the preferred teaching level: ")
        if teaching_level_input.isdigit() and 1 <= int(teaching_level_input) <= len(language_levels):
            preferred_teaching_level = language_levels[int(teaching_level_input) - 1]
            break
        else:
            print("Invalid teaching level. Please enter a valid number.")

    # Create a Teacher object with the collected information
    teacher = Teacher(name, primary_language, living_city, country, preferred_age_group, preferred_teaching_level)

    return teacher


def main():
    print("Welcome to the Uyghur Language Class Scheduling System!")
    
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
            # Process student information
            print("Student information collected:")
            print("Name:", student.name)
            print("Date of Birth:", student.date_of_birth)
            print("Living City:", student.living_city)
            print("Country:", student.country)
            print("Language Level:", student.language_level)
            print("Primary Language:", student.primary_language)
        
        elif role == "2":
            teacher = get_teacher_info()
            # Process teacher information
            print("Teacher information collected:")
            print("Name:", teacher.name)
            print("primary_language:", teacher.primary_language)
            print("Living City:", teacher.living_city)
            print("Country:", teacher.country)
            print("Preferred Age Group:", teacher.preferred_age_group)
            print("Preferred Level:", teacher.preferred_teaching_level)
        
        else:
            print("Invalid role selection.")


    

# Run the main function
if __name__ == "__main__":
    main()

