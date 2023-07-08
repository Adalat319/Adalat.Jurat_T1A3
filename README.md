# Uyghur Language Class Scheduling System

This is a Python terminal application that helps schedule Uyghur language classes by matching students with suitable teachers based on their preferences.

## Presentation Video

You can find a video demonstration of the application [here](insert_youtube_link).

## Acknowledgements

While building this Python terminal app, I would like to acknowledge the following reference sources:

- Class Recording: I would like to express my gratitude for the valuable insights and teaching provided by Akash. The knowledge and guidance shared during the class significantly influenced the development of this project.
- Chat GPT: I received exceptional assistance and guidance from Chat GPT, an AI language model developed by OpenAI. Whenever I encountered challenges or had queries, Chat GPT provided helpful suggestions and answers, greatly contributing to the overall content and functionality of this application.

## Source Control Repository

The source code for this application can be found on [GitHub](https://github.com/Adalat319/Adalat.Jurat_T1A3.git).

## Code Style Guide

The application follows the coding style guidelines outlined in PEP 8 (Python Enhancement Proposal 8). PEP 8 provides recommendations for code formatting, naming conventions, and code organization in Python. While I strive to adhere to these guidelines, as a beginner, there might be instances where I made mistakes or deviations. However, I continuously learn and improve my coding practices by referring to the official PEP 8 documentation available at [https://pep8.org/](https://pep8.org/).

## Features

### 1. Student Information Collection

Description: The application allows users to input and collect information about students, including their name, date of birth, country, language level, and primary language.

Implementation: The application uses variables to store the collected information and utilizes loops and conditional control structures to validate user inputs. Error handling is implemented to handle invalid inputs and provide appropriate error messages to the user.

### 2. Teacher Information Collection

Description: The application provides a feature to input and collect information about teachers, including their name, primary language, country, preferred age group, and preferred teaching level.

Implementation: Similar to the student information collection feature, this feature utilizes variables, loops, and conditional control structures to gather and validate user inputs. Error handling is implemented to handle any invalid inputs and guide the user through the data collection process.

### 3. Data Saving to CSV Files

Description: The application allows the collected student and teacher information to be saved to separate CSV files for future reference.

Implementation: The application uses the CSV module to write the student and teacher data to separate CSV files. It ensures that the data is properly formatted and handles any potential errors during the file-saving process.

## Implementation Plan

### 1. Collect Student and Teacher Information

Tasks:

- Collect student information (name, date of birth, country, primary language, language level).
- Validate and store student data.
- Collect teacher information (name, primary language, country, preferred age group, preferred teaching level).
- Validate and store teacher data.
Priority: High
Deadline: 1 week

### 2. Match Students and Teachers

Tasks:

- Analyze student and teacher data to identify potential matches.
- Consider age group, language level, and availability.
- Implement a matching algorithm to pair students with suitable teachers.
- Generate matched pairs for further processing.
Priority: Medium
Deadline: 2 weeks

### 3. Generate Matched Schedule

Tasks:

- Retrieve matched pairs of students and teachers.
- Create a schedule based on the availability of both parties.
- Consider time zone differences for international matches.
- Generate a finalized schedule with matched pairs and available time slots.
Priority: Medium
Deadline: 3 weeks

### 4. Store and Export Data

Tasks:

- Save matched pairs and schedule data.
- Store data in separate files for students and teachers.
- Implement export functionality to save data in CSV format.
Priority: Low
Deadline: 4 weeks

## Help Documentation

### Installation

To install the Uyghur Language Class Scheduling System, please follow these steps:

1.Clone the repository or download the project files to your local machine. You can clone the repository using the following command:

``` git clone <https://github.com/Adalat319/Adalat.Jurat_T1A3.git> ```

2.Navigate to the project directory:

   ```cd Adalat.Jurat_T1A3```

3.Create a virtual environment (optional but recommended) to isolate the project dependencies:

   ```python3 -m venv myenv```

4.Activate the virtual environment:

- On macOS and Linux:

     ```source myenv/bin/activate```

- On Windows:

     ```myenv\Scripts\activate```

5.Install the project dependencies:

   ```pip install -r requirements.txt```

### Usage

To use the Uyghur Language Class Scheduling System, you have two options:

Option 1: Using script.sh

1. Ensure that the `script.sh` file has execute permissions. If not, run the following command:

   ```$ chmod +x script.sh```

2. Run the `script.sh` file using the following command:

   ```./script.sh```

Option 2: Running main.py directly

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Activate the virtual environment (if created).

4. Run the main script using the following command:

   ```python main.py```

5. Follow the prompts and provide the required information to interact with the application.

6. To exit the application, enter `0` when prompted to select your role.

For any further assistance or questions, please contact me at <adalat.jurat@gmail.com>.
