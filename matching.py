import csv
import datetime
from main import Student, Teacher

def load_students_from_csv(filename):
    students = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['Name']
            date_of_birth = row['Date of Birth']
            country = row['Country']
            language_level = row['Language Level']
            primary_language = row['Primary Language']
            
            student = Student(name, date_of_birth, country, language_level, primary_language)
            students.append(student)
    
    return students

def load_teachers_from_csv(filename):
    teachers = []
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row['Name']
            primary_language = row['Primary Language']
            country = row['Country']
            preferred_age_group = row['Preferred Age Group']
            preferred_teaching_level = row['Preferred Teaching Level']
            
            teacher = Teacher(name, primary_language, country, preferred_age_group, preferred_teaching_level)
            teachers.append(teacher)
    
    return teachers


def match_students_with_teachers(students, teachers):
    matches = []  # List to store the matching pairs

    # Iterate through each student
    for student in students:
        best_match = None  # Variable to store the best matching teacher
        max_score = 0  # Variable to track the maximum score
        
        # Iterate through each teacher
        for teacher in teachers:
            # Check if the teacher's language level matches the student's language level
            if student.language_level in teacher.preferred_teaching_level:
                # Calculate the score based on age group compatibility
                score = calculate_age_group_score(student.date_of_birth, teacher.preferred_age_group)
                
                # Update the best match if the score is higher
                if score > max_score:
                    max_score = score
                    best_match = teacher
        
        # Add the matching pair to the matches list
        if best_match is not None:
            matches.append((student, best_match))
            teachers.remove(best_match)  # Remove the matched teacher from the list of available teachers
    
    return matches


def calculate_age_group_score(date_of_birth, preferred_age_group):
    # Convert the date of birth to datetime object
    dob = datetime.datetime.strptime(date_of_birth, "%d/%m/%Y")
    
    # Calculate the age based on the current date
    current_date = datetime.datetime.now()
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
    
    # Extract the minimum and maximum age from the preferred age group
    min_age, max_age = map(int, preferred_age_group.split('-'))
    
    # Calculate the score based on age group compatibility
    if min_age <= age <= max_age:
        return max_age - age + 1
    else:
        return 0


def save_matches_to_csv(matches, filename):
    fieldnames = ['Student Name', 'Teacher Name']
    
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for student, teacher in matches:
            writer.writerow({'Student Name': student.name, 'Teacher Name': teacher.name})
    
    print(f"Matching pairs saved to {filename}")


def main():
    # Load student data from CSV file
    students = load_students_from_csv('students.csv')

    # Load teacher data from CSV file
    teachers = load_teachers_from_csv('teachers.csv')

    # Match students with teachers
    matches = match_students_with_teachers(students, teachers)

    # Save the matching pairs to a CSV file
    save_matches_to_csv(matches, 'matching_pairs.csv')


if __name__ == '__main__':
    main()
