print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

print(min(1, 2, 3, 4, 0, 2, 1))
#prints the minimum value

print(max([1, 4, 9, 2, 5, 6, 8]))
#prints the maximum value

print(abs(-99))
#prints the absolute distance from zero to the value

print(abs(42))
#prints the absolute distance from zero to the value

print(sum([1, 2, 3, 4, 5]))
#prints the total sum of the list


if all([i > 5 for i in nums]):
   print("All larger than 5")
#prints "all larger than 5" if all the values in num are larger than 5

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")
#prints "at least one is even" if any of the values in num are an even number

for v in enumerate(nums):
   print(v)
#prints out the list, and prints out where each value is placed in the list
