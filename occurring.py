# Algorithm implementation in Python

# Step 1: Open and read the file
with open("text.txt", "r") as file:
    text = file.read().lower()  # convert to lowercase

# Step 2: Remove punctuation
import string
for ch in string.punctuation:
    text = text.replace(ch, "")

# Step 3: Split text into words
words = text.split()

# Step 4: Count word frequencies
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Step 5: Find the most occurring word
most_common_word = max(word_count, key=word_count.get)
count = word_count[most_common_word]

# Step 6: Print the result
print(f"The most occurring word is '{most_common_word}' appearing {count} times.")
