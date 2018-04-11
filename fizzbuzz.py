user_input = input("Enter a number between 1 and 100: ")
user_input = int(user_input)
current_number = 1

while current_number <= user_input:

    if current_number % 3 == 0 and current_number % 5 == 0:
        print("fizzbuzz")
    elif current_number % 3 == 0:
         print("fizz")
    elif current_number % 5 == 0:
         print("buzz")
    else:
        print(current_number)
    current_number += 1