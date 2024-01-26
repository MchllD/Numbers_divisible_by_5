# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5


# pseudocode


# Given list of numbers
# condition message
# Create a list using list comprehension to store numbers divisible by 5
# Print numbers divisible by 5
# Iterate over the list of numbers divisible by 5

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ actual code ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


# Given list of numbers
num_list = [11, 25, 30, 41, 55, 67, 75, 80]

# condition message
print("\nThere is a list of numbers. Let's identify the numbers that are divisible by 5.")
print("\nGiven list:", num_list)

# Create a list using list comprehension to store numbers divisible by 5
divisible_by_5 = [num for num in num_list if num % 5 == 0]

# Print numbers divisible by 5
# Iterate over the list of numbers divisible by 5

