"""
Write a Python function named count_vowels(text) that takes a string as input and returns a dictionary counting the occurrences of each vowel (a, e, i, o, u) present in the string.
"""

def count_vowels(text):
    vowels = "aeiou"
    counts = {}
    
    # Convert text to lowercase to make it case-insensitive
    for char in text.lower():
        if char in vowels:
            # Increment the count for the vowel, defaulting to 0 if not yet seen
            counts[char] = counts.get(char, 0) + 1
            
    # Sort the dictionary alphabetically by its keys (vowels)
    sorted_counts = dict(sorted(counts.items()))
    return sorted_counts

# Test the function
text = "Hello World! Welcome to Python programming."
print(count_vowels(text))