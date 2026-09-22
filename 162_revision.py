# Problem Statement — Word Frequency Analyzer
#
# Write a Python program that accepts a sentence from the user
# and analyzes the words present in the sentence.
#
# The program should:
#
# 1. Take a sentence as input from the user.
#
# 2. Convert the entire sentence to lowercase.
#
# 3. Split the sentence into individual words and store them in a list.
#
# 4. Create a dictionary containing each unique word and its frequency.
#
# 5. Display the word frequency dictionary.
#
# 6. Find and display the word that occurs the most number of times.
#
# 7. Find and display all words that occur exactly once.
#
# 8. Create a dictionary comprehension containing only words
#    whose frequency is greater than 1.
#
# 9. Create a list comprehension containing words whose length
#    is greater than 4 characters.
#
# 10. Display the total number of words and the number of unique words.
#
# Restrictions:
#
# - Do not use collections.Counter.
# - Use a dictionary to store word frequencies.
# - Use loops and conditional statements where appropriate.
# - Use a dictionary comprehension and list comprehension
#   for the requested operations.
#
# Topics:
# Strings, string methods, lists, dictionaries, loops,
# conditions, dictionary comprehension, list comprehension,
# input and output.
sentence = input("Enter a sentence: ")

sentence = sentence.lower()
words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")

most_word = ""
most_count = 0

for word, count in frequency.items():
    if count > most_count:
        most_count = count
        most_word = word

once_words = []

for word, count in frequency.items():
    if count == 1:
        once_words.append(word)

repeated_words = {
    word: count
    for word, count in frequency.items()
    if count > 1
}

long_words = [word for word in words if len(word) > 4]

print(f"\nMost frequent word: {most_word} - {most_count} times")
print(f"Words occurring exactly once: {once_words}")
print(f"Repeated words: {repeated_words}")
print(f"Words with more than 4 characters: {long_words}")
print(f"Total words: {len(words)}")
print(f"Unique words: {len(frequency)}")