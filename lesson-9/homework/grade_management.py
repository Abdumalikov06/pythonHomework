import csv

# Function to read the grades from the CSV file and store in a list of dictionaries
def read_grades(file_name):
    grades = []
    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(row)
    return grades

# Function to calculate the average grade for each subject
def calculate_average_grades(grades):
    subject_grades = {}

    # Accumulate grades by subject
    for entry in grades:
        subject = entry['Subject']
        grade = int(entry['Grade'])

        if subject not in subject_grades:
            subject_grades[subject] = {'total': 0, 'count': 0}
        
        subject_grades[subject]['total'] += grade
        subject_grades[subject]['count'] += 1

    # Calculate average for each subject
    average_grades = {}
    for subject, data in subject_grades.items():
        average_grades[subject] = round(data['total'] / data['count'], 2)

    return average_grades

# Function to write the average grades to a new CSV file
def write_average_grades(file_name, average_grades):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        
        for subject, avg_grade in average_grades.items():
            writer.writerow([subject, avg_grade])

# Main program to execute the steps
def main():
    # Read the grades from grades.csv
    grades = read_grades('grades.csv')

    # Calculate the average grade for each subject
    average_grades = calculate_average_grades(grades)

    # Write the average grades to average_grades.csv
    write_average_grades('average_grades.csv', average_grades)

    print("Average grades have been written to 'average_grades.csv'.")

# Run the main program
if __name__ == "__main__":
    main()
