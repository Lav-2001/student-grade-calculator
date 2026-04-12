#-----------------------Student Grade Calculator-----------------------#
# Define a function called grade_calculator that takes 'mark' (number of subjects) as input
def grade_calculator(mark):
    mark_list = []  # Create an empty list to store all subject marks
    
    for i in range(mark):  # Loop 'mark' times (once for each subject)
        marks = int(input("Enter Subject Mark: "))  # Ask user to enter a mark and convert it to integer
        mark_list.append(marks)  # Add the entered mark to the list
    
    total_marks = sum(mark_list)  # Add all marks in the list to get total marks
    print(f"Total Marks: {total_marks}")  # Display the total marks
    
    full_marks = mark * 100  # Calculate full marks (each subject is out of 100)
    percentage = (total_marks / full_marks) * 100  # Calculate percentage using formula
    print(f"Percentage: {percentage}")  # Display the calculated percentage
    
    if percentage >= 90 and percentage <=100:  # Check if percentage is between 90 and 100
        print("Grade: A+")       # Print grade A+
        print("Outstanding")     # Print remark
    elif percentage >= 80 and percentage < 90:  # Check if percentage is between 80 and 89
        print("Grade: A")        # Print grade A
        print("Excellent")       # Print remark
    elif percentage >= 70 and percentage < 80:  # Check if percentage is between 70 and 79
        print("Grade: B+")       # Print grade B+
        print("Very Good")       # Print remark
    elif percentage >= 60 and percentage < 70:  # Check if percentage is between 60 and 69
        print("Grade: B")        # Print grade B
        print("Good")            # Print remark
    elif percentage >= 50 and percentage < 60:  # Check if percentage is between 50 and 59
        print("Grade: C+")       # Print grade C+
        print("Satisfactory")    # Print remark
    elif percentage >= 40 and percentage < 50:  # Check if percentage is between 40 and 49
        print("Grade: C")         # Print grade C
        print("Acceptable")      # Print remark
    elif percentage >= 35 and percentage < 40:  # Check if percentage is between 35 and 39
        print("Grade: D")        # Print grade D
        print("Basic")           # Print remark
    elif percentage < 35:  # Check if percentage is below 35
        print("Grade: NG")       # Print grade NG (Not Graded)
        print("Not Graded")      # Print remark

mark = int(input("Enter a number of subject: "))  # Ask user how many subjects and convert to integer
grade_calculator(mark)  # Call the function and pass the number of subjects to start the program