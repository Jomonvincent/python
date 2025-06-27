# Sample text
text = "hello world hello python world python python"

# Initialize an empty dictionary to store word counts
word_count = {}

# Split the text into words
words = text.split()

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1  # Increment the count if the word is already in the dictionary
    else:
        word_count[word] = 1  # Initialize the count if the word is not in the dictionary

# Print the word counts
print(word_count)
