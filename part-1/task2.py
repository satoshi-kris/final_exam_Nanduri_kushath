# Define a function that takes a list of grades and checks each one
def check_grades(grades):
    # Go through each grade in the grades list
    for grade in grades:
        # If the grade is 75 or higher, it’s a pass
        if grade >= 75:
            print("Pass")
        # Otherwise, it’s not a pass
        else:
            print("No")

# Create a sample list of five grades to test the function
test_grades = [80, 60, 90, 74, 75]
# Call the function and see the output for each grade
check_grades(test_grades)