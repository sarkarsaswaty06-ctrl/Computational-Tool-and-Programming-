# Develop a Python program to count the frequency of words and characters in a text string    
# Program to count the frequency of words and characters

text = input("Enter a text string: ")

# Count word frequency
words = text.split()
word_frequency = {}

for word in words:
    word = word.lower()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Count character frequency
character_frequency = {}

for char in text:
    if char != " ":  # Ignore spaces
        char = char.lower()
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1

# Display results
print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)

print("\nCharacter Frequency:")
for char, count in character_frequency.items():
    print(char, ":", count)
