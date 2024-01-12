from collections import OrderedDict

def word_histogram(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize an ordered dictionary to store the word counts
    histogram = OrderedDict()

    # Iterate through each word in the list of words
    for word in words:
        # Increment the count for the current word in the ordered dictionary
        histogram[word] = histogram.get(word, 0) + 1

    return histogram

# Prompt the user for input
user_input = input("Please enter a sentence: ")

# Call the function and get the result
result = word_histogram(user_input)

# Sort the result by counts in descending order
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Display the top three words
print("The top three words are:")
for word, count in sorted_result[:3]:
    print("{}: {}".format(word, count))
