my_string = "The quick brown fox jumps over the lazy dog"

# Extract the words in reverse order
words_reverse =my_string.split()[-1: :-1]
reverse_string = " ".join(words_reverse)   # join function is used to concatenate the elements
print(reverse_string)

# Extract alternating words starting from index 1
listed_words = my_string.split()[1::2]
print(listed_words)
alternating_words = (" ".join(listed_words))
print(alternating_words)

# Extract a substring with multiple ranges
substring_ranges =my_string[4:9] + my_string[16:20] + my_string[-8:-4]
print(substring_ranges)

# Extracting a multiple substring using a list of indices
string = "Roman Humagain"
indices = [0,4,5,6]

substrings = [string[i] for i in indices]
print(''.join(substrings))

# Spliting a string into equal-sized chunks
my_str = "PythonIsLove"
chunk_size = 6

chunks = [my_str[i:i+chunk_size] for i in range(0, len(my_str), chunk_size)]
print(chunks)