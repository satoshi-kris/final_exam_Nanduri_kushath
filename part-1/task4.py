# Start with an empty list to store all entered numbers
numbers = []

# Keep asking the user until they type “done”
while True:
    # Prompt for input and remove extra spaces
    user_input = input("Enter a number (or 'done' to finish): ").strip()
    # If the user typed “done” (in any case), break out of the loop
    if user_input.lower() == "done":
        break
    # If they just hit enter without typing anything, warn and restart the loop
    if not user_input:
        print("Invalid input. Try again.")
        continue
    # Try to convert their input into a number
    try:
        num = float(user_input)
        # If it worked, add it to our list
        numbers.append(num)
    # If conversion failed, tell them and let them try again
    except ValueError:
        print("Invalid input. Try again.")

# After the loop, check if we got any valid numbers
if numbers:
    # Count how many numbers there are
    total = len(numbers)
    # Calculate the average and round it to two decimal places
    average = round(sum(numbers) / total, 2)
    # Print out the count and the average
    print(f"Total numbers entered: {total}")
    print(f"Average: {average}")
else:
    # If no numbers were ever added, let the user know
    print("No valid numbers were entered.")