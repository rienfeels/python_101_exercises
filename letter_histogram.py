def letter_histogram(word):
    # Initialize an empty dictionary to store the letter counts
    histogram = {}

    # Iterate through each letter in the word
    for letter in word:
        # Increment the count for the current letter in the dictionary
        histogram[letter] = histogram.get(letter, 0) + 1

    return histogram

# Prompt the user for input
user_input = input("Please enter a word: ")

# Call the function and get the result
result = letter_histogram(user_input)

# Sort the result dictionary by keys
sorted_result = dict(sorted(result.items()))

# Display the sorted result
print(sorted_result)
