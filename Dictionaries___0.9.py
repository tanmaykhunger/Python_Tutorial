
phone = input("Phone: ")
number_translation = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for numbers in phone:
    output += number_translation.get(numbers, "!") + " "
print(output)