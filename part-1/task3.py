# Define a function that counts vowels in a given text
def count_vowels(text):
    # List of vowels we want to check for
    vowels = 'aeiou'
    # Convert the whole text to lowercase so we count 'A' same as 'a'
    text_lower = text.lower()
    # Create a dictionary with each vowel as a key and start counts at 0
    vowel_counts = {v: 0 for v in vowels}
    # Variable to keep track of the total number of vowels
    total_count = 0

    # Look at each character in the lowercase text
    for char in text_lower:
        # If this character is one of our vowels
        if char in vowels:
            # Increase the count for that specific vowel
            vowel_counts[char] += 1
            # Also increase the total vowel count
            total_count += 1

    # After counting, print how many vowels we found in total
    print(f"Total number of vowels: {total_count}")
    # Then print the count for each individual vowel
    for v in vowels:
        print(f"{v}: {vowel_counts[v]}")

# Example string to run through our function
input_text = "I love python course and it helps me deal with the easy readable and executbale code."
# Call the vowel counter on the example text
count_vowels(input_text)