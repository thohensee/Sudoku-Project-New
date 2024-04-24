
# Lab 2A - Right Triangle Validator

# Prompt for side lengths of triangle
lengths = []
lengths.append(float(input("Enter side 1: ")))
lengths.append(float(input("Enter side 1: ")))
lengths.append(float(input("Enter side 1: ")))

# Determine longest length e.g. potential hypotenuse
longest = max(lengths)

# Validate that the triangle is a right triangle using Pythagorean Theorem
sum = 0
for x in lengths:
    if x < longest:
        x = x**2
        sum += x

if sum**0.5 == longest:
    print("This triangle has a right angle!")
else:
    print("This triangle doesn’t have a right angle...")